"use client";

import type { DigestEntry } from "../lib/generated";

type DigestViewProps = {
  digests: DigestEntry[];
};

export function DigestView({ digests }: DigestViewProps) {
  if (!digests.length) {
    return <p className="muted">No digests exported yet.</p>;
  }

  return (
    <div className="grid">
      {digests.map((digest) => (
        <article className="card" key={digest.path}>
          <h3>{digest.title}</h3>
          <p className="muted">{digest.created_at}</p>
          <p>{digest.path}</p>
        </article>
      ))}
    </div>
  );
}
