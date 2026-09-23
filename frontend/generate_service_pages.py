import os
import re

# The lists from update_services.py
website_design = [
    ("1-page Landing Page", "₹7,999"),
    ("3-5 page Business Website", "₹14,999"),
    ("5-8 page Professional Website", "₹24,999"),
    ("Business + Contact/Enquiry Forms", "₹29,999"),
    ("Dynamic Business Website", "₹39,999"),
    ("E-commerce Website", "₹49,999+"),
    ("Advanced E-commerce", "₹74,999+"),
    ("Custom Web Application", "₹99,999+"),
    ("AI-powered Website", "₹74,999+"),
    ("AI Web Application", "₹1,49,999+"),
    ("Custom SaaS/Web Platform", "₹2,49,999+")
]

data_ai_services = [
    ("Excel Data Cleaning", "₹4,999"),
    ("Excel Data Analysis", "₹7,999"),
    ("Excel Automation", "₹9,999"),
    ("SQL Data Analysis", "₹9,999"),
    ("Power BI Dashboard", "₹12,999"),
    ("Advanced Power BI Dashboard", "₹19,999"),
    ("Python Data Analysis", "₹14,999"),
    ("Python + SQL Analytics", "₹19,999"),
    ("Business/Data Analytics", "₹24,999"),
    ("Sales Analytics", "₹14,999"),
    ("HR Analytics", "₹14,999"),
    ("Financial Analytics", "₹19,999"),
    (" Analytics", "₹19,999"),
    ("Predictive Analytics", "₹34,999"),
    ("Machine Learning Model", "₹39,999"),
    ("Advanced ML Project", "₹59,999"),
    ("ML + API Deployment", "₹74,999"),
    ("AI Chatbot", "₹49,999"),
    ("AI/RAG Knowledge Assistant", "₹69,999"),
    ("AI Business Automation", "₹59,999"),
    ("AI + ML Custom Solution", "₹99,999+"),
    ("Custom Data/AI Software", "₹1,49,999+")
]

accounting_services = [
    ("Accounting", "Starting ₹4,999"),
    ("Auditing", "Starting ₹19,999"),
    ("Audit + Accounting", "Starting ₹49,999"),
    ("Corporate Audit & Accounting", "Starting ₹99,999")
]

def to_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

all_services = website_design + data_ai_services + accounting_services

