#!/usr/bin/env python3
"""
Post-process the generated navbar.js file to unescape HTML entities.
This script should be run after Hugo builds the site.
"""

import html
from pathlib import Path

def fix_navbar_js():
    navbar_path = Path("public/navbar/navbar.js")

    if not navbar_path.exists():
        print(f"Error: {navbar_path} not found")
        return

    # Read the file
    content = navbar_path.read_text(encoding='utf-8')

    # Unescape HTML entities
    content = html.unescape(content)

    # Write back
    navbar_path.write_text(content, encoding='utf-8')
    print(f"Fixed HTML entities in {navbar_path}")

if __name__ == "__main__":
    fix_navbar_js()
