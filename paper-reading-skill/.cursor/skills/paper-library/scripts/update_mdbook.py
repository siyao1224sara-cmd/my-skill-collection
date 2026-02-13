#!/usr/bin/env python3
"""
Generate mdbook markdown from extracted materials and update SUMMARY.md.

Usage:
    python update_mdbook.py materials/paper-slug/
    python update_mdbook.py materials/paper-slug/ --content content.md
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent.parent.parent


def load_metadata(materials_dir: Path) -> dict:
    metadata_file = materials_dir / "metadata.json"
    if not metadata_file.exists():
        raise FileNotFoundError(f"metadata.json not found in {materials_dir}")
    with open(metadata_file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_paper_markdown(materials_dir: Path, content_file: Path = None) -> str:
    metadata = load_metadata(materials_dir)
    slug = metadata.get("slug", materials_dir.name)
    title = metadata.get("metadata", {}).get("title", slug)
    
    md_lines = [f"# {title or slug}", ""]
    
    md_lines.append("## 论文信息")
    md_lines.append("")
    
    paper_meta = metadata.get("metadata", {})
    if paper_meta.get("author"):
        md_lines.append(f"- **作者**: {paper_meta['author']}")
    if paper_meta.get("page_count"):
        md_lines.append(f"- **页数**: {paper_meta['page_count']}")
    if paper_meta.get("source_file"):
        md_lines.append(f"- **源文件**: {paper_meta['source_file']}")
    md_lines.append("")
    
    if content_file and content_file.exists():
        with open(content_file, "r", encoding="utf-8") as f:
            content = f.read()
        md_lines.append(content)
        md_lines.append("")
    else:
        md_lines.extend([
            "## 论文概述", "",
            "<!-- paper-interpreter 将在此生成论文概述 -->", "",
            "## 核心贡献", "",
            "<!-- paper-interpreter 将在此生成核心贡献 -->", "",
            "## 方法论", "",
            "<!-- paper-interpreter 将在此生成方法论 -->", "",
            "## 实验与结果", "",
            "<!-- paper-interpreter 将在此生成实验与结果 -->", "",
        ])
    
    images_info = metadata.get("images", {})
    if images_info.get("image_count", 0) > 0:
        md_lines.extend(["## 图表", ""])
        for img in images_info.get("images", [])[:10]:
            img_name = img.get("filename", "")
            md_lines.append(f"![{img_name}](images/{slug}/{img_name})")
            md_lines.append("")
    
    tables_info = metadata.get("tables", {})
    if tables_info.get("table_count", 0) > 0:
        md_lines.extend(["## 表格", ""])
        for table in tables_info.get("tables", [])[:5]:
            table_id = table.get("id", "")
            md_lines.append(f"### {table_id}")
            md_lines.append(f"*Page {table.get('page', '?')}, {table.get('rows', '?')} rows*")
            md_lines.append("")
    
    md_lines.extend(["## 参考文献", "", "<!-- paper-interpreter 将在此生成重要参考文献 -->", ""])
    
    return "\n".join(md_lines)


def update_summary(book_dir: Path, slug: str, title: str) -> None:
    summary_file = book_dir / "src" / "SUMMARY.md"
    
    if not summary_file.exists():
        summary_content = "# Summary\n\n- [首页](README.md)\n- [论文列表](papers/README.md)\n"
    else:
        with open(summary_file, "r", encoding="utf-8") as f:
            summary_content = f.read()
    
    paper_link = f"papers/{slug}.md"
    if paper_link in summary_content:
        print(f"  Paper already in SUMMARY.md: {slug}")
        return
    
    paper_entry = f"  - [{title or slug}]({paper_link})"
    
    pattern = r"(\- \[论文列表\]\(papers/README\.md\))"
    if re.search(pattern, summary_content):
        summary_content = re.sub(pattern, f"\\1\n{paper_entry}", summary_content)
    else:
        summary_content = summary_content.rstrip() + f"\n{paper_entry}\n"
    
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary_content)
    
    print(f"  Updated SUMMARY.md with: {title or slug}")


def copy_images(materials_dir: Path, book_dir: Path, slug: str) -> int:
    src_images = materials_dir / "images"
    dst_images = book_dir / "src" / "papers" / "images" / slug
    
    if not src_images.exists():
        return 0
    
    dst_images.mkdir(parents=True, exist_ok=True)
    
    copied = 0
    for img_file in src_images.glob("*.*"):
        if img_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            shutil.copy2(img_file, dst_images / img_file.name)
            copied += 1
    
    return copied


def update_mdbook(materials_dir: str, content_file: str = None) -> dict:
    materials_path = Path(materials_dir)
    root = get_project_root()
    
    if not materials_path.is_absolute():
        materials_path = root / materials_path
    
    if not materials_path.exists():
        raise FileNotFoundError(f"Materials not found: {materials_path}")
    
    metadata = load_metadata(materials_path)
    slug = metadata.get("slug", materials_path.name)
    title = metadata.get("metadata", {}).get("title", slug)
    
    book_dir = root / "book"
    papers_dir = book_dir / "src" / "papers"
    papers_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Updating mdbook for: {slug}")
    
    content_path = Path(content_file) if content_file else None
    if content_path and not content_path.is_absolute():
        content_path = root / content_path
    
    markdown = generate_paper_markdown(materials_path, content_path)
    
    paper_file = papers_dir / f"{slug}.md"
    with open(paper_file, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"  Created: {paper_file}")
    
    copied_images = copy_images(materials_path, book_dir, slug)
    if copied_images:
        print(f"  Copied {copied_images} images")
    
    update_summary(book_dir, slug, title)
    
    return {"slug": slug, "paper_file": str(paper_file), "images_copied": copied_images}


def main():
    parser = argparse.ArgumentParser(description="Update mdbook with paper")
    parser.add_argument("materials_dir", help="Path to materials directory")
    parser.add_argument("--content", "-c", help="Path to content markdown")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        result = update_mdbook(args.materials_dir, args.content)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("\nUpdate complete!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