base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{uppercase_title} | OM Innoventures</title>
    
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
            <a href="../../index.html" class="nav-brand">OM<span>Intelligence</span></a>
            <div class="nav-links">
                <a href="../../index.html#hero">HOME</a>
                <a href="../../index.html#services-website">SERVICES</a>
            </div>
            <div class="nav-actions">
                <span id="nav-auth-container" class="nav-auth-group">
                    <a href="../../login.html" class="nav-auth-link nav-auth-login">Log In</a>
                    <a href="../../signup.html" class="nav-auth-link nav-auth-signup">Sign Up</a>
                </span>
                <a href="../../index.html#cta" class="btn-primary">Let's Talk</a>
                <script type="module">
                    import {{ getCurrentUser, logout }} from "../../src/auth.js";
                    const container = document.getElementById("nav-auth-container");
                    if (container) {{
                        getCurrentUser().then(user => {{
                            if (user) {{
                                container.innerHTML = `
                                    <a href="../../my-requests.html" class="nav-auth-link nav-auth-login" style="color: var(--gold-accent); font-weight: 600;">My Requests</a>
                                    <a href="#" id="nav-logout-link" class="nav-auth-link nav-auth-signup">Log Out</a>
                                `;
                                document.getElementById("nav-logout-link")?.addEventListener("click", async (e) => {{
                                    e.preventDefault();
                                    await logout().catch(() => {{}});
                                    window.location.reload();
                                }});
                            }}
                        }});
                    }}
                </script>
            </div>
            <button class="hamburger">☰</button>
        </div>
    </nav>

    <main class="service-page-main">
        <!-- HERO -->
        <section class="service-page-hero" style="padding-bottom: 30px;">
            <div class="container gsap-reveal">
                <span class="eyebrow">SERVICE DETAILS</span>
                <h1>{uppercase_title}</h1>
                <p>Innovative, data-driven, and perfectly scaled solutions designed around the core requirements and growth potential of your business.</p>
                <div class="service-hero-accent"></div>

                <!-- SPECIFIC REALISTIC SERVICE IMAGE SHOWCASE -->
                <div class="service-featured-image-box" style="margin: 36px auto 10px; max-width: 900px; border-radius: 14px; overflow: hidden; box-shadow: 0 16px 40px rgba(0,0,0,0.35); border: 1px solid rgba(201,151,34,0.35); position: relative; background: #07152f;">
                    <img src="../../assets/services/unique/{slug}.jpg" alt="{uppercase_title}" style="width: 100%; height: 440px; object-fit: cover; display: block; transition: transform 0.4s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'" onerror="this.src='../../assets/services/ai-ml-system.jpg'">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 22px 28px; background: linear-gradient(180deg, transparent 0%, rgba(5,13,26,0.95) 100%); display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 10px;">
                        <span style="color: var(--gold-accent, #daa520); font-family: 'Exo 2', sans-serif; font-weight: 700; font-size: 0.95rem; letter-spacing: 1px; text-transform: uppercase;">
                            ⚡ Real System Architecture &bull; {uppercase_title}
                        </span>
                        <span style="font-size: 0.82rem; color: #cbd5e1; background: rgba(0,0,0,0.6); padding: 5px 12px; border-radius: 4px; backdrop-filter: blur(4px);">
                            OM Innoventures &bull; Verified Implementation
                        </span>
                    </div>
                </div>
            </div>
        </section>

        <!-- 01 OVERVIEW -->
        <section class="sp-section sp-overview">
            <div class="container gsap-reveal">
                <span class="sp-label">01 &mdash; OVERVIEW</span>
                <p>At OM Innoventures, we believe that exceptional software begins with a deep understanding of your business purpose. Our {uppercase_title} services are designed to address both your immediate operational desires and the long-term scalability necessities of your project. We leverage modern methodologies to ensure everything we design is secure, sustainable, and built to the highest industry standards.</p>
            </div>
        </section>

        <!-- 02 WHAT WE FOCUS ON -->
        <section class="sp-section sp-section-gray">
            <div class="container gsap-reveal">
                <span class="sp-label" style="color: var(--navy-primary);">02 &mdash; WHAT WE FOCUS ON</span>
                <h2 class="sp-title">Capabilities & Deliverables</h2>
                <div class="sp-focus-grid">
                    
                    <div class="sp-focus-item">
                        <h3>Strategy & Planning</h3>
                        <p>Providing exact, professional outcomes focused on practical value and precision.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Custom Implementation</h3>
                        <p>Providing exact, professional outcomes focused on practical value and precision.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Quality Assurance</h3>
                        <p>Providing exact, professional outcomes focused on practical value and precision.</p>
                    </div>
                    <div class="sp-focus-item">
                        <h3>Continuous Support</h3>
                        <p>Providing exact, professional outcomes focused on practical value and precision.</p>
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

        <!-- RELATED PAST WORK & VERIFIED REVIEWS -->
        <section class="sp-section" style="background: rgba(255,255,255,0.02);">
            <div class="container gsap-reveal">
                <span class="sp-label">PAST WORK &amp; REVIEWS</span>
                <h2 class="sp-title">Verified Projects</h2>
                <div id="serviceProjectsContainer" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 30px;">
                    <!-- Dynamically populated from GET /api/v1/projects/published -->
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>OM INNOVENTURES</h3>
                    <p>&amp; AI AGENCY</p>
                </div>
                <div class="footer-col">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="../../index.html#hero">Home</a></li>
                        <li><a href="../../index.html#services-website">Services</a></li>
                        <li><a href="../../index.html#capabilities">Capabilities</a></li>
                        <li><a href="../../index.html#industries">Industries</a></li>
                        <li><a href="../../index.html#about">About</a></li>
                        <li><a href="../../index.html#cta">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 OM Innoventures. All rights reserved.</span>
            </div>
        </div>
    </footer>

    <script type="module" src="../../src/main.js"></script>
    <script type="module">
        import {{ renderPublishedProjects }} from "../../src/projectsRenderer.js";
        document.addEventListener('DOMContentLoaded', () => {{
            renderPublishedProjects('serviceProjectsContainer', '{slug}');
        }});
    </script>

    <script type="module">
        import gsap from 'gsap';
        import ScrollTrigger from 'gsap/ScrollTrigger';
        
        gsap.registerPlugin(ScrollTrigger);

        // Reveal elements using GSAP
        setTimeout(() => {{
            const reveals = document.querySelectorAll('.gsap-reveal');
            reveals.forEach((el) => {{
                gsap.fromTo(el, 
                    {{ opacity: 0, y: 50, visibility: 'hidden' }}, 
                    {{
                        scrollTrigger: {{
                            trigger: el,
                            start: "top 85%",
                            toggleActions: "play none none none"
                        }},
                        opacity: 1,
                        y: 0,
                        visibility: 'visible',
                        duration: 1,
                        ease: "power2.out"
                    }}
                );
            }});

            // Interactive 3D tilt motion on featured image
            const imgBox = document.querySelector('.service-featured-image-box');
            if (imgBox) {{
                imgBox.style.transition = 'transform 0.15s ease-out';
                imgBox.addEventListener('mousemove', (e) => {{
                    const rect = imgBox.getBoundingClientRect();
                    const x = e.clientX - rect.left - rect.width / 2;
                    const y = e.clientY - rect.top - rect.height / 2;
                    const rotX = (-y / rect.height) * 10;
                    const rotY = (x / rect.width) * 10;
                    imgBox.style.transform = `perspective(1000px) rotateX(${{rotX}}deg) rotateY(${{rotY}}deg) scale(1.02)`;
                }});
                imgBox.addEventListener('mouseleave', () => {{
                    imgBox.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
                }});
            }}
        }}, 100);
    </script>
</body>
</html>
"""

from pathlib import Path
base_dir = Path(__file__).resolve().parent / "services"
base_dir.mkdir(parents=True, exist_ok=True)

for title, price in all_services:
    slug = to_slug(title)
    service_dir = base_dir / slug
    service_dir.mkdir(parents=True, exist_ok=True)
    
    html_content = base_template.format(
        uppercase_title=title.upper(),
        price=price,
        slug=slug
    )
    
    with open(service_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generated {len(all_services)} service pages.")
