"use client";

import type { Paper } from "../lib/generated";

type PaperCardProps = {
  paper: Paper;
};

export function PaperCard({ paper }: PaperCardProps) {
  return (
    <article className="card paperCard">
      <div className="paperMeta">
        <span className="pill">{paper.source || "source"}</span>
        <span className="pill">Tier {paper.tier || 0}</span>
        <span className="pill">{paper.venue_quality || "unranked"}</span>
        <span className="pill">Importance {paper.importance_score.toFixed(1)}</span>
        <span className="pill">Score {paper.relevance_score.toFixed(1)}</span>
        <span className="pill">{paper.importance_bucket}</span>
      </div>
      <h3>{paper.title}</h3>
      <p className="muted">
        {paper.authors.slice(0, 4).join(", ") || "Unknown authors"}
        {paper.year ? ` • ${paper.year}` : ""}
        {paper.journal ? ` • ${paper.journal}` : paper.venue ? ` • ${paper.venue}` : ""}
      </p>
      <p>{paper.abstract ? `${paper.abstract.slice(0, 240)}${paper.abstract.length > 240 ? "..." : ""}` : "No abstract available."}</p>
      <div className="topicList">
        {paper.topics.slice(0, 4).map((topic) => (
          <span className="pill topicPill" key={topic}>
            {topic}
          </span>
        ))}
      </div>
      <div className="paperLinks">
        {paper.url ? (
          <a href={paper.url} target="_blank" rel="noreferrer">
            Source
          </a>
        ) : null}
        {paper.pdf_url ? (
          <a href={paper.pdf_url} target="_blank" rel="noreferrer">
            PDF
          </a>
        ) : null}
        {paper.markdown_path ? <span className="muted">{paper.markdown_path}</span> : null}
      </div>
    </article>
  );
}
