---
name: paper-library
description: Convert research paper PDFs to mdbook format with Chinese interpretations. Use when adding papers to paper-pdf/, converting PDFs to readable format, or building the paper reading site.
---

# Paper Library Workflow

将论文 PDF 转换为 mdbook 格式的阅读站点，包含中文解读、图表、参考文献等。

## Quick Start

当用户添加新 PDF 到 `paper-pdf/` 目录时，执行以下工作流：

```
Task Progress:
- [ ] Step 0: 检查 meta.yaml 状态
- [ ] Step 1: 解析 PDF 提取元数据
- [ ] Step 2: 调用 paper-interpreter 生成解读
- [ ] Step 3: 更新 mdbook 结构
```

## Step 0: 检查转换状态

运行状态检查脚本：

```bash
python .cursor/skills/paper-library/scripts/check_meta.py paper-pdf/paper-name.pdf
```

**输出解释：**
- `pending` - 未转换，继续下一步
- `converted` - 已转换，询问用户是否强制重新生成
- `failed` - 上次失败，建议重新转换

如果已转换，询问用户：
> "该论文已转换过，是否需要强制重新生成？"

## Step 1: 解析 PDF 提取元数据

运行提取脚本：

```bash
python .cursor/skills/paper-library/scripts/extract_pdf.py paper-pdf/paper-name.pdf
```

**脚本功能：**
1. 创建 `materials/{paper-slug}/` 目录
2. 提取文本到 `text/full.txt` 和按页分割
3. 提取表格到 `tables/` (JSON 格式)
4. 提取图片到 `images/`
5. 生成 `metadata.json` 包含标题、作者等信息

**验证提取结果：**
```bash
ls materials/{paper-slug}/
```

确保包含：`metadata.json`, `text/`, `images/`, `tables/`

## Step 2: 调用 paper-interpreter 生成解读

使用 paper-interpreter subagent 分析论文：

1. 读取 `materials/{paper-slug}/metadata.json` 获取论文信息
2. 读取 `materials/{paper-slug}/text/full.txt` 获取全文
3. 查看 `materials/{paper-slug}/images/` 和 `tables/` 了解图表内容
4. 生成中文解读，包含：
   - 论文概述
   - 核心贡献
   - 方法论
   - 实验与结果
   - 图表解读
   - 参考文献
   - 原文摘录

## Step 3: 更新 mdbook 结构

运行 mdbook 更新脚本：

```bash
python .cursor/skills/paper-library/scripts/update_mdbook.py materials/{paper-slug}/
```

**脚本功能：**
1. 生成 `book/src/papers/{paper-slug}.md`
2. 更新 `book/src/SUMMARY.md` 添加论文条目
3. 复制图片到 `book/src/papers/images/`

**验证结果：**
```bash
cd book && mdbook build
```

## Step 4: 更新 meta.yaml

转换完成后更新状态：

```bash
python .cursor/skills/paper-library/scripts/check_meta.py paper-pdf/paper-name.pdf --set-status converted
```

## 目录结构

```
papers-library/
├── paper-pdf/           # 原始 PDF
├── materials/           # 提取的素材
│   └── {paper-slug}/
│       ├── metadata.json
│       ├── text/
│       ├── images/
│       └── tables/
├── meta.yaml            # 转换状态追踪
└── book/                # mdbook 输出
    ├── book.toml
    └── src/
        ├── SUMMARY.md
        └── papers/
```

## Utility Scripts

| 脚本 | 功能 |
|------|------|
| `scripts/check_meta.py` | 检查/更新 meta.yaml 状态 |
| `scripts/extract_pdf.py` | 提取 PDF 文本、图片、表格 |
| `scripts/update_mdbook.py` | 生成 mdbook markdown |

## Dependencies

确保已安装：
```bash
pip install pdfplumber pypdf PyYAML Pillow
```

## 相关资源

- PDF 处理详情见 [pdf skill](../pdf/SKILL.md)
- 论文解读由 paper-interpreter subagent 完成
