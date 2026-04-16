# 部署指南

## 本地开发

```bash
cd web
npm install
npm run dev
```

访问 `http://localhost:3000`。本地开发使用符号链接 `public/pdfs` 和 `public/digests`。

## Vercel 部署

### 选项 A：Vercel 托管 web 子目录（推荐）

1. 把整个仓库推到 GitHub
2. 在 Vercel 新建项目，选择该仓库
3. **Root Directory** 设置为 `web`
4. 其他保持默认

构建时会自动运行 `npm run build`，其中 `prepare:public` 脚本会把 `digests/` 复制到 `web/public/digests/`。

### 选项 B：纯静态导出

如果想完全静态（如 GitHub Pages / Cloudflare Pages），修改 `next.config.mjs`：

```js
const nextConfig = {
  output: "export",
};
```

然后：

```bash
cd web
npm run build
# 产物在 web/out/
```

部署 `web/out/` 整个目录即可。

## PDF 图片说明

精读笔记引用的论文 figure 存放在 `pdfs/YYYY-MM-DD/*.mineru/hybrid_auto/images/`。

**默认行为**：`prepare:public` 脚本**不会**把 `pdfs/` 全部拷贝到 `public/`，因为它可能非常大（含大量 PDF 原文件）。本地开发通过符号链接访问。

**若需在生产环境展示笔记中的图片**，有三种方案：

1. **只拷贝 images 子目录**：修改 `scripts/prepare-public.mjs`，遍历 `pdfs/*/` 只拷贝 `*.mineru/hybrid_auto/images/` 子目录
2. **单独把 images 上传到 CDN**：用 Cloudflare R2 / S3，在前端改写图片 URL
3. **全量拷贝**（仅在内容量小时适用）：取消 `prepare-public.mjs` 中的 `// await syncResource("pdfs")` 注释

## 数据更新

数据从 SQLite 导出到 `web/public/generated/*.json`。更新数据：

```bash
# 根目录
python -c "from src.pipeline import CollectionPipeline; CollectionPipeline().export_all()"
# 然后 npm run build 或在 Vercel 触发重新部署
```

## 环境变量

当前不需要任何环境变量。所有数据都是构建时静态生成。
