import re

services = [
    {"slug": "data-analytics-bi", "name": "Data Analytics & BI", "price": "Starting ₹14,999", "img": "service_ml.jpg"},
    {"slug": "data-science", "name": "Data Science", "price": "Starting ₹24,999", "img": "service_ml.jpg"},
    {"slug": "ai-ml-solutions", "name": "AI / ML Solutions", "price": "Starting ₹49,999", "img": "service_ml.jpg"},
    {"slug": "software-development", "name": "Software Development", "price": "Starting ₹99,999", "img": "service_vision.jpg"},
    {"slug": "product-development", "name": "Product Development", "price": "Starting ₹1,49,999", "img": "service_vision.jpg"},
    {"slug": "ui-ux-design", "name": "UI / UX Design", "price": "Starting ₹29,999", "img": "service_vision.jpg"},
    {"slug": "graphic-design", "name": "Graphic Design", "price": "Starting ₹9,999", "img": "service_vision.jpg"},
    {"slug": "finance-accounting", "name": "Finance & Accounting Services", "price": "Starting ₹19,999", "img": "service_analytics.jpg"},
    {"slug": "auditing-assurance", "name": "Auditing & Assurance Services", "price": "Starting ₹39,999", "img": "service_analytics.jpg"},
    {"slug": "cybersecurity", "name": "Cybersecurity Services", "price": "Starting ₹49,999", "img": "service_analytics.jpg"},
    {"slug": "saas-ai-solutions", "name": "SaaS & AI Powered Solutions", "price": "Starting ₹1,99,999", "img": "service_ml.jpg"}
]

html_cards = ""
for i, svc in enumerate(services):
    index = i + 1
    # Add hidden class to cards after 10
    display_style = 'style="display: none;"' if index > 10 else ''
    html_cards += f'''                    <a href="services/{svc['slug']}/index.html" class="service-card reveal-card" data-index="{index}" {display_style}>
                        <span class="service-number">{index:02d}</span>
                        <h3 class="service-title">{svc['name']}</h3>
                        <div class="service-price-block">
                            <span class="price-label">PRICE</span>
                            <span class="price-value">{svc['price']}</span>
                        </div>
                        <div class="service-hover-image">
                            <img src="assets/ai_images/{svc['img']}" alt="{svc['name']}">
                        </div>
                    </a>\n'''

services_section = f'''        <!-- SERVICES -->
        <section id="services" class="section-gray">
            <div class="container">
                <span class="eyebrow">OUR CORE FOCUS</span>
                <h2 class="section-title">Our Services</h2>
                <p class="section-subtitle">A comprehensive suite of capabilities designed to elevate your business.</p>
                <div class="services-grid" id="main-services-grid">
{html_cards}                </div>
                
                <div id="view-more-container" style="text-align: center; margin-top: 50px;">
                    <button id="view-more-btn" class="btn-outline">View More Services</button>
                </div>
            </div>
        </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the featured services section
pattern = r'<!-- FEATURED SERVICES -->.*?</section>'
content = re.sub(pattern, services_section, content, flags=re.DOTALL)

# Add the script to the end of the file if not already there
if 'servicesReveal.js' not in content:
    content = content.replace('</body>', '    <script type="module" src="src/servicesReveal.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with new services section and script link.")
