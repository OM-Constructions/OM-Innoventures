import os
import sys
from pathlib import Path

# Add backend to sys.path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from app.services.service_catalog import SERVICES

frontend_dir = backend_dir.parent / "frontend"
services_root = frontend_dir / "services"
services_root.mkdir(parents=True, exist_ok=True)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | OM Innoventures & Build AI Technologies</title>
    <meta name="description" content="{tagline} Expert {name} services by OM Innoventures & Build AI Technologies in Bengaluru.">

    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>

    <!-- NAV BAR -->
    <nav id="navbar">
        <div class="container nav-container">
            <a href="/" class="nav-brand">
                <span class="brand-om">OM</span>
                <span class="brand-long">INNOVENTURES</span>
                <span class="brand-sister">&amp; Build AI Technologies</span>
            </a>

            <div class="nav-menu" id="nav-menu">
                <div class="nav-links">
                    <a href="/" class="nav-link-item">Home</a>
                    <a href="/#services" class="nav-link-item active">Services</a>
                    <a href="/#capabilities" class="nav-link-item">Capabilities</a>
                    <a href="/#industries" class="nav-link-item">Industries</a>
                    <a href="/#work" class="nav-link-item">SaaS Demos</a>
                    <a href="/#about" class="nav-link-item">About</a>
                    <a href="/#cta" class="nav-link-item">Contact</a>
                </div>

                <div class="nav-actions">
                    <a href="https://om-buildings.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn-cross-link">
                        <span> Services</span>
                        <span>↗</span>
                    </a>

                    <span id="navAuthActions" class="nav-auth-group">
                        <a href="/login.html" class="nav-auth-link">Log In</a>
                        <a href="/signup.html" class="nav-auth-link">Sign Up</a>
                    </span>

                    <a href="/#cta?service={slug}" class="btn-primary">Enquire Now</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- SERVICE DETAIL HERO -->
    <header style="padding: 140px 0 70px; background-color: var(--navy-primary); color: #FFFFFF; border-bottom: 1px solid rgba(255,255,255,0.08);">
        <div class="container">
            <div style="margin-bottom: 16px;">
                <a href="/#services" style="color: var(--gold-accent); text-decoration: none; font-size: 0.9rem; font-weight: 600;">&larr; Back to All Disciplines</a>
            </div>
            <span class="eyebrow" style="color: var(--gold-accent);">{number} &bull; {category}</span>
            <h1 style="font-size: clamp(2.4rem, 4.5vw, 3.6rem); color: #FFFFFF; margin-bottom: 16px;">{name}</h1>
            <p style="font-size: 1.2rem; color: rgba(255, 255, 255, 0.85); max-width: 820px; line-height: 1.6; margin-bottom: 28px;">{tagline}</p>
            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                <a href="/#cta?service={slug}" class="btn-primary btn-gold">Request Project Proposal &rarr;</a>
                <a href="tel:8310160257" class="btn-outline">Speak with an Engineer: +91 83101 60257</a>
            </div>
        </div>
    </header>

    <!-- CONTENT SECTION -->
    <main class="section-gray">
        <div class="container" style="max-width: 960px;">
            <span class="eyebrow">OVERVIEW &amp; SPECIFICATION</span>
            <h2 class="section-title">Discipline Scope &amp; Architecture</h2>
            <p style="font-size: 1.12rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 44px;">
                {description}
            </p>

            <h3 style="font-size: 1.4rem; color: var(--navy-primary); margin-bottom: 20px;">Key Deliverables &amp; Outcomes</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; margin-bottom: 48px;">
                {deliverables_html}
            </div>

            <h3 style="font-size: 1.4rem; color: var(--navy-primary); margin-bottom: 16px;">Supported Tooling &amp; Stack</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 60px;">
                {technologies_html}
            </div>

            <!-- CTA BOX -->
            <div style="background: var(--navy-primary); color: #FFFFFF; border-radius: 12px; padding: 48px; text-align: center; box-shadow: var(--shadow-lg);">
                <span class="eyebrow" style="color: var(--gold-accent);">START YOUR BUILD</span>
                <h2 style="font-size: 2rem; color: #FFFFFF; margin-bottom: 12px;">Ready to Engineer Your {name} Solution?</h2>
                <p style="max-width: 620px; margin: 0 auto 28px; color: rgba(255, 255, 255, 0.8); line-height: 1.6;">
                    Our senior engineering team will evaluate your scope, design technical milestones, and build a reliable production system.
                </p>
                <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                    <a href="/#cta?service={slug}" class="btn-primary btn-gold">Initiate Project Consultation &rarr;</a>
                    <a href="mailto:ominnoventuresaitech@gmail.com" class="btn-outline">Email Project Brief</a>
                </div>
            </div>
        </div>
    </main>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-bottom" style="border-top: none; padding-top: 0;">
                <span>&copy; 2026 <strong>OM INNOVENTURES &amp; BUILD AI TECHNOLOGIES</strong>. All rights reserved.</span>
                <a href="https://om-buildings.vercel.app/" target="_blank" rel="noopener noreferrer" style="color: var(--gold-accent); text-decoration: none;">OM Innoventures & Build AI technologies ↗</a>
            </div>
        </div>
    </footer>

    <script src="/js/api.js"></script>
    <script src="/js/auth.js"></script>
    <script src="/js/main.js"></script>
</body>
</html>
"""

def generate_all_service_pages():
    for slug, svc in SERVICES.items():
        svc_dir = services_root / slug
        svc_dir.mkdir(parents=True, exist_ok=True)

        deliverables_html = "\n".join([
            f"""<div style="background: #FFFFFF; border: 1px solid var(--border-subtle); border-radius: 8px; padding: 20px; display: flex; align-items: flex-start; gap: 12px; box-shadow: var(--shadow-sm);">
                <span style="color: var(--gold-accent); font-weight: 800;">◆</span>
                <strong style="font-size: 0.95rem; color: var(--navy-primary);">{item}</strong>
            </div>"""
            for item in svc.get("deliverables", [])
        ])

        technologies_html = "\n".join([
            f"""<span style="background: #FFFFFF; border: 1px solid var(--border-subtle); color: var(--navy-primary); padding: 8px 16px; border-radius: 9999px; font-size: 0.86rem; font-weight: 600; box-shadow: var(--shadow-sm);">{tech}</span>"""
            for tech in svc.get("technologies", [])
        ])

        html_content = TEMPLATE.format(
            slug=slug,
            name=svc["name"],
            number=svc.get("number", "01"),
            category=svc.get("category", "AI & Technology"),
            tagline=svc.get("tagline", ""),
            description=svc.get("description", ""),
            deliverables_html=deliverables_html,
            technologies_html=technologies_html,
        )

        out_file = svc_dir / "index.html"
        out_file.write_text(html_content, encoding="utf-8")

    print("All 11 service detail pages successfully generated with updated theme!")

if __name__ == "__main__":
    generate_all_service_pages()
