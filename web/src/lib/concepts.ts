export type ConceptOccurrence = {
  note_path: string;
  note_title: string;
  note_date: string;
  hit_count: number;
  snippets: string[];
};

export type Concept = {
  id: string;
  display_name: string;
  category: "equation" | "method" | "framework" | "tool" | "principle" | string;
  short_description: string;
  aliases: string[];
  total_occurrences: number;
  note_count: number;
  occurrences: ConceptOccurrence[];
};

export const CATEGORY_LABELS: Record<string, string> = {
  equation: "方程",
  method: "方法",
  framework: "框架",
  principle: "原理",
  tool: "工具",
};

export const CATEGORY_COLORS: Record<string, string> = {
  equation: "#e63946",
  method: "#fca311",
  framework: "#457b9d",
  principle: "#1d3557",
  tool: "#8ecae6",
};
