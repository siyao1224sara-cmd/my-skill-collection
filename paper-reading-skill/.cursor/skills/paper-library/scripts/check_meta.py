#!/usr/bin/env python3
"""
Check and update paper conversion status in meta.yaml.

Usage:
    python check_meta.py paper-pdf/paper.pdf              # Check status
    python check_meta.py paper-pdf/paper.pdf --set-status converted
    python check_meta.py --list                           # List all papers
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

import yaml


def get_project_root() -> Path:
    """Get project root directory."""
    return Path(__file__).parent.parent.parent.parent.parent


def get_paper_slug(pdf_path: str) -> str:
    """Convert PDF path to paper slug."""
    return Path(pdf_path).stem


def load_meta(meta_path: Path) -> dict:
    """Load meta.yaml, create if not exists."""
    if not meta_path.exists():
        return {"papers": {}}
    
    with open(meta_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data if data else {"papers": {}}


def save_meta(meta_path: Path, data: dict) -> None:
    """Save meta.yaml."""
    with open(meta_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def check_status(pdf_path: str) -> dict:
    """Check conversion status for a PDF."""
    root = get_project_root()
    meta_path = root / "meta.yaml"
    meta = load_meta(meta_path)
    
    slug = get_paper_slug(pdf_path)
    
    if slug not in meta.get("papers", {}):
        # Add new entry with pending status
        if "papers" not in meta:
            meta["papers"] = {}
        meta["papers"][slug] = {
            "status": "pending",
            "source": pdf_path,
            "title": "",
            "converted_at": None,
            "materials_path": f"materials/{slug}/",
            "mdbook_path": f"book/src/papers/{slug}.md"
        }
        save_meta(meta_path, meta)
        return {"slug": slug, "status": "pending", "is_new": True}
    
    paper_info = meta["papers"][slug]
    return {
        "slug": slug,
        "status": paper_info.get("status", "pending"),
        "title": paper_info.get("title", ""),
        "converted_at": paper_info.get("converted_at"),
        "is_new": False
    }


def set_status(pdf_path: str, status: str, title: str = None) -> dict:
    """Set conversion status for a PDF."""
    root = get_project_root()
    meta_path = root / "meta.yaml"
    meta = load_meta(meta_path)
    
    slug = get_paper_slug(pdf_path)
    
    if "papers" not in meta:
        meta["papers"] = {}
    
    if slug not in meta["papers"]:
        meta["papers"][slug] = {
            "source": pdf_path,
            "materials_path": f"materials/{slug}/",
            "mdbook_path": f"book/src/papers/{slug}.md"
        }
    
    meta["papers"][slug]["status"] = status
    
    if title:
        meta["papers"][slug]["title"] = title
    
    if status == "converted":
        meta["papers"][slug]["converted_at"] = datetime.now().isoformat()
    
    save_meta(meta_path, meta)
    
    return {"slug": slug, "status": status, "updated": True}


def list_papers() -> list:
    """List all papers and their status."""
    root = get_project_root()
    meta_path = root / "meta.yaml"
    meta = load_meta(meta_path)
    
    papers = []
    for slug, info in meta.get("papers", {}).items():
        papers.append({
            "slug": slug,
            "status": info.get("status", "unknown"),
            "title": info.get("title", ""),
            "source": info.get("source", "")
        })
    
    return papers


def main():
    parser = argparse.ArgumentParser(description="Check/update paper conversion status")
    parser.add_argument("pdf_path", nargs="?", help="Path to PDF file")
    parser.add_argument("--set-status", choices=["pending", "converting", "converted", "failed"],
                        help="Set status for the paper")
    parser.add_argument("--set-title", help="Set title for the paper")
    parser.add_argument("--list", action="store_true", help="List all papers")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    if args.list:
        papers = list_papers()
        if args.json:
            import json
            print(json.dumps(papers, indent=2, ensure_ascii=False))
        else:
            if not papers:
                print("No papers found in meta.yaml")
            else:
                print(f"{'Slug':<40} {'Status':<12} {'Title'}")
                print("-" * 80)
                for p in papers:
                    print(f"{p['slug']:<40} {p['status']:<12} {p['title'][:30]}")
        return
    
    if not args.pdf_path:
        parser.print_help()
        sys.exit(1)
    
    if args.set_status:
        result = set_status(args.pdf_path, args.set_status, args.set_title)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"Updated {result['slug']}: status = {result['status']}")
    else:
        result = check_status(args.pdf_path)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            status_msg = "NEW - " if result.get("is_new") else ""
            print(f"{status_msg}{result['slug']}: {result['status']}")
            if result.get("title"):
                print(f"  Title: {result['title']}")
            if result.get("converted_at"):
                print(f"  Converted: {result['converted_at']}")


if __name__ == "__main__":
    main()
