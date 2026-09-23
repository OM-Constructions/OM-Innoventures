import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the full services block
services_pattern = r'(<!-- SERVICES - WEBSITE DESIGN -->.*?<!-- SERVICES - ACCOUNTING -->.*?</section>)'
match = re.search(services_pattern, content, flags=re.DOTALL)

if not match:
    print("Could not find services section in index.html")
    exit(1)

full_services_html = match.group(1)

# Generate services.html
# We will use the layout of index.html but replace the body content with the services
header_pattern = r'(.*?<!-- SERVICES - WEBSITE DESIGN -->)'
footer_pattern = r'(</main>\s*<!-- FOOTER -->.*)'

header_match = re.search(header_pattern, content, flags=re.DOTALL)
footer_match = re.search(footer_pattern, content, flags=re.DOTALL)

if header_match and footer_match:
    header_html = header_match.group(1)
    footer_html = footer_match.group(1)
    
    # Remove the intro splash and hero from the header for the services page
    header_html = re.sub(r'<!-- INTRO SPLASH -->.*?<!-- HERO -->.*?<div class="hero-actions">.*?</div>.*?</div>.*?</div>.*?<!-- CAPABILITIES -->', '', header_html, flags=re.DOTALL)
    
    # Add a custom hero for the services page
    services_hero = '''
    <main>
        <!-- HERO -->
        <section class="service-page-hero" style="padding-top: 150px; padding-bottom: 50px; background-color: var(--dark-bg); text-align: center;">
            <div class="container gsap-reveal">
                <span class="eyebrow">OUR CAPABILITIES</span>
                <h1>ALL SERVICES</h1>
                <p>Comprehensive Intelligence, Design, and Assurance solutions.</p>
                <div class="service-hero-accent" style="margin: 30px auto 0;"></div>
            </div>
        </section>
'''
    
    # We need to construct services.html carefully.
    # Actually, it's easier to just use the structure we know.
    services_page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Services | OM Innoventures</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="./style.css?v=11">
    
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
            <a href="index.html" class="nav-brand">
                <span class="brand-om">OM</span><span class="brand-long">Intelligence</span>
            </a>
            <div class="nav-links">
                <a href="index.html#hero" class="nav-link-item">Home</a>
                <a href="services.html" class="nav-link-item">Services</a>
                <a href="index.html#capabilities" class="nav-link-item">Capabilities</a>
                <a href="index.html#industries" class="nav-link-item">Industries</a>
            </div>
            <button class="hamburger">☰</button>
        </div>
    </nav>

    {services_hero}
    
    {full_services_html}
    
    </main>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>OM INNOVENTURES</h3>
                    <p>&amp; AI AGENCY</p>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 OM Innoventures. All rights reserved.</span>
            </div>
        </div>
    </footer>

    <script type="module" src="./src/main.js"></script>
</body>
</html>
'''
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(services_page_html)

# Now, update index.html to only have a single "Featured Services" block
featured_services = '''        <!-- FEATURED SERVICES -->
        <section id="services-featured" class="section-gray">
            <div class="container">
                <span class="eyebrow">OUR CORE FOCUS</span>
                <h2 class="section-title">Featured Services</h2>
                <p class="section-subtitle">A glimpse into our comprehensive AI and Software capabilities.</p>
                <div class="services-grid">
                    <a href="services/ai-web-application/index.html" class="service-card" data-index="1">
                        <span class="service-number">01</span>
                        <h3 class="service-title">AI Web Application</h3>
                        <div class="service-price-block">
                            <span class="price-label">PRICE</span>
                            <span class="price-value">₹1,49,999+</span>
                        </div>
                        <div class="service-hover-image"><img src="assets/ai_images/service_vision.jpg" alt="AI Web Application"></div>
                    </a>
                    <a href="services/machine-learning-model/index.html" class="service-card" data-index="2">
                        <span class="service-number">02</span>
                        <h3 class="service-title">Machine Learning Model</h3>
                        <div class="service-price-block">
                            <span class="price-label">PRICE</span>
                            <span class="price-value">₹39,999</span>
                        </div>
                        <div class="service-hover-image"><img src="assets/ai_images/service_ml.jpg" alt="Machine Learning Model"></div>
                    </a>
                    <a href="services/corporate-audit-accounting/index.html" class="service-card" data-index="3">
                        <span class="service-number">03</span>
                        <h3 class="service-title">Corporate Audit & Accounting</h3>
                        <div class="service-price-block">
                            <span class="price-label">PRICE</span>
                            <span class="price-value">Starting ₹99,999</span>
                        </div>
                        <div class="service-hover-image"><img src="assets/ai_images/service_analytics.jpg" alt="Corporate Audit & Accounting"></div>
                    </a>
                </div>
                
                <div style="text-align: center; margin-top: 50px;">
                    <a href="services.html" class="btn-primary">View All 37 Services</a>
                </div>
            </div>
        </section>'''

new_index_content = re.sub(services_pattern, featured_services, content, flags=re.DOTALL)
new_index_content = new_index_content.replace('href="#services-website"', 'href="services.html"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_content)

print("Created services.html and simplified index.html")
