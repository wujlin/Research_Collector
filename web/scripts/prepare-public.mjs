#!/usr/bin/env node
/**
 * 构建前准备脚本：
 * 1. 删除 public/pdfs 和 public/digests（如果是符号链接或目录）
 * 2. 从仓库根复制 pdfs/ 和 digests/ 到 public/
 *
 * 符号链接在本地 dev 环境可用，但 Vercel 等静态托管可能不跟随。
 * 本脚本确保部署时这些资源作为真实文件存在于 public/ 下。
 */
import { cp, rm, stat } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const webRoot = resolve(here, "..");
const repoRoot = resolve(webRoot, "..");

async function exists(p) {
  try {
    await stat(p);
    return true;
  } catch {
    return false;
  }
}

async function syncResource(name) {
  const src = resolve(repoRoot, name);
  const dst = resolve(webRoot, "public", name);
  if (!(await exists(src))) {
    console.warn(`[prepare-public] skip: ${src} not found`);
    return;
  }
  if (await exists(dst)) {
    await rm(dst, { recursive: true, force: true });
  }
  console.log(`[prepare-public] copying ${src} -> ${dst}`);
  await cp(src, dst, { recursive: true, dereference: true });
}

async function main() {
  const mode = process.argv[2] ?? "copy";
  if (mode === "copy") {
    await syncResource("digests");
    // 注意：pdfs 可能非常大，默认仍保留符号链接
    // 如果要部署到 Vercel，可以改成真实复制：
    // await syncResource("pdfs");
    console.log("[prepare-public] done (digests copied). pdfs stays as symlink for dev.");
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
