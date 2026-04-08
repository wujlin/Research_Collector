"use client";

import type { GraphNode, GraphPayload } from "../lib/generated";

type KnowledgeGraphProps = {
  graph: GraphPayload;
};

type PositionedNode = {
  id: string;
  label: string;
  type: "topic" | "paper";
  x: number;
  y: number;
};

const TOPIC_X_STEP = 150;
const TOPIC_Y_STEP = 115;
const PAPER_Y_GAP = 150;
const PAPER_X_STEP = 110;

export function KnowledgeGraph({ graph }: KnowledgeGraphProps) {
  const topicNodes = graph.nodes.filter((node) => node.type === "topic");
  const visiblePaperNodes = graph.nodes.filter((node) => node.type === "paper").slice(0, 12);
  const topicLookup = new Map(topicNodes.map((node) => [node.id, node]));
  const childrenByParent = new Map<string, GraphNode[]>();
  const positioned: Record<string, PositionedNode> = {};
  const paperAnchors = new Map<string, string>();
  let nextLeafX = 120;
  let maxTopicDepth = 0;

  topicNodes.forEach((node) => {
    if (!node.parent_key) {
      return;
    }
    const siblings = childrenByParent.get(node.parent_key) ?? [];
    siblings.push(node);
    childrenByParent.set(node.parent_key, siblings);
  });

  childrenByParent.forEach((children) => {
    children.sort((left, right) => left.id.localeCompare(right.id));
  });

  const roots = topicNodes
    .filter((node) => !node.parent_key)
    .sort((left, right) => left.id.localeCompare(right.id));

  const layoutTopicNode = (node: GraphNode, depth: number): number => {
    maxTopicDepth = Math.max(maxTopicDepth, depth);
    const children = childrenByParent.get(node.id) ?? [];
    const childXs = children.map((child) => layoutTopicNode(child, depth + 1));
    const x = childXs.length
      ? childXs.reduce((sum, value) => sum + value, 0) / childXs.length
      : nextLeafX;

    if (!childXs.length) {
      nextLeafX += TOPIC_X_STEP;
    }

    positioned[node.id] = {
      id: node.id,
      label: node.label,
      type: "topic",
      x,
      y: 80 + depth * TOPIC_Y_STEP,
    };
    return x;
  };

  roots.forEach((root) => {
    layoutTopicNode(root, 0);
    nextLeafX += 60;
  });

  graph.edges
    .filter((edge) => edge.type === "belongs_to")
    .forEach((edge) => {
      if (!topicLookup.has(edge.target)) {
        return;
      }
      const current = paperAnchors.get(edge.source);
      const currentDepth = current ? (topicLookup.get(current)?.depth ?? 0) : -1;
      const nextDepth = topicLookup.get(edge.target)?.depth ?? 0;
      if (!current || nextDepth >= currentDepth) {
        paperAnchors.set(edge.source, edge.target);
      }
    });

  const papersByAnchor = new Map<string, GraphNode[]>();
  visiblePaperNodes.forEach((node) => {
    const anchor = paperAnchors.get(node.id);
    if (!anchor || !positioned[anchor]) {
      return;
    }
    const papers = papersByAnchor.get(anchor) ?? [];
    papers.push(node);
    papersByAnchor.set(anchor, papers);
  });

  papersByAnchor.forEach((papers, anchor) => {
    papers.forEach((paperNode, index) => {
      const anchorPosition = positioned[anchor];
      const column = index % 3;
      const row = Math.floor(index / 3);
      positioned[paperNode.id] = {
        id: paperNode.id,
        label: paperNode.label,
        type: "paper",
        x: anchorPosition.x + (column - 1) * PAPER_X_STEP,
        y: anchorPosition.y + PAPER_Y_GAP + row * 90,
      };
    });
  });

  const unanchoredPapers = visiblePaperNodes.filter((node) => !positioned[node.id]);
  unanchoredPapers.forEach((node, index) => {
    positioned[node.id] = {
      id: node.id,
      label: node.label,
      type: "paper",
      x: 120 + (index % 4) * 180,
      y: 120 + (maxTopicDepth + 1) * TOPIC_Y_STEP + Math.floor(index / 4) * 90,
    };
  });

  const visibleNodeIds = new Set(Object.keys(positioned));
  const edges = graph.edges.filter(
    (edge) => visibleNodeIds.has(edge.source) && visibleNodeIds.has(edge.target),
  );
  const width = Math.max(960, nextLeafX + 160);
  const height = Math.max(720, 180 + (maxTopicDepth + 1) * TOPIC_Y_STEP + 320);

  return (
    <div className="graphShell card">
      <svg viewBox={`0 0 ${width} ${height}`} className="graph">
        {edges.map((edge, index) => {
          const source = positioned[edge.source];
          const target = positioned[edge.target];
          if (!source || !target) {
            return null;
          }
          return (
            <line
              key={`${edge.source}-${edge.target}-${index}`}
              x1={source.x}
              y1={source.y}
              x2={target.x}
              y2={target.y}
              stroke={edge.type === "taxonomy" ? "rgba(29, 53, 87, 0.22)" : "rgba(214, 122, 92, 0.28)"}
              strokeWidth={edge.type === "taxonomy" ? 1.4 : 1.6}
            />
          );
        })}
        {Object.values(positioned).map((node) => (
          <g key={node.id} transform={`translate(${node.x}, ${node.y})`}>
            <circle
              r={node.type === "paper" ? 18 : 24}
              fill={node.type === "paper" ? "#f1faee" : "#a8dadc"}
              stroke="#1d3557"
              strokeWidth={2}
            />
            <text
              textAnchor="middle"
              y={node.type === "paper" ? 34 : 40}
              className="graphLabel"
            >
              {truncate(node.label, node.type === "paper" ? 24 : 20)}
            </text>
          </g>
        ))}
      </svg>
      <p className="muted">
        The upper rows show the recursive topic hierarchy. Papers are pinned below the deepest
        visible topic they belong to, so bridge papers tend to sit between multiple layers.
      </p>
    </div>
  );
}

function truncate(value: string, length: number): string {
  return value.length > length ? `${value.slice(0, length - 1)}…` : value;
}
