"use client";

import { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { loadGenerated } from "../../../lib/generated";
import { CATEGORY_COLORS, CATEGORY_LABELS, type Concept } from "../../../lib/concepts";

function ConceptContent() {
  const params = useSearchParams();
  const id = params.get("id");
  const [concept, setConcept] = useState<Concept | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) return;
    loadGenerated<Concept[]>("concepts", []).then((all) => {
      setConcept(all.find((c) => c.id === id) ?? null);
      setLoading(false);
    });
  }, [id]);

  if (!id) return <p>未指定概念 ID。</p>;
  if (loading) return <p>Loading…</p>;
  if (!concept) return <p>未找到该概念。</p>;

  return (
    <div className="page">
      <a href="/concepts" style={{ display: "inline-block", marginBottom: 16 }}>
        ← 返回概念列表
      </a>

      <section className="card">
        <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
          <span
            style={{
              fontSize: 11,
              padding: "3px 10px",
              borderRadius: 12,
              background: CATEGORY_COLORS[concept.category] ?? "#666",
              color: "#fff",
              fontWeight: 600,
            }}
          >
            {CATEGORY_LABELS[concept.category] ?? concept.category}
          </span>
          <span className="muted" style={{ fontSize: 12 }}>
            {concept.note_count} 篇笔记 · {concept.total_occurrences} 次提及
          </span>
        </div>
        <h1 style={{ fontSize: 26, margin: "4px 0 8px" }}>{concept.display_name}</h1>
        <p style={{ fontSize: 15, color: "#444", margin: "0 0 12px" }}>{concept.short_description}</p>
        <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
          {concept.aliases.map((a) => (
            <span
              key={a}
              style={{
                fontSize: 11,
                padding: "3px 8px",
                borderRadius: 4,
                background: "#f1faee",
                border: "1px solid #a8dadc",
                color: "#1d3557",
                fontFamily: "monospace",
              }}
            >
              {a}
            </span>
          ))}
        </div>
      </section>

      <section>
        <h2 style={{ fontSize: 18, marginBottom: 12 }}>在笔记中的出现</h2>
        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          {concept.occurrences.map((occ) => (
            <div key={occ.note_path} className="card">
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
                <a
                  href={`/notes/view?path=${encodeURIComponent(occ.note_path)}`}
                  style={{ textDecoration: "none", color: "#1d3557", fontWeight: 600, fontSize: 15 }}
                >
                  {occ.note_title}
                </a>
                <span className="muted" style={{ fontSize: 12 }}>
                  {occ.note_date} · {occ.hit_count} 次
                </span>
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                {occ.snippets.map((s, i) => (
                  <blockquote
                    key={i}
                    style={{
                      margin: 0,
                      padding: "8px 14px",
                      borderLeft: `3px solid ${CATEGORY_COLORS[concept.category] ?? "#999"}`,
                      background: "#fafafa",
                      fontSize: 13,
                      lineHeight: 1.55,
                      color: "#333",
                      fontStyle: "normal",
                    }}
                  >
                    …{highlight(s, concept.aliases)}…
                  </blockquote>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

function highlight(text: string, aliases: string[]): React.ReactNode {
  const escaped = aliases.map((a) => a.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
  const pattern = new RegExp(`(${escaped.join("|")})`, "gi");
  const parts = text.split(pattern);
  return parts.map((p, i) =>
    escaped.some((a) => new RegExp(`^${a}$`, "i").test(p)) ? (
      <mark key={i} style={{ background: "#fff3b0", padding: "0 2px" }}>
        {p}
      </mark>
    ) : (
      <span key={i}>{p}</span>
    ),
  );
}

export default function ConceptViewPage() {
  return (
    <Suspense fallback={<p>Loading…</p>}>
      <ConceptContent />
    </Suspense>
  );
}
