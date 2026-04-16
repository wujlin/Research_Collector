"use client";

import { useEffect, useState } from "react";
import type { GraphPayload } from "../../lib/generated";
import { NetworkGraph } from "../../components/NetworkGraph";

type ViewMode = "knowledge" | "authors" | "venues";

const VIEW_FILES: Record<ViewMode, string> = {
  knowledge: "graph",
  authors: "author_network",
  venues: "venue_network",
};

const VIEW_LABELS: Record<ViewMode, string> = {
  knowledge: "Knowledge Graph",
  authors: "Author Network",
  venues: "Venue Network",
};

export default function GraphPage() {
  const [view, setView] = useState<ViewMode>("knowledge");
  const [data, setData] = useState<GraphPayload | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetch(`/generated/${VIEW_FILES[view]}.json`)
      .then((res) => (res.ok ? res.json() : null))
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [view]);

  return (
    <section>
      <h2>Interactive Network Visualization</h2>
      <div style={{ display: "flex", gap: "8px", marginBottom: "16px" }}>
        {(Object.keys(VIEW_LABELS) as ViewMode[]).map((key) => (
          <button
            key={key}
            onClick={() => setView(key)}
            style={{
              padding: "8px 16px",
              borderRadius: "6px",
              border: view === key ? "2px solid #1d3557" : "1px solid #ccc",
              background: view === key ? "#a8dadc" : "#fff",
              fontWeight: view === key ? 600 : 400,
              cursor: "pointer",
            }}
          >
            {VIEW_LABELS[key]}
          </button>
        ))}
      </div>

      {data?.stats && (
        <p className="muted" style={{ marginBottom: "12px" }}>
          {Object.entries(data.stats)
            .map(([k, v]) => `${k}: ${v}`)
            .join(" · ")}
        </p>
      )}

      {loading && <p>Loading…</p>}
      {!loading && !data && <p>No graph data available.</p>}
      {!loading && data && <NetworkGraph data={data} viewMode={view} />}
    </section>
  );
}
