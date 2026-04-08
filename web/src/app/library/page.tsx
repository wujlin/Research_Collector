"use client";

import { useEffect, useMemo, useState } from "react";

import { PaperCard } from "../../components/PaperCard";
import { SearchBar } from "../../components/SearchBar";
import type { Paper, Topic } from "../../lib/generated";
import { loadGenerated } from "../../lib/generated";

export default function LibraryPage() {
  const [papers, setPapers] = useState<Paper[]>([]);
  const [topics, setTopics] = useState<Topic[]>([]);
  const [query, setQuery] = useState("");
  const [selectedTopic, setSelectedTopic] = useState("");

  useEffect(() => {
    loadGenerated<Paper[]>("papers", []).then(setPapers);
    loadGenerated<Topic[]>("topics", []).then(setTopics);
  }, []);

  const filtered = useMemo(() => {
    return papers
      .filter((paper) => {
        const haystack = `${paper.title} ${paper.abstract} ${paper.authors.join(" ")} ${paper.topics.join(" ")}`.toLowerCase();
        const queryOk = !query || haystack.includes(query.toLowerCase());
        const topicOk = !selectedTopic || paper.topics.includes(selectedTopic);
        return queryOk && topicOk;
      })
      .sort((left, right) => right.importance_score - left.importance_score);
  }, [papers, query, selectedTopic]);

  const selectableTopics = useMemo(() => {
    return topics
      .filter((topic) => topic.is_leaf)
      .sort((left, right) => left.key.localeCompare(right.key));
  }, [topics]);

  return (
    <div className="page">
      <section className="sectionHeader">
        <div>
          <h2>Library</h2>
          <p className="muted">Browse the exported paper catalog.</p>
        </div>
        <div className="filterBar">
          <SearchBar value={query} onChange={setQuery} />
          <label className="searchBar">
            <span>Topic</span>
            <select value={selectedTopic} onChange={(event) => setSelectedTopic(event.target.value)}>
              <option value="">All topics</option>
              {selectableTopics.map((topic) => (
                <option key={topic.key} value={topic.key}>
                  {topic.lineage.join(" / ")}
                </option>
              ))}
            </select>
          </label>
        </div>
      </section>

      <div className="grid">
        {filtered.map((paper) => (
          <PaperCard key={paper.id} paper={paper} />
        ))}
      </div>
    </div>
  );
}
