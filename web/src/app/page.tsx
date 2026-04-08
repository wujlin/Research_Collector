"use client";

import { useEffect, useState } from "react";

import { KnowledgeGraph } from "../components/KnowledgeGraph";
import { PaperCard } from "../components/PaperCard";
import type { GraphPayload, Paper, Stats } from "../lib/generated";
import { loadGenerated } from "../lib/generated";

export default function HomePage() {
  const [graph, setGraph] = useState<GraphPayload>({ nodes: [], edges: [] });
  const [papers, setPapers] = useState<Paper[]>([]);
  const [stats, setStats] = useState<Stats>({
    total_papers: 0,
    by_status: {},
    by_topic: {},
  });

  useEffect(() => {
    loadGenerated<GraphPayload>("graph", { nodes: [], edges: [] }).then(setGraph);
    loadGenerated<Paper[]>("papers", []).then((items) => setPapers(items.slice(0, 6)));
    loadGenerated<Stats>("stats", { total_papers: 0, by_status: {}, by_topic: {} }).then(setStats);
  }, []);

  return (
    <div className="page">
      <section className="hero card">
        <p className="eyebrow">Knowledge Topology</p>
        <h2>Track one continuous research program, not four isolated topics.</h2>
        <p>
          This project treats stochastic analysis as the mathematical spine, Fokker-Planck and
          master equations as the translation layer, statistical physics as the thermodynamic
          semantics, AI for Physics as the computational machinery, and urban systems as the
          application arena. Inside AI for Physics, the hierarchy now separates generative
          dynamics from physics-informed modeling, so score/diffusion sits under that computation
          layer instead of beside statistical physics. The current frontier is the bridge between
          non-equilibrium statistical physics and generative modeling.
        </p>
        <div className="statsGrid">
          <div>
            <strong>{stats.total_papers}</strong>
            <span>Total papers</span>
          </div>
          {Object.entries(stats.by_status).map(([status, count]) => (
            <div key={status}>
              <strong>{count}</strong>
              <span>{status}</span>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2>Knowledge Graph</h2>
        <KnowledgeGraph graph={graph} />
      </section>

      <section>
        <div className="sectionHeader">
          <h2>High-Priority Papers</h2>
          <a href="/library">Open full library</a>
        </div>
        <div className="grid">
          {papers.map((paper) => (
            <PaperCard key={paper.id} paper={paper} />
          ))}
        </div>
      </section>
    </div>
  );
}
