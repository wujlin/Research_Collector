"""知识图谱数据导出：topic / paper / author / venue 四层网络。"""

from __future__ import annotations

import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Any

from src.storage.database import Database
from src.utils.helpers import dump_json, flatten_topics, load_config


class KnowledgeGraphExporter:
    def __init__(self, output_path: str = "web/public/generated/graph.json"):
        self.output_path = Path(output_path)

    def export(self, database: Database, max_papers: int = 80) -> dict[str, Any]:
        taxonomy = load_config("topics.yaml")
        topic_entries = flatten_topics(taxonomy)
        papers = database.list_papers(limit=max_papers)

        nodes: list[dict[str, Any]] = []
        edges: list[dict[str, Any]] = []

        # ── Topic 节点 + taxonomy 边 ──
        for entry in topic_entries:
            nodes.append({
                "id": entry["key"],
                "label": entry["display_name"],
                "type": "topic",
                "parent_key": entry["parent_key"],
                "depth": entry.get("depth", 0),
                "is_leaf": entry.get("is_leaf", False),
            })
            if entry["parent_key"]:
                edges.append({
                    "source": entry["parent_key"],
                    "target": entry["key"],
                    "type": "taxonomy",
                })

        # ── 预计算（避免 ORM lazy load 在 session 外失败） ──
        author_paper_counts: dict[int, int] = defaultdict(int)
        paper_venue_map: dict[int, dict] = {}
        try:
            raw = database.engine.raw_connection()
            cur = raw.cursor()
            cur.execute("SELECT author_id, COUNT(*) FROM paper_authors GROUP BY author_id")
            for aid, cnt in cur.fetchall():
                author_paper_counts[aid] = cnt
            cur.execute("""
                SELECT v.id, v.name, v.display_name, v.tier, v.reputation, v.paper_count
                FROM venues v
            """)
            venue_cache = {
                row[0]: {"id": row[0], "name": row[1], "display_name": row[2] or row[1],
                         "tier": row[3], "reputation": row[4], "paper_count": row[5]}
                for row in cur.fetchall()
            }
            cur.execute("SELECT id, venue_id FROM papers WHERE venue_id IS NOT NULL")
            for pid, vid in cur.fetchall():
                if vid in venue_cache:
                    paper_venue_map[pid] = venue_cache[vid]
            raw.close()
        except Exception:
            pass

        # ── Paper 节点 + paper-topic / paper-author / paper-venue 边 ──
        seen_author_ids: set[int] = set()
        seen_venue_ids: set[int] = set()

        for paper in papers:
            paper_id = f"paper:{paper.id}"
            nodes.append({
                "id": paper_id,
                "label": paper.title,
                "type": "paper",
                "year": paper.year,
                "relevance_score": paper.relevance_score,
                "citation_count": paper.citation_count,
                "tier": paper.tier,
                "venue": paper.journal or paper.venue or "",
            })
            for topic in paper.topics[:3]:
                edges.append({"source": paper_id, "target": topic.key, "type": "belongs_to"})

            for author in paper.authors:
                author_node_id = f"author:{author.id}"
                if author.id not in seen_author_ids:
                    seen_author_ids.add(author.id)
                    nodes.append({
                        "id": author_node_id,
                        "label": author.name,
                        "type": "author",
                        "affiliation": author.affiliation or "",
                        "h_index": author.h_index,
                        "paper_count": author_paper_counts.get(author.id, 0),
                    })
                edges.append({"source": author_node_id, "target": paper_id, "type": "authored"})

            v_info = paper_venue_map.get(paper.id)
            if v_info and v_info["id"] not in seen_venue_ids:
                seen_venue_ids.add(v_info["id"])
                nodes.append({
                    "id": f"venue:{v_info['id']}",
                    "label": v_info["display_name"],
                    "type": "venue",
                    "tier": v_info["tier"],
                    "reputation": v_info["reputation"],
                    "paper_count": v_info["paper_count"],
                })
            if v_info:
                edges.append({
                    "source": paper_id,
                    "target": f"venue:{v_info['id']}",
                    "type": "published_in",
                })

        # ── Co-authorship 边（仅在可见作者之间） ──
        coauthor_edges = self._load_coauthorship_edges(database, seen_author_ids)
        edges.extend(coauthor_edges)

        payload = {
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "topics": sum(1 for n in nodes if n["type"] == "topic"),
                "papers": sum(1 for n in nodes if n["type"] == "paper"),
                "authors": sum(1 for n in nodes if n["type"] == "author"),
                "venues": sum(1 for n in nodes if n["type"] == "venue"),
                "coauthor_edges": len(coauthor_edges),
            },
        }
        dump_json(self.output_path, payload)
        return payload

    @staticmethod
    def _load_coauthorship_edges(
        database: Database, visible_author_ids: set[int]
    ) -> list[dict[str, Any]]:
        """从 author_coauthors 表加载可见作者之间的合作边。"""
        edges: list[dict[str, Any]] = []
        try:
            raw_conn = database.engine.raw_connection()
            cursor = raw_conn.cursor()
            cursor.execute(
                "SELECT author_a_id, author_b_id, shared_papers FROM author_coauthors"
            )
            for a, b, count in cursor.fetchall():
                if a in visible_author_ids and b in visible_author_ids:
                    edges.append({
                        "source": f"author:{a}",
                        "target": f"author:{b}",
                        "type": "coauthor",
                        "weight": count,
                    })
            raw_conn.close()
        except Exception:
            pass
        return edges

    def export_author_network(
        self, database: Database, output_path: str = "web/public/generated/author_network.json"
    ) -> dict[str, Any]:
        """独立的作者合作网络导出，包含全部作者。"""
        out = Path(output_path)
        nodes: list[dict[str, Any]] = []
        edges: list[dict[str, Any]] = []

        raw_conn = database.engine.raw_connection()
        cursor = raw_conn.cursor()

        # 只导出至少有 1 篇论文的作者
        cursor.execute("""
            SELECT a.id, a.name, a.affiliation, a.h_index, a.openalex_id,
                   COUNT(pa.paper_id) as paper_count
            FROM authors a
            JOIN paper_authors pa ON a.id = pa.author_id
            GROUP BY a.id
            HAVING paper_count >= 1
        """)
        author_ids: set[int] = set()
        for row in cursor.fetchall():
            aid = row[0]
            author_ids.add(aid)
            nodes.append({
                "id": f"author:{aid}",
                "label": row[1],
                "affiliation": row[2] or "",
                "h_index": row[3],
                "paper_count": row[5],
            })

        cursor.execute("SELECT author_a_id, author_b_id, shared_papers FROM author_coauthors")
        for a, b, count in cursor.fetchall():
            if a in author_ids and b in author_ids:
                edges.append({
                    "source": f"author:{a}",
                    "target": f"author:{b}",
                    "weight": count,
                })

        raw_conn.close()

        payload = {
            "nodes": nodes,
            "edges": edges,
            "stats": {"authors": len(nodes), "coauthor_edges": len(edges)},
        }
        dump_json(out, payload)
        return payload

    def export_venue_network(
        self, database: Database, output_path: str = "web/public/generated/venue_network.json"
    ) -> dict[str, Any]:
        """期刊网络导出：venue 节点 + 共享作者构成的边。"""
        out = Path(output_path)
        raw_conn = database.engine.raw_connection()
        cursor = raw_conn.cursor()

        cursor.execute("""
            SELECT v.id, v.name, v.display_name, v.tier, v.reputation, v.paper_count
            FROM venues v WHERE v.paper_count > 0
        """)
        nodes = []
        venue_ids: set[int] = set()
        for row in cursor.fetchall():
            venue_ids.add(row[0])
            nodes.append({
                "id": f"venue:{row[0]}",
                "label": row[2] or row[1],
                "tier": row[3],
                "reputation": row[4],
                "paper_count": row[5],
            })

        # 基于共享作者构建 venue 之间的连接
        cursor.execute("""
            SELECT p.venue_id, pa.author_id
            FROM papers p
            JOIN paper_authors pa ON p.id = pa.paper_id
            WHERE p.venue_id IS NOT NULL
        """)
        venue_authors: dict[int, set[int]] = defaultdict(set)
        for vid, aid in cursor.fetchall():
            venue_authors[vid].add(aid)

        raw_conn.close()

        edges: list[dict[str, Any]] = []
        venue_list = sorted(venue_authors.keys())
        for i, va in enumerate(venue_list):
            for vb in venue_list[i + 1:]:
                shared = len(venue_authors[va] & venue_authors[vb])
                if shared > 0:
                    edges.append({
                        "source": f"venue:{va}",
                        "target": f"venue:{vb}",
                        "weight": shared,
                    })

        payload = {
            "nodes": nodes,
            "edges": edges,
            "stats": {"venues": len(nodes), "venue_edges": len(edges)},
        }
        dump_json(out, payload)
        return payload
