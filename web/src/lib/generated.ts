export type Paper = {
  id: number;
  title: string;
  abstract: string;
  authors: string[];
  year: number | null;
  publication_date: string;
  journal: string;
  venue: string;
  doi: string | null;
  arxiv_id: string | null;
  url: string;
  pdf_url: string;
  citation_count: number;
  influential_citation_count: number;
  relevance_score: number;
  tier: number;
  venue_quality: string;
  status: string;
  is_seminal: boolean;
  source: string;
  topics: string[];
  markdown_path: string;
  importance_score: number;
  importance_bucket: string;
};

export type Topic = {
  key: string;
  display_name: string;
  parent_key: string | null;
  description: string;
  paper_count: number;
  depth: number;
  is_leaf: boolean;
  lineage: string[];
};

export type YouTubeResource = {
  id: number;
  title: string;
  channel_name: string;
  channel_id: string;
  video_id: string | null;
  playlist_id: string | null;
  url: string;
  description: string;
  published_at: string;
  duration: string;
  view_count: number;
  topic_key: string;
  resource_type: string;
  importance_score: number;
  importance_bucket: string;
};

export type DigestEntry = {
  title: string;
  path: string;
  created_at: string;
};

export type Author = {
  id: number;
  name: string;
  affiliation: string;
  openalex_id: string;
  h_index: number;
  paper_count: number;
  topic_keys: string[];
};

export type GraphNode = {
  id: string;
  label: string;
  type: "topic" | "paper" | "author" | "venue";
  parent_key?: string | null;
  depth?: number;
  is_leaf?: boolean;
  relevance_score?: number;
  citation_count?: number;
  year?: number;
  tier?: number;
  affiliation?: string;
  h_index?: number;
  paper_count?: number;
  reputation?: string;
  venue?: string;
  weight?: number;
};

export type GraphEdge = {
  source: string;
  target: string;
  type: string;
  weight?: number;
};

export type GraphPayload = {
  nodes: GraphNode[];
  edges: GraphEdge[];
  stats?: Record<string, number>;
};

export type Stats = {
  total_papers: number;
  by_status: Record<string, number>;
  by_topic: Record<string, number>;
};

export async function loadGenerated<T>(fileName: string, fallback: T): Promise<T> {
  try {
    const response = await fetch(`/generated/${fileName}.json`, {
      cache: "no-store",
    });
    if (!response.ok) {
      return fallback;
    }
    return (await response.json()) as T;
  } catch {
    return fallback;
  }
}
