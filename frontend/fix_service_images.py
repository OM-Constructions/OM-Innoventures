#!/usr/bin/env python3
"""
1. Updates every service detail page to use its own unique image.
2. For services missing a unique image, copies the best matching fallback.
"""
import pathlib, re, shutil

BASE       = pathlib.Path('/home/dilli/OM construction-AI/frontend')
SERVICES   = BASE / 'services'
UNIQUE_DIR = BASE / 'assets/services/unique'
ASSETS     = BASE / 'assets/services'

# ── Fallback map for services that have no unique image yet ──
# Maps service-slug → best existing image (in assets/services/ OR unique/)
FALLBACK = {
    'ai-ml-solutions':       UNIQUE_DIR / 'ai-ml-custom-solution.jpg',
    'analytics':             UNIQUE_DIR / 'businessdata-analytics.jpg',
    'auditing-assurance':    UNIQUE_DIR / 'auditing.jpg',
    'cybersecurity':         ASSETS     / 'ai-ml-system.jpg',         # will copy as cyber
    'data-analytics-bi':     UNIQUE_DIR / 'businessdata-analytics.jpg',
    'data-science':          UNIQUE_DIR / 'python-data-analysis.jpg',
    'finance-accounting':    UNIQUE_DIR / 'accounting.jpg',
    'graphic-design':        ASSETS     / 'ai-ml-system.jpg',
    'product-development':   ASSETS     / 'saas-platform.jpg',
    'saas-ai-solutions':     ASSETS     / 'saas-platform.jpg',
    'software-development':  ASSETS     / 'business-website.jpg',
    'ui-ux-design':          ASSETS     / 'landing-page.jpg',
}

# Better fallbacks where possible (use real themed images)
BETTER = {
    'cybersecurity':         ASSETS / 'ai-ml-system.jpg',
    'graphic-design':        ASSETS / 'contact-forms.jpg',
}
FALLBACK.update(BETTER)

def ensure_unique_image(slug: str) -> str:
    """Return the correct ../../assets/services/unique/<slug>.jpg path,
       creating the file from a fallback if needed."""
    target = UNIQUE_DIR / f'{slug}.jpg'
    if target.exists():
        return f'../../assets/services/unique/{slug}.jpg'
    # copy fallback
    src = FALLBACK.get(slug)
    if src and src.exists():
        shutil.copy2(src, target)
        print(f'  COPIED fallback → {target.name}')
        return f'../../assets/services/unique/{slug}.jpg'
    # last resort: use generic
    print(f'  WARNING: no fallback for {slug}, using generic')
    return '../../assets/services/ai-ml-system.jpg'


IMG_RE = re.compile(
    r'(<img\b[^>]*?src=)["\']([^"\']+)["\']([^>]*?onerror=["\'][^"\']+["\'][^>]*?>)',
    re.DOTALL
)

def fix_page(html_path: pathlib.Path, slug: str):
    text = html_path.read_text(encoding='utf-8')
    correct_src = ensure_unique_image(slug)

    # Replace img src inside the service-hero-right div
    def replacer(m):
        return f'{m.group(1)}"{correct_src}"{m.group(3)}'

    new_text, n = IMG_RE.subn(replacer, text, count=1)  # only first img (hero)
    if n == 0:
        # Fallback: replace any ../../assets/services/... src
        new_text = re.sub(
            r'(src=")[^"]*assets/services/[^"]+(")',
            lambda m: f'{m.group(1)}{correct_src}{m.group(2)}',
            text, count=1
        )

    if new_text != text:
        html_path.write_text(new_text, encoding='utf-8')
        print(f'  FIXED: {slug:40} → {correct_src}')
    else:
        print(f'  SKIP (no change): {slug}')


def main():
    for service_dir in sorted(SERVICES.iterdir()):
        if not service_dir.is_dir():
            continue
        idx = service_dir / 'index.html'
        if not idx.exists():
            continue
        fix_page(idx, service_dir.name)
    print('\nDone.')


if __name__ == '__main__':
    main()
