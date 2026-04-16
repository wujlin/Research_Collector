"use client";

import { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { MarkdownRender } from "../../../components/MarkdownRender";

function NoteContent() {
  const params = useSearchParams();
  const path = params.get("path");
  const [content, setContent] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    if (!path) return;
    setLoading(true);
    fetch(`/digests/${path}`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.text();
      })
      .then((text) => {
        // 移除 YAML frontmatter
        let cleaned = text;
        if (text.startsWith("---")) {
          const end = text.indexOf("---", 3);
          if (end > 0) cleaned = text.slice(end + 3).trim();
        }
        setContent(cleaned);
        setLoading(false);
      })
      .catch((e) => {
        setError(String(e));
        setLoading(false);
      });
  }, [path]);

  if (!path) return <p>未指定笔记路径。</p>;
  if (loading) return <p>Loading…</p>;
  if (error) return <p style={{ color: "crimson" }}>加载失败：{error}</p>;

  return (
    <div className="page">
      <a href="/notes" style={{ display: "inline-block", marginBottom: 16 }}>
        ← 返回笔记列表
      </a>
      <section className="card" style={{ padding: "24px 32px" }}>
        <MarkdownRender content={content} />
      </section>
    </div>
  );
}

export default function NoteViewPage() {
  return (
    <Suspense fallback={<p>Loading…</p>}>
      <NoteContent />
    </Suspense>
  );
}
