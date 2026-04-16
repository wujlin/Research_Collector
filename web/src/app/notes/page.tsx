"use client";

import { useEffect, useMemo, useState } from "react";
import type { DigestEntry } from "../../lib/generated";
import { loadGenerated } from "../../lib/generated";

const TOPIC_GROUPS: { label: string; keywords: string[] }[] = [
  { label: "生成模型 / AI for Physics", keywords: ["生成", "扩散", "flow", "score", "DDPM", "physics-informed", "variational"] },
  { label: "随机热力学 / 非平衡", keywords: ["热力学", "非平衡", "涨落", "熵产生", "随机"] },
  { label: "数学骨架 / SDE", keywords: ["SDE", "Fokker-Planck", "最优传输", "HJB", "Lyapunov", "McKean"] },
  { label: "桥梁主题", keywords: ["自由能", "信息几何", "主动推断", "变分"] },
  { label: "其他", keywords: [] },
];

function classifyByTopic(entry: DigestEntry): string {
  const joined = (entry.topics ?? []).join(" ") + " " + entry.title;
  for (const group of TOPIC_GROUPS) {
    if (group.keywords.length === 0) continue;
    for (const kw of group.keywords) {
      if (joined.toLowerCase().includes(kw.toLowerCase())) return group.label;
    }
  }
  return "其他";
}

function readingMinutes(wordCount?: number): number {
  if (!wordCount) return 5;
  return Math.max(5, Math.round(wordCount / 200));
}

export default function NotesPage() {
  const [entries, setEntries] = useState<DigestEntry[]>([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    loadGenerated<DigestEntry[]>("digests", []).then((all) => {
      const notes = all.filter((e) => e.type === "reading_note");
      setEntries(notes);
    });
  }, []);

  const filtered = useMemo(() => {
    if (!query.trim()) return entries;
    const q = query.toLowerCase();
    return entries.filter(
      (e) =>
        e.title.toLowerCase().includes(q) ||
        (e.authors ?? "").toLowerCase().includes(q) ||
        (e.venue ?? "").toLowerCase().includes(q) ||
        (e.topics ?? []).some((t) => t.toLowerCase().includes(q)),
    );
  }, [entries, query]);

  const grouped = useMemo(() => {
    const map = new Map<string, DigestEntry[]>();
    for (const group of TOPIC_GROUPS) map.set(group.label, []);
    for (const entry of filtered) {
      const g = classifyByTopic(entry);
      map.get(g)!.push(entry);
    }
    return map;
  }, [filtered]);

  return (
    <div className="page">
      <section className="card">
        <p className="eyebrow">Reading Archive</p>
        <h2>精读笔记 · {entries.length} 篇</h2>
        <p>
          按主题分组的深度阅读笔记，每篇都包含作者机构、核心推导与关键图片。
          当前覆盖 <strong>生成模型</strong>、<strong>随机热力学</strong>、
          <strong>SDE 理论</strong>与<strong>桥梁主题</strong>的前沿工作。
        </p>
        <input
          type="search"
          placeholder="搜索标题 / 作者 / 期刊 / 主题…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            marginTop: 12,
            padding: "10px 14px",
            width: "100%",
            maxWidth: 420,
            borderRadius: 6,
            border: "1px solid #ccc",
            fontSize: 14,
          }}
        />
      </section>

      {TOPIC_GROUPS.map((group) => {
        const items = grouped.get(group.label) ?? [];
        if (items.length === 0) return null;
        return (
          <section key={group.label}>
            <div className="sectionHeader">
              <h2>{group.label}</h2>
              <span className="muted">{items.length} 篇</span>
            </div>
            <div className="grid">
              {items
                .sort((a, b) => (b.created_at ?? "").localeCompare(a.created_at ?? ""))
                .map((entry) => (
                  <a
                    key={entry.path}
                    href={`/notes/view?path=${encodeURIComponent(entry.path)}`}
                    className="card"
                    style={{ textDecoration: "none", color: "inherit", display: "block" }}
                  >
                    <p className="eyebrow" style={{ marginBottom: 6 }}>
                      {entry.created_at} · {readingMinutes(entry.word_count)} min 阅读
                    </p>
                    <h3 style={{ margin: "4px 0 8px", fontSize: 16, lineHeight: 1.35 }}>
                      {entry.title}
                    </h3>
                    {entry.authors && (
                      <p style={{ fontSize: 13, color: "#555", margin: "0 0 4px" }}>
                        {entry.authors}
                      </p>
                    )}
                    {entry.venue && (
                      <p style={{ fontSize: 12, color: "#888", margin: "0 0 8px" }}>
                        {entry.venue}
                      </p>
                    )}
                    {entry.topics && entry.topics.length > 0 && (
                      <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
                        {entry.topics.slice(0, 4).map((t) => (
                          <span
                            key={t}
                            style={{
                              fontSize: 11,
                              padding: "2px 8px",
                              borderRadius: 10,
                              background: "#a8dadc",
                              color: "#1d3557",
                            }}
                          >
                            {t}
                          </span>
                        ))}
                      </div>
                    )}
                  </a>
                ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
