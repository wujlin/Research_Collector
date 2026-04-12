# WSA MinerU PDF Workflow

本项目当前约定把本地 PDF 送到 WSA 上的 MinerU 做解析，再把输出回传到本地 PDF 同级目录。

## 前置条件

```bash
export WSA_SSH_PASSWORD='...'
```

WSA 侧默认使用：

- 项目目录：`/home/jinlin/projects/Research_Collector`
- Conda 环境：`dpl`
- MinerU API 端口：`18000`

## 启动或校验 WSA 上的 MinerU API

先确保代码已经同步到 WSA，然后在 WSA 上运行：

```bash
cd /home/jinlin/projects/Research_Collector
bash scripts/wsa_ensure_mineru_api.sh
```

## 从本地触发 PDF 提取并回传

针对单个 PDF：

```bash
python scripts/extract_pdfs_via_wsa.py pdfs/2026-04-11/foo.pdf --force
```

针对一个目录递归处理：

```bash
python scripts/extract_pdfs_via_wsa.py pdfs/2026-04-11 --force
```

回传后的输出目录会直接落在源 PDF 同级目录，命名为 `<pdf_stem>.mineru/`。

例如：

- 输入：`pdfs/2026-04-11/foo.pdf`
- 输出：`pdfs/2026-04-11/foo.mineru/`

输出目录里会包含 MinerU 生成的 `hybrid_auto/*.md`、`*_content_list.json`、`*_layout.pdf` 等结果文件。
