"use client";

import { useEffect, useState } from "react";

import { DigestView } from "../../components/DigestView";
import type { DigestEntry } from "../../lib/generated";
import { loadGenerated } from "../../lib/generated";

export default function DigestsPage() {
  const [digests, setDigests] = useState<DigestEntry[]>([]);

  useEffect(() => {
    loadGenerated<DigestEntry[]>("digests", []).then(setDigests);
  }, []);

  return (
    <div className="page">
      <section className="card">
        <p className="eyebrow">Research Rhythm</p>
        <h2>Digests</h2>
        <p>Weekly and monthly summary artifacts generated from the current database snapshot.</p>
      </section>
      <DigestView digests={digests} />
    </div>
  );
}
