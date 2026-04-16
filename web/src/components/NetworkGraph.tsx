"use client";

import { useMemo, useState, Suspense } from "react";
import dynamic from "next/dynamic";
import type { GraphPayload, GraphNode } from "../lib/generated";

const GraphCanvas = dynamic(
  () => import("reagraph").then((mod) => mod.GraphCanvas),
  { ssr: false },
);

type Props = {
  data: GraphPayload;
  viewMode: string;
};

const TYPE_COLORS: Record<string, string> = {
  topic: "#a8dadc",
  paper: "#f1faee",
  author: "#fca311",
  venue: "#e76f51",
};

const TYPE_LABELS: Record<string, string> = {
  topic: "主题",
  paper: "论文",
  author: "作者",
  venue: "期刊",
};

const EDGE_COLORS: Record<string, string> = {
  taxonomy: "rgba(29, 53, 87, 0.15)",
  belongs_to: "rgba(168, 218, 220, 0.3)",
  authored: "rgba(252, 163, 17, 0.25)",
  coauthor: "rgba(252, 163, 17, 0.4)",
  published_in: "rgba(231, 111, 81, 0.3)",
};

function nodeSize(node: GraphNode): number {
  if (node.type === "topic") return node.is_leaf ? 3 : 5;
  if (node.type === "author") return Math.min(2 + (node.paper_count ?? 1) * 0.8, 8);
  if (node.type === "venue") return Math.min(3 + (node.paper_count ?? 1) * 0.5, 10);
  return 2;
}

function nodeLabel(node: GraphNode, viewMode: string): string {
  if (viewMode === "authors" && node.affiliation) {
    return `${node.label}\n${node.affiliation}`;
  }
  if (viewMode === "venues" && node.tier !== undefined) {
    return `${node.label} (T${node.tier})`;
  }
  return node.label;
}

