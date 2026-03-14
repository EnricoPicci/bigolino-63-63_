#!/usr/bin/env python3
"""
Test script for the 63-63 party website.
Validates the generated index.html for structure, content, and images.
Run: python3 scripts/test.py
"""

import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(PROJECT_ROOT, 'index.html')
PICTURES_DIR = os.path.join(PROJECT_ROOT, 'pictures')

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}

passed = 0
failed = 0
warnings = 0


def check(description, condition, warn_only=False):
    """Check a condition and report pass/fail."""
    global passed, failed, warnings
    if condition:
        passed += 1
        print(f"  PASS: {description}")
    elif warn_only:
        warnings += 1
        print(f"  WARN: {description}")
    else:
        failed += 1
        print(f"  FAIL: {description}")


def run_tests():
    global passed, failed, warnings

    print("Testing 63-63 website...\n")

    # ---- File existence ----
    print("[Files]")
    check("index.html exists", os.path.exists(INDEX_PATH))
    check("template.html exists", os.path.exists(os.path.join(PROJECT_ROOT, 'template.html')))
    check("css/style.css exists", os.path.exists(os.path.join(PROJECT_ROOT, 'css', 'style.css')))
    check("js/main.js exists", os.path.exists(os.path.join(PROJECT_ROOT, 'js', 'main.js')))

    if not os.path.exists(INDEX_PATH):
        print("\nCannot continue without index.html. Run 'python3 scripts/build.py' first.")
        return False

    html = open(INDEX_PATH, 'r', encoding='utf-8').read()

    # ---- Required sections ----
    print("\n[Required Sections]")
    sections = {
        'hero': 'id="hero"',
        'rsvp': 'id="rsvp"',
        'storia': 'id="storia"',
        'fab-four': 'id="fab-four"',
        'spettro': 'id="spettro"',
        'luogo': 'id="luogo"',
        'gallery': 'id="gallery"',
        'dove-dormire': 'id="dove-dormire"',
        'footer': 'class="site-footer"',
    }
    for name, marker in sections.items():
        check(f"Section '{name}' present", marker in html)

    # ---- Bilingual content ----
    print("\n[Bilingual Content]")
    check("Italian content blocks present", 'class="content-it"' in html)
    check("English content blocks present", 'class="content-en"' in html)
    check("Language toggle present", 'class="lang-toggle"' in html)

    # Key Italian phrases
    check("Italian hero text present", '63-63' in html)
    check("Italian story section has content", 'Liceo' in html or 'Tito Livio' in html)

    # Key English phrases
    check("English story content present", 'Friendship' in html or 'friendship' in html)

    # ---- Profile content ----
    print("\n[Profiles]")
    profiles = ['Giovanni Della Frattina', 'Enrico Piccinin', 'Stefano Visentin', 'Luigi']
    for name in profiles:
        check(f"Profile '{name}' present", name in html)

    # ---- Images ----
    print("\n[Images]")
    # Extract all image src attributes
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    gallery_imgs = re.findall(r'gallery-item.*?<img[^>]+src=["\']([^"\']+)["\']', html, re.DOTALL)

    check("At least one gallery image", len(gallery_imgs) > 0)

    # Verify gallery images exist on disk
    for src in gallery_imgs:
        full_path = os.path.join(PROJECT_ROOT, src)
        check(f"Gallery image exists: {src}", os.path.exists(full_path))

    # Profile images (warn only - they may not exist yet)
    profile_imgs = [s for s in img_srcs if 'profiles/' in s]
    for src in profile_imgs:
        full_path = os.path.join(PROJECT_ROOT, src)
        check(f"Profile image exists: {src}", os.path.exists(full_path), warn_only=True)

    # ---- Landscape images ----
    landscape_dir = os.path.join(PICTURES_DIR, 'landscape')
    if os.path.exists(landscape_dir):
        landscape_count = len([f for f in os.listdir(landscape_dir)
                              if os.path.splitext(f)[1].lower() in IMAGE_EXTENSIONS])
        check(f"Landscape images present ({landscape_count} found)", landscape_count > 0)

    # ---- Tomba Brion page ----
    print("\n[Tomba Brion Page]")
    check("Main content wrapper present", 'id="main-content"' in html)
    check("Tomba Brion page div present", 'id="tomba-brion-page"' in html)
    check("Back navigation present", 'class="back-nav"' in html)
    check("Tomba Brion CTA button present", 'btn-tomba-brion' in html)
    check("Carlo Scarpa mentioned", 'Carlo Scarpa' in html)

    # ---- Footer ----
    print("\n[Footer]")
    check("Powered by badge present", 'Daniela and Dario Amodei' in html)
    check("AI Prosecco tagline present", 'Prosecco' in html.split('site-footer')[-1] if 'site-footer' in html else False)
    check("Image credits present", 'CC BY-SA' in html or 'Wikimedia' in html)

    # ---- HTML validity (basic) ----
    print("\n[HTML Structure]")
    check("DOCTYPE present", '<!DOCTYPE html>' in html)
    check("Charset defined", 'charset="UTF-8"' in html or 'charset=UTF-8' in html)
    check("Viewport meta present", 'viewport' in html)
    check("CSS linked", 'style.css' in html)
    check("JS linked", 'main.js' in html)

    # ---- Content files ----
    print("\n[Content Files]")
    content_dir = os.path.join(PROJECT_ROOT, 'content')
    for lang in ['it', 'en']:
        lang_dir = os.path.join(content_dir, lang)
        if os.path.exists(lang_dir):
            md_files = [f for f in os.listdir(lang_dir) if f.endswith('.md')]
            check(f"Content files for '{lang}' ({len(md_files)} found)", len(md_files) >= 9)
        else:
            check(f"Content directory '{lang}' exists", False)

    # ---- No unreplaced placeholders ----
    print("\n[Build Quality]")
    placeholders = re.findall(r'\{\{(\w+)\}\}', html)
    check("No unreplaced placeholders", len(placeholders) == 0)
    if placeholders:
        print(f"    Found: {placeholders}")

    # ---- Summary ----
    print(f"\n{'=' * 40}")
    print(f"Results: {passed} passed, {failed} failed, {warnings} warnings")
    print(f"{'=' * 40}")

    return failed == 0


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
