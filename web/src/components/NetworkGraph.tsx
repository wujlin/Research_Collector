"use client";

import { useMemo, Suspense } from "react";
import dynamic from "next/dynamic";
import type { GraphPayload, GraphNode, GraphEdge } from "../lib/generated";

const GraphCanvas = dynamic(
  () => import("reagraph").then((mod) => mod.GraphCanvas),
  { ssr: false },
);

type Props = {
  data: GraphPayload;
  viewMode: string;
};

const TYPE_COLORS: Record<string, string> = {
  topic: "#a8dadc",
  paper: "#f1faee",
  author: "#fca311",
  venue: "#e76f51",
};

const EDGE_COLORS: Record<string, string> = {
  taxonomy: "rgba(29, 53, 87, 0.15)",
  belongs_to: "rgba(168, 218, 220, 0.3)",
  authored: "rgba(252, 163, 17, 0.25)",
  coauthor: "rgba(252, 163, 17, 0.4)",
  published_in: "rgba(231, 111, 81, 0.3)",
};

function nodeSize(node: GraphNode): number {
  if (node.type === "topic") return node.is_leaf ? 3 : 5;
  if (node.type === "author") return Math.min(2 + (node.paper_count ?? 1) * 0.8, 8);
  if (node.type === "venue") return Math.min(3 + (node.paper_count ?? 1) * 0.5, 10);
  return 2;
}

function nodeLabel(node: GraphNode, viewMode: string): string {
  if (viewMode === "authors" && node.affiliation) {
    return `${node.label}\n${node.affiliation}`;
  }
  if (viewMode === "venues" && node.tier !== undefined) {
    return `${node.label} (T${node.tier})`;
  }
  return node.label;
}

export function NetworkGraph({ data, viewMode }: Props) {
  const reagraphNodes = useMemo(
    () =>
      data.nodes.map((n) => ({
        id: n.id,
        label: nodeLabel(n, viewMode),
        fill: TYPE_COLORS[n.type] ?? "#ddd",
        size: nodeSize(n),
      })),
    [data.nodes, viewMode],
  );

  const reagraphEdges = useMemo(
    () =>
      data.edges.map((e, i) => ({
        id: `${e.source}-${e.target}-${i}`,
        source: e.source,
        target: e.target,
        fill: EDGE_COLORS[e.type] ?? "rgba(0,0,0,0.1)",
        size: e.weight ? Math.min(1 + e.weight * 0.3, 4) : 1,
      })),
    [data.edges],
  );

  return (
    <div style={{ height: "70vh", width: "100%", border: "1px solid #eee", borderRadius: "8px" }}>
      <Suspense fallback={<p>Loading graph…</p>}>
        <GraphCanvas
          nodes={reagraphNodes}
          edges={reagraphEdges}
          layoutType="forceDirected2d"
          labelType="auto"
          draggable
          animated={false}
        />
      </Suspense>
    </div>
  );
}
