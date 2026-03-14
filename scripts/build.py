#!/usr/bin/env python3
"""
Build script for the 63-63 party website.
Reads Markdown content files and a template, generates index.html.
Also scans the pictures/ folder to generate the gallery.
"""

import os
import re
import glob

try:
    import markdown
except ImportError:
    print("ERROR: 'markdown' library not installed.")
    print("Run: pip install markdown")
    raise SystemExit(1)

# Paths (relative to project root)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'template.html')
OUTPUT_PATH = os.path.join(PROJECT_ROOT, 'index.html')
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')
PICTURES_DIR = os.path.join(PROJECT_ROOT, 'pictures')

# Mapping: placeholder name -> (language, filename)
CONTENT_MAP = {
    'hero_it': ('it', 'hero.md'),
    'hero_en': ('en', 'hero.md'),
    'storia_it': ('it', 'storia.md'),
    'storia_en': ('en', 'story.md'),
    'giovanni_it': ('it', 'giovanni.md'),
    'giovanni_en': ('en', 'giovanni.md'),
    'enrico_it': ('it', 'enrico.md'),
    'enrico_en': ('en', 'enrico.md'),
    'stefano_it': ('it', 'stefano.md'),
    'stefano_en': ('en', 'stefano.md'),
    'gigio_it': ('it', 'gigio.md'),
    'gigio_en': ('en', 'gigio.md'),
    'spettro_it': ('it', 'spettro-politico.md'),
    'spettro_en': ('en', 'political-spectrum.md'),
    'luogo_it': ('it', 'luogo.md'),
    'luogo_en': ('en', 'venue.md'),
    'dove_dormire_it': ('it', 'dove-dormire.md'),
    'dove_dormire_en': ('en', 'where-to-stay.md'),
    'tomba_brion_it': ('it', 'tomba-brion.md'),
    'tomba_brion_en': ('en', 'brion-tomb.md'),
    'rsvp_it': ('it', 'rsvp.md'),
    'rsvp_en': ('en', 'rsvp.md'),
}

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}


def read_file(path):
    """Read a file and return its contents."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def md_to_html(md_text):
    """Convert Markdown to HTML."""
    return markdown.markdown(md_text, extensions=['extra'])


def scan_gallery_images():
    """Scan the pictures/ folder for images and generate gallery HTML."""
    images = []
    for root, dirs, files in os.walk(PICTURES_DIR):
        # Skip the profiles and landscape subfolders for gallery
        rel_root = os.path.relpath(root, PROJECT_ROOT)
        if 'profiles' in rel_root or 'landscape' in rel_root or 'tomba-brion' in rel_root:
            continue
        for filename in sorted(files):
            ext = os.path.splitext(filename)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                rel_path = os.path.relpath(os.path.join(root, filename), PROJECT_ROOT)
                images.append(rel_path)

    if not images:
        return '<p>No photos yet.</p>'

    html_parts = []
    for img_path in images:
        alt_text = os.path.splitext(os.path.basename(img_path))[0].replace('-', ' ').replace('_', ' ')
        html_parts.append(
            f'            <div class="gallery-item">\n'
            f'                <img src="{img_path}" alt="{alt_text}" loading="lazy">\n'
            f'            </div>'
        )
    return '\n'.join(html_parts)


def build():
    """Main build function."""
    print("Building 63-63 website...")

    # Read template
    if not os.path.exists(TEMPLATE_PATH):
        print(f"ERROR: Template not found at {TEMPLATE_PATH}")
        raise SystemExit(1)

    template = read_file(TEMPLATE_PATH)

    # Process content files
    replacements = {}
    for placeholder, (lang, filename) in CONTENT_MAP.items():
        filepath = os.path.join(CONTENT_DIR, lang, filename)
        if not os.path.exists(filepath):
            print(f"WARNING: Content file not found: {filepath}")
            replacements[placeholder] = f'<p>[Missing content: {lang}/{filename}]</p>'
        else:
            md_content = read_file(filepath)
            replacements[placeholder] = md_to_html(md_content)

    # Generate gallery
    replacements['gallery_images'] = scan_gallery_images()

    # Apply replacements
    output = template
    for placeholder, html_content in replacements.items():
        output = output.replace('{{' + placeholder + '}}', html_content)

    # Check for unreplaced placeholders
    remaining = re.findall(r'\{\{(\w+)\}\}', output)
    if remaining:
        print(f"WARNING: Unreplaced placeholders: {remaining}")

    # Write output
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Generated: {OUTPUT_PATH}")
    print(f"Gallery images found: {len(re.findall(r'gallery-item', output))}")


if __name__ == '__main__':
    build()
