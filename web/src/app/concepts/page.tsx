"use client";

import { useEffect, useMemo, useState } from "react";
import { loadGenerated } from "../../lib/generated";
import { CATEGORY_COLORS, CATEGORY_LABELS, type Concept } from "../../lib/concepts";

export default function ConceptsPage() {
  const [concepts, setConcepts] = useState<Concept[]>([]);
  const [query, setQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState<string>("all");

  useEffect(() => {
    loadGenerated<Concept[]>("concepts", []).then(setConcepts);
  }, []);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return concepts.filter((c) => {
      if (activeCategory !== "all" && c.category !== activeCategory) return false;
      if (!q) return true;
      return (
        c.display_name.toLowerCase().includes(q) ||
        c.aliases.some((a) => a.toLowerCase().includes(q)) ||
        c.short_description.toLowerCase().includes(q)
      );
    });
  }, [concepts, query, activeCategory]);

  const categories = useMemo(() => {
    const set = new Set<string>();
    for (const c of concepts) set.add(c.category);
    return Array.from(set).sort();
  }, [concepts]);

  const maxCount = Math.max(...filtered.map((c) => c.note_count), 1);

  return (
    <div className="page">
      <section className="card">
        <p className="eyebrow">Concept Index</p>
        <h2>概念词条库 · {concepts.length} 个概念</h2>
        <p>
          跨越 <strong>{new Set(concepts.flatMap((c) => c.occurrences.map((o) => o.note_path))).size}</strong>{" "}
          篇精读笔记提取的关键概念索引。点击任一概念查看它在哪些笔记中出现，以及每次出现的上下文片段。
        </p>
        <div style={{ display: "flex", gap: 8, marginTop: 16, flexWrap: "wrap" }}>
          <button
            onClick={() => setActiveCategory("all")}
            style={pillStyle(activeCategory === "all", "#333")}
          >
            全部
          </button>
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setActiveCategory(cat)}
              style={pillStyle(activeCategory === cat, CATEGORY_COLORS[cat] ?? "#666")}
            >
              {CATEGORY_LABELS[cat] ?? cat}
            </button>
          ))}
        </div>
        <input
          type="search"
          placeholder="搜索概念名、别名或描述…"
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

      <section>
        <div className="grid">
          {filtered.map((c) => {
            const width = (c.note_count / maxCount) * 100;
            return (
              <a
                key={c.id}
                href={`/concepts/view?id=${c.id}`}
                className="card"
                style={{ textDecoration: "none", color: "inherit", display: "block" }}
              >
                <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                  <span
                    style={{
                      fontSize: 10,
                      padding: "2px 8px",
                      borderRadius: 10,
                      background: CATEGORY_COLORS[c.category] ?? "#666",
                      color: "#fff",
                      fontWeight: 600,
                    }}
                  >
                    {CATEGORY_LABELS[c.category] ?? c.category}
                  </span>
                </div>
                <h3 style={{ margin: "4px 0 6px", fontSize: 16 }}>{c.display_name}</h3>
                <p style={{ fontSize: 12, color: "#555", margin: "0 0 10px", lineHeight: 1.45 }}>
                  {c.short_description}
                </p>
                <div
                  style={{
                    height: 6,
                    background: "#eee",
                    borderRadius: 3,
                    overflow: "hidden",
                    marginBottom: 4,
                  }}
                >
                  <div
                    style={{
                      width: `${width}%`,
                      height: "100%",
                      background: CATEGORY_COLORS[c.category] ?? "#666",
                    }}
                  />
                </div>
                <p style={{ fontSize: 11, color: "#888", margin: 0 }}>
                  {c.note_count} 篇笔记 · {c.total_occurrences} 次提及
                </p>
              </a>
            );
          })}
        </div>
      </section>
    </div>
  );
}

function pillStyle(active: boolean, color: string): React.CSSProperties {
  return {
    padding: "6px 14px",
    borderRadius: 20,
    border: active ? `2px solid ${color}` : "1px solid #ccc",
    background: active ? color : "#fff",
    color: active ? "#fff" : "#333",
    fontSize: 13,
    fontWeight: active ? 600 : 400,
    cursor: "pointer",
  };
}
