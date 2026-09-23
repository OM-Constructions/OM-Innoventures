#!/usr/bin/env python3
"""
Replaces the old stacked hero section in every service detail page
with the new split layout:  LEFT = text info  |  RIGHT = image
"""

import os, re, pathlib

SERVICES_DIR = pathlib.Path(__file__).parent / "services"

OLD_HERO_START = '<section class="service-page-hero"'
OLD_HERO_END   = '</section>'   # first closing tag after the hero open

def build_new_hero(title: str, desc: str, img_src: str) -> str:
    # Pick a short badge label from the title
    badge = f"⚡ Real System Architecture &bull; {title}"
    return f'''\
        <!-- HERO: Split Layout -->
        <section class="service-page-hero">
            <div class="container">
                <div class="service-hero-split gsap-reveal">

                    <!-- LEFT: text info -->
                    <div class="service-hero-left">
                        <span class="eyebrow">SERVICE DETAILS</span>
                        <h1>{title}</h1>
                        <p>{desc}</p>
                    </div>

                    <!-- RIGHT: image panel -->
                    <div class="service-hero-right">
                        <img
                            src="{img_src}"
                            alt="{title}"
                            onerror="this.src='../../assets/services/ai-ml-system.jpg'"
                        >
                        <div class="service-hero-img-caption">
                            <span class="caption-badge">{badge}</span>
                            <span class="caption-tag">OM Innoventures &bull; Verified Implementation</span>
                        </div>
                    </div>

                </div>
            </div>
        </section>'''


def extract_between(text, start_tag, end_tag):
    """Return (content_between, start_idx, end_idx) for the FIRST occurrence."""
    si = text.find(start_tag)
    if si == -1:
        return None, -1, -1
    # find the matching closing tag (skip nested same tags)
    depth = 0
    i = si
    tag_name = re.match(r'<(\w[\w-]*)', start_tag).group(1)
    open_re  = re.compile(rf'<{tag_name}[\s>]')
    close_re = re.compile(rf'</{tag_name}>')
    while i < len(text):
        om = open_re.search(text, i)
        cm = close_re.search(text, i)
        if om and (not cm or om.start() < cm.start()):
            depth += 1
            i = om.end()
        elif cm:
            depth -= 1
            i = cm.end()
            if depth == 0:
                return text[si:i], si, i
        else:
            break
    return None, -1, -1


def process_file(html_path: pathlib.Path):
    text = html_path.read_text(encoding='utf-8')

    # --- locate hero section ---
    hero_html, h_start, h_end = extract_between(text, '<section class="service-page-hero"', '</section>')
    if h_start == -1:
        # try variant with inline style
        hero_html, h_start, h_end = extract_between(
            text, '<section class="service-page-hero"', '</section>')
    if h_start == -1:
        print(f"  SKIP (no hero found): {html_path.name}")
        return

    # --- extract h1 title ---
    m = re.search(r'<h1[^>]*>(.*?)</h1>', hero_html, re.DOTALL)
    title = m.group(1).strip() if m else html_path.parent.name.upper().replace('-', ' ')

    # --- extract description <p> ---
    m = re.search(r'<p[^>]*>(.*?)</p>', hero_html, re.DOTALL)
    desc = m.group(1).strip() if m else "Innovative, data-driven, and perfectly scaled solutions designed around the core requirements and growth potential of your business."

    # --- extract image src ---
    m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', hero_html)
    img_src = m.group(1) if m else f"../../assets/services/unique/{html_path.parent.name}.jpg"

    new_hero = build_new_hero(title, desc, img_src)

    # --- replace old hero block in the full text ---
    # Indent level: the <section> in the file is typically inside <main>, 8 spaces
    new_text = text[:h_start] + new_hero + "\n" + text[h_end:]

    html_path.write_text(new_text, encoding='utf-8')
    print(f"  OK: {html_path.parent.name}")


def main():
    updated = 0
    for service_dir in sorted(SERVICES_DIR.iterdir()):
        if not service_dir.is_dir():
            continue
        idx = service_dir / "index.html"
        if not idx.exists():
            print(f"  NO index.html: {service_dir.name}")
            continue
        process_file(idx)
        updated += 1
    print(f"\nDone — updated {updated} service pages.")


if __name__ == "__main__":
    main()
