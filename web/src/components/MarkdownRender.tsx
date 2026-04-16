"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";

type Props = {
  content: string;
  imageBasePath?: string;
};

/**
 * 渲染精读笔记的 Markdown 内容。
 * - 支持 GFM（表格、任务列表等）
 * - 支持 KaTeX 数学公式（$...$ 与 $$...$$）
 * - 相对图片路径自动解析到正确位置
 */
export function MarkdownRender({ content, imageBasePath = "" }: Props) {
  return (
    <article className="markdown-body">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeKatex]}
        components={{
          img: ({ src, alt }) => {
            let resolved = src ?? "";
            // 笔记中使用 ../../pdfs/... 的相对路径，需要把 ../.. 替换到 public 根路径
            if (resolved.startsWith("../../")) {
              resolved = "/" + resolved.slice("../../".length);
            } else if (imageBasePath && !resolved.startsWith("http") && !resolved.startsWith("/")) {
              resolved = `${imageBasePath}/${resolved}`;
            }
            return (
              <img
                src={resolved}
                alt={alt ?? ""}
                style={{ maxWidth: "100%", borderRadius: 8, margin: "16px 0" }}
              />
            );
          },
          a: ({ href, children }) => (
            <a href={href} target="_blank" rel="noopener noreferrer">
              {children}
            </a>
          ),
          table: ({ children }) => (
            <div style={{ overflowX: "auto" }}>
              <table>{children}</table>
            </div>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </article>
  );
}
