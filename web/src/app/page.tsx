"use client";

import { useEffect, useMemo, useState } from "react";

import { PaperCard } from "../components/PaperCard";
import type { DigestEntry, Paper, Stats } from "../lib/generated";
import { loadGenerated } from "../lib/generated";

const TOPIC_TRUNKS = [
  { key: "stochastic_analysis", label: "随机分析" },
  { key: "statistical_physics", label: "统计物理" },
  { key: "ai_for_physics", label: "AI for Physics" },
  { key: "bridges", label: "桥接主题" },
  { key: "urban_complex_systems", label: "城市复杂系统" },
];

export default function HomePage() {
  const [papers, setPapers] = useState<Paper[]>([]);
  const [stats, setStats] = useState<Stats>({ total_papers: 0, by_status: {}, by_topic: {} });
  const [digests, setDigests] = useState<DigestEntry[]>([]);

  useEffect(() => {
    loadGenerated<Paper[]>("papers", []).then(setPapers);
    loadGenerated<Stats>("stats", { total_papers: 0, by_status: {}, by_topic: {} }).then(setStats);
    loadGenerated<DigestEntry[]>("digests", []).then(setDigests);
  }, []);

  const readingNotes = useMemo(() => digests.filter((d) => d.type === "reading_note"), [digests]);

  // 7天和30天阅读统计
  const { readingLast7, readingLast30, latestNotes, readsByDay } = useMemo(() => {
    const today = new Date();
    const days7 = new Date(today.getTime() - 7 * 24 * 3600 * 1000);
    const days30 = new Date(today.getTime() - 30 * 24 * 3600 * 1000);
    let c7 = 0;
    let c30 = 0;
    const byDay = new Map<string, number>();
    for (const n of readingNotes) {
      if (!n.created_at || n.created_at === "shared") continue;
      const d = new Date(n.created_at);
      if (d >= days7) c7++;
      if (d >= days30) c30++;
      byDay.set(n.created_at, (byDay.get(n.created_at) ?? 0) + 1);
    }
    const latest = [...readingNotes]
      .sort((a, b) => (b.created_at ?? "").localeCompare(a.created_at ?? ""))
      .slice(0, 5);
    // 过去 14 天热度图
    const days: Array<{ date: string; count: number }> = [];
    for (let i = 13; i >= 0; i--) {
      const d = new Date(today.getTime() - i * 24 * 3600 * 1000);
      const iso = d.toISOString().slice(0, 10);
      days.push({ date: iso, count: byDay.get(iso) ?? 0 });
    }
    return { readingLast7: c7, readingLast30: c30, latestNotes: latest, readsByDay: days };
  }, [readingNotes]);

  // 主干主题进度（已入库论文数 vs 已读）
  const trunkProgress = useMemo(() => {
    return TOPIC_TRUNKS.map(({ key, label }) => {
      const total = stats.by_topic?.[key] ?? 0;
      return { key, label, total };
    });
  }, [stats]);

  const topPapers = useMemo(() => papers.slice(0, 6), [papers]);
  const readCount = stats.by_status?.read ?? 0;

  return (
    <div className="page">
      {/* Hero + 关键指标 */}
      <section className="hero card">
        <p className="eyebrow">Research Dashboard</p>
        <h2>Frontier literature tracker for one continuous research program</h2>
        <p>
          随机路径 → 密度演化 → 热力学/信息论解释 → 生成机制 → 城市应用。
          目前的重点前沿是<strong>非平衡统计物理 × 生成模型</strong>。
        </p>
        <div className="statsGrid">
          <div>
            <strong>{stats.total_papers}</strong>
            <span>已入库论文</span>
          </div>
          <div>
            <strong>{readingNotes.length}</strong>
            <span>精读笔记</span>
          </div>
          <div>
            <strong>{readCount}</strong>
            <span>已标记阅读</span>
          </div>
          <div>
            <strong>{readingLast7}</strong>
            <span>近 7 天新笔记</span>
          </div>
          <div>
            <strong>{readingLast30}</strong>
            <span>近 30 天新笔记</span>
          </div>
        </div>
      </section>

      {/* 阅读热度图 */}
      <section className="card">
        <h3>过去 14 天阅读热度</h3>
        <div style={{ display: "flex", gap: 4, marginTop: 16, flexWrap: "wrap" }}>
          {readsByDay.map(({ date, count }) => {
            const intensity = Math.min(count, 6);
            const bg = count === 0 ? "#eee" : `rgba(29, 53, 87, ${0.15 + intensity * 0.15})`;
            return (
              <div
                key={date}
                title={`${date}: ${count} 篇`}
                style={{
                  width: 32,
                  height: 32,
                  borderRadius: 4,
                  background: bg,
                  color: count > 2 ? "#fff" : "#333",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: 11,
                  fontWeight: 600,
                }}
              >
                {count > 0 ? count : ""}
              </div>
            );
          })}
        </div>
        <p className="muted" style={{ fontSize: 12, marginTop: 8 }}>
          颜色深浅代表当日新增精读笔记数。数字为笔记数（0 不显示）。
        </p>
      </section>

      {/* 5 大主题分布 */}
      <section className="card">
        <h3>5 大主题论文数</h3>
        <div style={{ display: "flex", flexDirection: "column", gap: 10, marginTop: 14 }}>
          {trunkProgress.map(({ key, label, total }) => {
            const maxTotal = Math.max(...trunkProgress.map((t) => t.total), 1);
            const pct = (total / maxTotal) * 100;
            return (
              <div key={key} style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <span style={{ width: 130, fontSize: 13 }}>{label}</span>
                <div
                  style={{
                    flex: 1,
                    height: 18,
                    background: "#eee",
                    borderRadius: 4,
                    overflow: "hidden",
                  }}
                >
                  <div
                    style={{
                      width: `${pct}%`,
                      height: "100%",
                      background: "linear-gradient(90deg, #a8dadc, #1d3557)",
                    }}
                  />
                </div>
                <span style={{ fontSize: 13, fontWeight: 600, width: 40, textAlign: "right" }}>
                  {total}
                </span>
              </div>
            );
          })}
        </div>
      </section>

      {/* 最近精读笔记 */}
      <section>
        <div className="sectionHeader">
          <h2>最近精读</h2>
          <a href="/notes">查看全部 {readingNotes.length} 篇 →</a>
        </div>
        <div className="grid">
          {latestNotes.map((note) => (
            <a
              key={note.path}
              href={`/notes/view?path=${encodeURIComponent(note.path)}`}
              className="card"
              style={{ textDecoration: "none", color: "inherit", display: "block" }}
            >
              <p className="eyebrow" style={{ marginBottom: 4 }}>
                {note.created_at}
              </p>
              <h4 style={{ margin: "4px 0 8px", fontSize: 15, lineHeight: 1.35 }}>
                {note.title}
              </h4>
              {note.authors && (
                <p style={{ fontSize: 12, color: "#666", margin: "0 0 4px" }}>{note.authors}</p>
              )}
              {note.venue && (
                <p style={{ fontSize: 11, color: "#888", margin: 0 }}>{note.venue}</p>
              )}
            </a>
          ))}
        </div>
      </section>

      {/* 高优先级论文 */}
      <section>
        <div className="sectionHeader">
          <h2>High-Priority Papers</h2>
          <a href="/library">Open full library</a>
        </div>
        <div className="grid">
          {topPapers.map((paper) => (
            <PaperCard key={paper.id} paper={paper} />
          ))}
        </div>
      </section>
    </div>
  );
}
