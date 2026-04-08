"use client";

import { useEffect, useMemo, useState } from "react";

import { SearchBar } from "../../components/SearchBar";
import type { YouTubeResource } from "../../lib/generated";
import { loadGenerated } from "../../lib/generated";

export default function YouTubePage() {
  const [resources, setResources] = useState<YouTubeResource[]>([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    loadGenerated<YouTubeResource[]>("youtube", []).then(setResources);
  }, []);

  const filtered = useMemo(() => {
    return resources
      .filter((resource) => {
      const text = `${resource.title} ${resource.channel_name} ${resource.topic_key}`.toLowerCase();
      return !query || text.includes(query.toLowerCase());
      })
      .sort((left, right) => right.importance_score - left.importance_score);
  }, [query, resources]);

  return (
    <div className="page">
      <section className="sectionHeader">
        <div>
          <h2>YouTube Learning Resources</h2>
          <p className="muted">Pulled from configured channels and playlists, sorted by importance.</p>
        </div>
        <SearchBar value={query} onChange={setQuery} placeholder="Filter channels or videos" />
      </section>

      <div className="grid">
        {filtered.map((resource) => (
          <article className="card" key={`${resource.video_id ?? resource.title}-${resource.id}`}>
            <h3>{resource.title}</h3>
            <p className="muted">
              {resource.channel_name}
              {resource.published_at ? ` • ${resource.published_at.slice(0, 10)}` : ""}
            </p>
            <p>{resource.description.slice(0, 220)}{resource.description.length > 220 ? "..." : ""}</p>
            <div className="topicList">
              <span className="pill">Importance {resource.importance_score.toFixed(1)}</span>
              <span className="pill">{resource.importance_bucket}</span>
              {resource.topic_key ? <span className="pill topicPill">{resource.topic_key}</span> : null}
              {resource.duration ? <span className="pill">{resource.duration}</span> : null}
              {resource.view_count ? <span className="pill">{resource.view_count.toLocaleString()} views</span> : null}
            </div>
            {resource.url ? (
              <a href={resource.url} target="_blank" rel="noreferrer">
                Open video
              </a>
            ) : null}
          </article>
        ))}
      </div>
    </div>
  );
}
