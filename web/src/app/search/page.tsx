"use client";

import { useEffect, useMemo, useState } from "react";

import { PaperCard } from "../../components/PaperCard";
import { SearchBar } from "../../components/SearchBar";
import type { Paper } from "../../lib/generated";
import { loadGenerated } from "../../lib/generated";

export default function SearchPage() {
  const [papers, setPapers] = useState<Paper[]>([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    loadGenerated<Paper[]>("papers", []).then(setPapers);
  }, []);

  const filtered = useMemo(() => {
    const trimmed = query.trim().toLowerCase();
    if (!trimmed) {
      return papers.slice(0, 12);
    }
    return papers
      .filter((paper) => {
        const text = `${paper.title} ${paper.abstract} ${paper.authors.join(" ")} ${paper.topics.join(" ")}`.toLowerCase();
        return text.includes(trimmed);
      })
      .sort((left, right) => right.importance_score - left.importance_score);
  }, [papers, query]);

  return (
    <div className="page">
      <section className="card">
        <h2>Search</h2>
        <SearchBar value={query} onChange={setQuery} placeholder="Search the exported paper snapshot" />
      </section>
      <div className="grid">
        {filtered.map((paper) => (
          <PaperCard key={paper.id} paper={paper} />
        ))}
      </div>
    </div>
  );
}
