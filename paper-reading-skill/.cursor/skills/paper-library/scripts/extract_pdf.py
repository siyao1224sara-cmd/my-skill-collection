#!/usr/bin/env python3
"""
Extract text, images, and tables from PDF to materials directory.

Usage:
    python extract_pdf.py paper-pdf/paper.pdf
    python extract_pdf.py paper-pdf/paper.pdf --output materials/custom-name/
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import pdfplumber
from pypdf import PdfReader


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent.parent.parent


def get_paper_slug(pdf_path: str) -> str:
    return Path(pdf_path).stem


def extract_metadata(pdf_path: Path) -> dict:
    reader = PdfReader(pdf_path)
    meta = reader.metadata
    return {
        "title": meta.title if meta and meta.title else "",
        "author": meta.author if meta and meta.author else "",
        "subject": meta.subject if meta and meta.subject else "",
        "page_count": len(reader.pages),
        "source_file": str(pdf_path.name)
    }


def extract_text(pdf_path: Path, output_dir: Path) -> dict:
    text_dir = output_dir / "text"
    text_dir.mkdir(parents=True, exist_ok=True)
    
    full_text = []
    page_texts = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            page_texts.append(text)
            full_text.append(f"--- Page {i + 1} ---\n{text}")
            
            page_file = text_dir / f"page_{i + 1:03d}.txt"
            with open(page_file, "w", encoding="utf-8") as f:
                f.write(text)
    
    full_file = text_dir / "full.txt"
    with open(full_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(full_text))
    
    return {
        "page_count": len(page_texts),
        "total_chars": sum(len(t) for t in page_texts),
        "output_dir": str(text_dir)
    }


def extract_tables(pdf_path: Path, output_dir: Path) -> dict:
    tables_dir = output_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    
    table_count = 0
    tables_info = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for table_idx, table in enumerate(tables):
                if not table or len(table) < 2:
                    continue
                
                table_count += 1
                table_id = f"page{page_num + 1}_table{table_idx + 1}"
                
                table_file = tables_dir / f"{table_id}.json"
                with open(table_file, "w", encoding="utf-8") as f:
                    json.dump({
                        "page": page_num + 1,
                        "table_index": table_idx + 1,
                        "headers": table[0] if table else [],
                        "rows": table[1:] if len(table) > 1 else [],
                        "row_count": len(table) - 1 if table else 0
                    }, f, ensure_ascii=False, indent=2)
                
                tables_info.append({
                    "id": table_id,
                    "page": page_num + 1,
                    "rows": len(table) - 1
                })
    
    index_file = tables_dir / "index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(tables_info, f, ensure_ascii=False, indent=2)
    
    return {"table_count": table_count, "tables": tables_info}


def extract_images(pdf_path: Path, output_dir: Path) -> dict:
    images_dir = output_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        prefix = images_dir / "img"
        subprocess.run(
            ["pdfimages", "-j", "-p", str(pdf_path), str(prefix)],
            capture_output=True, check=False
        )
    except FileNotFoundError:
        try:
            import pypdfium2 as pdfium
            pdf = pdfium.PdfDocument(pdf_path)
            for i, page in enumerate(pdf):
                bitmap = page.render(scale=2.0)
                img = bitmap.to_pil()
                img.save(images_dir / f"page_{i + 1:03d}.png", "PNG")
        except ImportError:
            pass
    
    image_files = [f for f in images_dir.glob("*.*") 
                   if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".ppm"]]
    
    images_info = [{"filename": f.name} for f in sorted(image_files)]
    
    index_file = images_dir / "index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(images_info, f, ensure_ascii=False, indent=2)
    
    return {"image_count": len(image_files), "images": images_info}


def extract_pdf(pdf_path: str, output_dir: str = None) -> dict:
    pdf_path = Path(pdf_path)
    root = get_project_root()
    
    if not pdf_path.is_absolute():
        pdf_path = root / pdf_path
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    slug = get_paper_slug(str(pdf_path))
    
    if output_dir:
        out_path = Path(output_dir)
        if not out_path.is_absolute():
            out_path = root / out_path
    else:
        out_path = root / "materials" / slug
    
    out_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting: {pdf_path.name}")
    print(f"Output: {out_path}")
    
    print("  - Extracting metadata...")
    metadata = extract_metadata(pdf_path)
    
    print("  - Extracting text...")
    text_info = extract_text(pdf_path, out_path)
    
    print("  - Extracting tables...")
    tables_info = extract_tables(pdf_path, out_path)
    
    print("  - Extracting images...")
    images_info = extract_images(pdf_path, out_path)
    
    result = {
        "slug": slug,
        "source": str(pdf_path),
        "output_dir": str(out_path),
        "metadata": metadata,
        "text": text_info,
        "tables": tables_info,
        "images": images_info
    }
    
    metadata_file = out_path / "metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\nExtraction complete!")
    print(f"  Pages: {metadata['page_count']}")
    print(f"  Text chars: {text_info['total_chars']}")
    print(f"  Tables: {tables_info['table_count']}")
    print(f"  Images: {images_info['image_count']}")
    
    return result


def main():
    parser = argparse.ArgumentParser(description="Extract content from PDF")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Output directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        result = extract_pdf(args.pdf_path, args.output)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
