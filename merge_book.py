#!/usr/bin/env python3
"""
Script to merge scattered PDF chapters into complete book(s).

This script combines individual chapter PDF files from the 
"Linear Algebra Made Easy - Learn with Python and Visualization" book
into complete, continuously readable PDF files.

Output files:
- 线性代数_上册.pdf: Upper volume (Chapters 1-7) with preface
- 线性代数_下册.pdf: Lower volume (Chapters 8-15) with preface  
- 线性代数_完整版.pdf: Full book with both prefaces and all chapters

Usage:
    python merge_book.py
"""

import os
import re
import glob
from PyPDF2 import PdfMerger


def get_chapter_number(filename):
    """Extract chapter number from filename for sorting."""
    # Pattern: LA_XX_YY_topic.pdf where XX is chapter, YY is section
    match = re.match(r'LA_(\d+)_(\d+)', filename)
    if match:
        chapter = int(match.group(1))
        section = int(match.group(2))
        return (chapter, section)
    return (0, 0)


def get_content_pdfs(directory):
    """Get all content PDF files (chapters 1-15), sorted by chapter and section."""
    pattern = os.path.join(directory, 'LA_[0-9][0-9]_[0-9][0-9]_*.pdf')
    pdf_files = glob.glob(pattern)
    
    # Filter out chapter 00 (prefaces)
    content_files = [f for f in pdf_files if not os.path.basename(f).startswith('LA_00_')]
    
    # Sort by chapter and section number
    content_files.sort(key=lambda x: get_chapter_number(os.path.basename(x)))
    
    return content_files


def get_upper_volume_chapters(all_chapters):
    """Get chapters 1-7 for upper volume."""
    return [f for f in all_chapters if 1 <= get_chapter_number(os.path.basename(f))[0] <= 7]


def get_lower_volume_chapters(all_chapters):
    """Get chapters 8-15 for lower volume."""
    return [f for f in all_chapters if 8 <= get_chapter_number(os.path.basename(f))[0] <= 15]


def merge_pdfs(pdf_files, output_path):
    """Merge a list of PDF files into a single PDF."""
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        print(f"  Adding: {os.path.basename(pdf_file)}")
        merger.append(pdf_file)
    
    merger.write(output_path)
    merger.close()
    print(f"Created: {output_path}")


def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define preface files
    upper_preface = os.path.join(script_dir, 'LA_00_上册_正文前_V2.pdf')
    lower_preface = os.path.join(script_dir, 'LA_00_下册_正文前_V2.pdf')
    
    # Get all content chapters
    all_chapters = get_content_pdfs(script_dir)
    
    if not all_chapters:
        print("Error: No chapter PDF files found!")
        return
    
    print(f"Found {len(all_chapters)} chapter PDF files\n")
    
    # Get chapter groups
    upper_chapters = get_upper_volume_chapters(all_chapters)
    lower_chapters = get_lower_volume_chapters(all_chapters)
    
    print(f"Upper volume (Chapters 1-7): {len(upper_chapters)} files")
    print(f"Lower volume (Chapters 8-15): {len(lower_chapters)} files\n")
    
    # Define output directory for merged books
    output_dir = os.path.join(script_dir, 'merged_books')
    os.makedirs(output_dir, exist_ok=True)
    
    # Create Upper Volume (上册)
    print("=" * 60)
    print("Creating Upper Volume (上册) - Chapters 1-7")
    print("=" * 60)
    upper_volume_files = []
    if os.path.exists(upper_preface):
        upper_volume_files.append(upper_preface)
    upper_volume_files.extend(upper_chapters)
    
    upper_output = os.path.join(output_dir, '线性代数_上册.pdf')
    merge_pdfs(upper_volume_files, upper_output)
    print()
    
    # Create Lower Volume (下册)
    print("=" * 60)
    print("Creating Lower Volume (下册) - Chapters 8-15")
    print("=" * 60)
    lower_volume_files = []
    if os.path.exists(lower_preface):
        lower_volume_files.append(lower_preface)
    lower_volume_files.extend(lower_chapters)
    
    lower_output = os.path.join(output_dir, '线性代数_下册.pdf')
    merge_pdfs(lower_volume_files, lower_output)
    print()
    
    # Create Full Book (完整版)
    print("=" * 60)
    print("Creating Full Book (完整版) - All Chapters")
    print("=" * 60)
    full_book_files = []
    if os.path.exists(upper_preface):
        full_book_files.append(upper_preface)
    full_book_files.extend(upper_chapters)
    if os.path.exists(lower_preface):
        full_book_files.append(lower_preface)
    full_book_files.extend(lower_chapters)
    
    full_output = os.path.join(output_dir, '线性代数_完整版.pdf')
    merge_pdfs(full_book_files, full_output)
    print()
    
    # Print summary
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Upper Volume: {upper_output}")
    print(f"Lower Volume: {lower_output}")
    print(f"Full Book: {full_output}")
    print("\nBook compilation complete!")


if __name__ == '__main__':
    main()
