import os
import json

services = [
    {"slug": "data-analytics-bi", "name": "Data Analytics & BI", "tagline": "Uncover hidden insights within your data.", "price": "Starting ₹14,999", "img": "service_ml.jpg"},
    {"slug": "data-science", "name": "Data Science", "tagline": "Advanced statistical modeling and algorithms.", "price": "Starting ₹24,999", "img": "service_ml.jpg"},
    {"slug": "ai-ml-solutions", "name": "AI / ML Solutions", "tagline": "Intelligent machine learning pipelines.", "price": "Starting ₹49,999", "img": "service_ml.jpg"},
    {"slug": "software-development", "name": "Software Development", "tagline": "Custom enterprise-grade web applications.", "price": "Starting ₹99,999", "img": "service_vision.jpg"},
    {"slug": "product-development", "name": "Product Development", "tagline": "End-to-end digital product lifecycle management.", "price": "Starting ₹1,49,999", "img": "service_vision.jpg"},
    {"slug": "ui-ux-design", "name": "UI / UX Design", "tagline": "Intuitive, engaging user experiences.", "price": "Starting ₹29,999", "img": "service_vision.jpg"},
    {"slug": "graphic-design", "name": "Graphic Design", "tagline": "Stunning visuals and brand identity.", "price": "Starting ₹9,999", "img": "service_vision.jpg"},
    {"slug": "finance-accounting", "name": "Finance & Accounting Services", "tagline": "Precise financial management and bookkeeping.", "price": "Starting ₹19,999", "img": "service_analytics.jpg"},
    {"slug": "auditing-assurance", "name": "Auditing & Assurance Services", "tagline": "Rigorous compliance and internal controls.", "price": "Starting ₹39,999", "img": "service_analytics.jpg"},
    {"slug": "cybersecurity", "name": "Cybersecurity Services", "tagline": "Robust protection for your digital assets.", "price": "Starting ₹49,999", "img": "service_analytics.jpg"},
    {"slug": "saas-ai-solutions", "name": "SaaS & AI Powered Solutions", "tagline": "Scalable platforms infused with AI.", "price": "Starting ₹1,99,999", "img": "service_ml.jpg"}
]

base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | OM Innoventures</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../style.css?v=11">
    
    <script type="importmap">
        {{
            "imports": {{
                "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
                "gsap": "https://unpkg.com/gsap@3.12.2/index.js",
                "gsap/ScrollTrigger": "https://unpkg.com/gsap@3.12.2/ScrollTrigger.js"
            }}
        }}
    </script>
</head>
<body>

    <!-- NAV BAR -->
    <nav id="navbar" class="scrolled">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span class="brand-om">OM</span><span class="brand-long">Innoventures</span>
            </a>
            <div class="nav-links">
                <a href="../../index.html#hero" class="nav-link-item">Home</a>
                <a href="../../index.html#services" class="nav-link-item">Services</a>
            </div>
            <div class="nav-actions">
                <span id="nav-auth-container" class="nav-auth-group">
                    <a href="../../login.html" class="nav-auth-link nav-auth-login">Log In</a>
                    <a href="../../signup.html" class="nav-auth-link nav-auth-signup">Sign Up</a>
                </span>
                <a href="../../index.html#cta" class="btn-primary">Let's Talk</a>
            </div>
            <button class="hamburger">☰</button>
        </div>
    </nav>

    <main class="service-page-main">
        <!-- HERO -->
        <section class="service-page-hero">
            <div class="container gsap-reveal">
                <span class="eyebrow">SERVICE DETAILS</span>
                <h1>{title}</h1>
                <p>{tagline}</p>
                <div class="service-hero-accent"></div>
            </div>
        </section>

        <!-- 01 OVERVIEW -->
        <section class="sp-section sp-overview">
            <div class="container gsap-reveal">
                <span class="sp-label">01 &mdash; OVERVIEW</span>
                <p>At OM Innoventures, our {title} services are built to solve your unique challenges. We provide a full-spectrum solution tailored to your operational constraints, driving real value through advanced technical methodologies.</p>
            </div>
        </section>

        <!-- 02 WHAT WE FOCUS ON -->
        <section class="sp-section sp-section-gray">
            <div class="container gsap-reveal">
                <span class="sp-label" style="color: var(--navy-primary);">02 &mdash; WHAT WE FOCUS ON</span>
                <h2 class="sp-title">Capabilities & Deliverables</h2>
                <div class="sp-focus-grid">
                    <div class="sp-focus-item">
                        <h3>Strategy & Implementation</h3>
                        <p>Defining the optimal path forward and seamlessly deploying the solution.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Custom Development</h3>
                        <p>Building exactly what you need without relying on rigid, off-the-shelf constraints.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Quality Assurance</h3>
                        <p>Rigorous testing and continuous oversight to guarantee performance.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Ongoing Support</h3>
                        <p>Long-term maintenance and scaling capabilities as your business grows.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- PRICING SECTION -->
        <section class="sp-section" style="text-align: center;">
            <div class="container gsap-reveal">
                <span class="sp-label">INVESTMENT</span>
                <h2 class="sp-title" style="margin-bottom: 20px;">Estimated Pricing</h2>
                <div style="font-size: 2.5rem; color: var(--gold-accent); font-weight: 700; font-family: 'Exo 2', sans-serif;">
                    {price}
                </div>
                <p style="margin-top: 15px; max-width: 600px; margin-left: auto; margin-right: auto; opacity: 0.8;">Note: Exact pricing may vary depending on project complexity, scope, and specific client requirements.</p>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>OM INNOVENTURES</h3>
                    <p>&amp; AI TECHNOLOGIES</p>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 OM Innoventures. All rights reserved.</span>
            </div>
        </div>
    </footer>

    <script type="module" src="../../src/main.js"></script>
</body>
</html>
"""

base_dir = "/home/dilli/OM -AI/frontend/services"
os.makedirs(base_dir, exist_ok=True)

for svc in services:
    service_dir = os.path.join(base_dir, svc["slug"])
    os.makedirs(service_dir, exist_ok=True)
    
    html_content = base_template.format(
        title=svc["name"].upper(),
        tagline=svc["tagline"],
        price=svc["price"]
    )
    
    with open(os.path.join(service_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(services)} service pages.")
