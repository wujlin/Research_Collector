"use client";

import { useEffect, useState } from "react";

import { TopicTree } from "../../components/TopicTree";
import type { Topic } from "../../lib/generated";
import { loadGenerated } from "../../lib/generated";

export default function TopicsPage() {
  const [topics, setTopics] = useState<Topic[]>([]);

  useEffect(() => {
    loadGenerated<Topic[]>("topics", []).then(setTopics);
  }, []);

  return (
    <div className="page">
      <section className="card">
        <p className="eyebrow">Taxonomy</p>
        <h2>Topic Landscape</h2>
        <p>
          The taxonomy is intentionally not siloed. Top-level groups play different roles in one
          chain: mathematical backbone, thermodynamic semantics, AI for Physics machinery,
          application arena, and explicit bridge mechanisms such as Fokker-Planck, free energy,
          stochastic thermodynamics, and optimal transport. Inside AI for Physics, score/diffusion
          is now treated as one branch of generative dynamics rather than a peer of statistical
          physics.
        </p>
      </section>
      <TopicTree topics={topics} />
    </div>
  );
}