export function NetworkGraph({ data, viewMode }: Props) {
  const types = useMemo(() => {
    const set = new Set<string>();
    for (const n of data.nodes) set.add(n.type);
    return Array.from(set);
  }, [data.nodes]);

  const [disabledTypes, setDisabledTypes] = useState<Set<string>>(new Set());
  const [minYear, setMinYear] = useState<number>(2000);
  const [focusId, setFocusId] = useState<string | null>(null);

  // 年份滑块范围
  const yearRange = useMemo(() => {
    const years = data.nodes
      .filter((n) => n.type === "paper" && n.year)
      .map((n) => n.year!)
      .filter((y) => y && y > 1900);
    if (years.length === 0) return { min: 2000, max: 2026 };
    return { min: Math.min(...years), max: Math.max(...years) };
  }, [data.nodes]);

  // 邻居查找（当聚焦某节点时，保留它 + 1 跳邻居）
  const visibleNodeIds = useMemo(() => {
    if (!focusId) return null;
    const keep = new Set<string>([focusId]);
    for (const e of data.edges) {
      if (e.source === focusId) keep.add(e.target);
      if (e.target === focusId) keep.add(e.source);
    }
    return keep;
  }, [focusId, data.edges]);

  const reagraphNodes = useMemo(() => {
    return data.nodes
      .filter((n) => {
        if (disabledTypes.has(n.type)) return false;
        if (n.type === "paper" && n.year && n.year < minYear) return false;
        if (visibleNodeIds && !visibleNodeIds.has(n.id)) return false;
        return true;
      })
      .map((n) => ({
        id: n.id,
        label: nodeLabel(n, viewMode),
        fill: focusId === n.id
          ? "#e63946"
          : (TYPE_COLORS[n.type] ?? "#ddd"),
        size: focusId === n.id ? nodeSize(n) + 4 : nodeSize(n),
      }));
  }, [data.nodes, disabledTypes, minYear, visibleNodeIds, viewMode, focusId]);

  const visibleIds = useMemo(() => new Set(reagraphNodes.map((n) => n.id)), [reagraphNodes]);

  const reagraphEdges = useMemo(
    () =>
      data.edges
        .filter((e) => visibleIds.has(e.source) && visibleIds.has(e.target))
        .map((e, i) => ({
          id: `${e.source}-${e.target}-${i}`,
          source: e.source,
          target: e.target,
          fill: EDGE_COLORS[e.type] ?? "rgba(0,0,0,0.1)",
          size: e.weight ? Math.min(1 + e.weight * 0.3, 4) : 1,
        })),
    [data.edges, visibleIds],
  );

  const toggleType = (t: string) => {
    const next = new Set(disabledTypes);
    if (next.has(t)) next.delete(t);
    else next.add(t);
    setDisabledTypes(next);
  };

  return (
    <div>
      {/* 控制面板 */}
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: 16,
          alignItems: "center",
          padding: "12px 16px",
          background: "#f8f9fa",
          borderRadius: 8,
          marginBottom: 12,
          fontSize: 13,
        }}
      >
        <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
          <span style={{ fontWeight: 600 }}>显示：</span>
          {types.map((t) => (
            <button
              key={t}
              onClick={() => toggleType(t)}
              style={{
                padding: "4px 10px",
                borderRadius: 12,
                border: disabledTypes.has(t) ? "1px solid #ccc" : `2px solid ${TYPE_COLORS[t] ?? "#666"}`,
                background: disabledTypes.has(t) ? "#fff" : TYPE_COLORS[t] ?? "#ddd",
                color: disabledTypes.has(t) ? "#999" : "#1d3557",
                fontSize: 12,
                fontWeight: 600,
                cursor: "pointer",
                textDecoration: disabledTypes.has(t) ? "line-through" : "none",
              }}
            >
              {TYPE_LABELS[t] ?? t}
            </button>
          ))}
        </div>

        {yearRange.min < yearRange.max && (
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ fontWeight: 600 }}>年份 ≥</span>
            <input
              type="range"
              min={yearRange.min}
              max={yearRange.max}
              value={minYear}
              onChange={(e) => setMinYear(Number(e.target.value))}
              style={{ width: 150 }}
            />
            <span style={{ fontFamily: "monospace" }}>{minYear}</span>
          </div>
        )}

        {focusId && (
          <button
            onClick={() => setFocusId(null)}
            style={{
              padding: "4px 12px",
              borderRadius: 12,
              border: "1px solid #e63946",
              background: "#fff",
              color: "#e63946",
              fontSize: 12,
              fontWeight: 600,
              cursor: "pointer",
            }}
          >
            清除聚焦 ✕
          </button>
        )}

        <div style={{ marginLeft: "auto", color: "#666", fontSize: 12 }}>
          {reagraphNodes.length} 节点 · {reagraphEdges.length} 边
        </div>
      </div>

      {/* 图谱 */}
      <div
        style={{
          height: "70vh",
          width: "100%",
          border: "1px solid #eee",
          borderRadius: 8,
          position: "relative",
        }}
      >
        <Suspense fallback={<p>Loading graph…</p>}>
          <GraphCanvas
            nodes={reagraphNodes}
            edges={reagraphEdges}
            layoutType="forceDirected2d"
            labelType="auto"
            draggable
            animated={false}
            onNodeClick={(node) => setFocusId(node.id)}
          />
        </Suspense>
      </div>

      {focusId && (
        <p className="muted" style={{ fontSize: 12, marginTop: 8 }}>
          当前聚焦：<code>{focusId}</code> 及其 1 跳邻居。再次点击其他节点切换焦点。
        </p>
      )}
      <p className="muted" style={{ fontSize: 11, marginTop: 4 }}>
        💡 小贴士：点击节点聚焦其邻居子图；用左上角按钮切换显示的节点类型；
        拖动年份滑块过滤早年论文。
      </p>
    </div>
  );
}
