import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title and Brand
content = content.replace('<title>OM Innoventures & Build AI technologies</title>', '<title>OM Innoventures</title>')
content = content.replace('<span class="brand-om">OM</span><span class="brand-long">s</span>', '<span class="brand-om">OM</span><span class="brand-long">Intelligence</span>')
content = content.replace('<span class="brand-mobile-text">s</span>', '<span class="brand-mobile-text">Intelligence</span>')

# 2. Splash Text
content = content.replace('<div class="company-name">s</div>', '<div class="company-name">Intelligence</div>')
content = content.replace('<span>&amp; Engineering consultants</span>', '<span>&amp; AI Agency</span>')

# 3. Hero Section
content = content.replace('<span class="eyebrow">ENGINEERING TODAY &bull; BUILDING TOMORROW</span>', '<span class="eyebrow">INTELLIGENCE TODAY &bull; BUILDING TOMORROW</span>')
content = content.replace('<p>We deliver high-quality  and engineering solutions from concept to completion &mdash;', '<p>We deliver high-quality artificial intelligence solutions from concept to completion &mdash;')
content = content.replace('creating structures built for performance, durability, and lasting value.</p>', 'creating models built for performance, accuracy, and lasting value.</p>')

# Replace video with image
video_tag = '<video src="assets/hero/building.mp4" class="hero-video" id="hero-video" autoplay muted loop\n                        playsinline preload="metadata"></video>'
img_tag = '<img src="assets/ai_images/hero_ai.jpg" class="hero-video" id="hero-video" alt="AI Neural Network" style="object-fit: cover; width: 100%; height: 100%;">'
content = content.replace(video_tag, img_tag)

# Hero Annotations
content = content.replace('<span class="ann-text">ARCHITECTURAL DESIGN</span>', '<span class="ann-text">MACHINE LEARNING</span>')
content = content.replace('<span class="ann-text">STRUCTURAL ENGINEERING</span>', '<span class="ann-text">NEURAL NETWORKS</span>')
content = content.replace('<span class="ann-text">PROJECT PLANNING</span>', '<span class="ann-text">PREDICTIVE ANALYTICS</span>')

# 4. Capabilities Strip
strip_replacements = {
    'FASTER DELIVERY': 'MACHINE LEARNING',
    'ON-TIME COMPLETION': 'NATURAL LANGUAGE PROCESSING',
    'QUALITY FIRST': 'COMPUTER VISION',
    'COST EFFICIENT': 'PREDICTIVE ANALYTICS',
    'RELIABLE EXECUTION': 'DEEP LEARNING',
    'ENGINE PRECISION': 'AI CONSULTING',
    'END-TO-END SOLUTIONS': 'NEURAL NETWORKS',
    'CUSTOMER FOCUSED': 'DATA SCIENCE'
}
for old, new in strip_replacements.items():
    content = content.replace(f'<span class="ticker-item">{old}</span>', f'<span class="ticker-item">{new}</span>')

# 5. Services Section Header
content = content.replace('<span class="eyebrow">OUR  &amp; ENGINEERING SERVICES</span>', '<span class="eyebrow">OUR ARTIFICIAL INTELLIGENCE SERVICES</span>')
content = content.replace('<h2 class="section-title">Engineering Excellence. Built on Trust.</h2>', '<h2 class="section-title">Intelligence Excellence. Built on Trust.</h2>')
content = content.replace('<p class="section-subtitle">We deliver comprehensive  and structural solutions, prioritizing\n                    safety, quality, and precision from concept to completion.</p>', '<p class="section-subtitle">We deliver comprehensive AI and machine learning solutions, prioritizing\n                    accuracy, scalability, and precision from concept to completion.</p>')

# 6. Service Cards (Regex to replace images and titles)
services = [
    (" COST", "AI STRATEGY", "service_analytics.jpg"),
    ("ARCHITECTURAL DESIGN", "NATURAL LANGUAGE PROCESSING", "service_nlp.jpg"),
    ("ARCHITECTURAL 2D PLANS", "COMPUTER VISION", "service_vision.jpg"),
    ("STRUCTURAL DESIGN", "MACHINE LEARNING", "service_ml.jpg"),
    ("PROJECT PLANNING", "PREDICTIVE ANALYTICS", "service_analytics.jpg"),
    ("INTERIOR DESIGN", "DEEP LEARNING", "service_nlp.jpg"),
    ("GEOTECHNICAL REPORT", "DATA SCIENCE", "service_ml.jpg"),
    ("MEP DESIGNS", "AI CONSULTING", "service_vision.jpg"),
    ("3D BUILDING DESIGN", "NEURAL NETWORKS", "service_ml.jpg"),
    ("REALISTIC RENDERING", "GENERATIVE AI", "service_nlp.jpg"),
    ("ESTIMATION &amp; COSTING", "DATA ENGINEERING", "service_analytics.jpg"),
    ("TOTAL STATION SURVEY", "MLOPS", "service_vision.jpg"),
    ("INTERIOR DESIGN + EXECUTION", "AI IN HEALTHCARE", "service_ml.jpg"),
    ("COMPLETE DESIGN PACKAGE", "AI IN FINANCE", "service_analytics.jpg"),
    ("PREMIUM COMPLETE DESIGN PACKAGE", "CUSTOM AI SOLUTIONS", "service_nlp.jpg"),
    ("TURNKEY HOME ", "ENTERPRISE AI", "service_vision.jpg")
]

for old_title, new_title, img in services:
    content = content.replace(f'<h3 class="service-title">{old_title}</h3>', f'<h3 class="service-title">{new_title}</h3>')

content = re.sub(r'src="assets/services/[^"]+"', 'src="assets/ai_images/service_nlp.jpg"', content)

# 7. Capabilities Section
content = content.replace('<span class="eyebrow">OUR ENGINEERING CAPABILITIES</span>', '<span class="eyebrow">OUR AI CAPABILITIES</span>')
content = content.replace('<p class="section-subtitle">Proven engineering methods and  standards behind every\n                        project.</p>', '<p class="section-subtitle">Proven AI methods and machine learning standards behind every\n                        project.</p>')

content = content.replace('<h3>STRUCTURAL SYSTEMS</h3>', '<h3>AI SYSTEMS</h3>')
content = content.replace('<li>RCC </li>', '<li>Machine Learning</li>')
content = content.replace('<li>Steel Structures</li>', '<li>Deep Learning</li>')
content = content.replace('<li>Precast </li>', '<li>Neural Networks</li>')

content = content.replace('<li>IS Code Compliance</li>', '<li>Data Privacy Laws</li>')
content = content.replace('<li>ISO 9001 Standards</li>', '<li>AI Ethics Standards</li>')
content = content.replace('<li>Vaastu Compliance</li>', '<li>Model Fairness</li>')

content = content.replace('<li>Design-Build</li>', '<li>Agile Development</li>')
content = content.replace('<li>EPC Contracts</li>', '<li>MLOps Pipelines</li>')
content = content.replace('<li>Turnkey Projects</li>', '<li>Cloud Deployment</li>')

content = content.replace('<li>Green Building Practices</li>', '<li>Efficient Computing</li>')
content = content.replace('<li>Energy-Efficient Design</li>', '<li>Model Optimization</li>')
content = content.replace('<li>Material Optimization</li>', '<li>Hardware Acceleration</li>')

# 8. Industries Section
ind_replacements = {
    'RESIDENTIAL ': 'HEALTHCARE',
    'COMMERCIAL BUILDINGS': 'FINANCE',
    'INDUSTRIAL FACILITIES': 'E-COMMERCE',
    'INFRASTRUCTURE PROJECTS': 'MANUFACTURING',
    'INSTITUTIONAL BUILDINGS': 'EDUCATION',
    'HOSPITALITY PROJECTS': 'LOGISTICS',
    'RENOVATION &amp; RETROFIT': 'CYBERSECURITY',
    'GOVERNMENT &amp; PUBLIC WORKS': 'PUBLIC SECTOR'
}
for old, new in ind_replacements.items():
    content = content.replace(f'<h3>{old}</h3>', f'<h3>{new}</h3>')

# 9. Selected Work Section
content = content.replace('MODERN VILLA', 'HEALTHCARE DIAGNOSTICS AI')
content = content.replace('APARTMENT BUILDING', 'ALGORITHMIC TRADING BOT')
content = content.replace('INDEPENDENT HOUSE', 'SMART LOGISTICS ROUTING')
content = content.replace('CONTEMPORARY RESIDENCE', 'AI CUSTOMER SUPPORT')

content = content.replace('assets/projects/modern-villa.webp', 'assets/ai_images/project_healthcare.jpg')
content = content.replace('assets/projects/apartment-building.webp', 'assets/ai_images/project_finance.jpg')
content = content.replace('assets/projects/independent-house.webp', 'assets/ai_images/project_healthcare.jpg')
content = content.replace('assets/projects/contemporary-residence.webp', 'assets/ai_images/project_finance.jpg')

# 10. About Section
content = content.replace('<span class="eyebrow">ABOUT OM Innoventures & Build AI technologies</span>', '<span class="eyebrow">ABOUT OM INNOVENTURES</span>')
content = content.replace('OM Innoventures & Build AI technologies &amp; Engineering Consultants brings precision engineering, thoughtful\n                        design, and disciplined project execution together to deliver structures built for performance,\n                        durability, and lasting value.', 'OM Innoventures brings cutting-edge AI research, thoughtful\n                        model design, and disciplined deployment execution together to deliver solutions built for performance,\n                        accuracy, and lasting value.')
content = content.replace('assets/founder/kishor-kumar-a.jpg', 'assets/ai_images/founder_ai.jpg')
content = content.replace('BE Civil Engineer / Senior Architect / Data Analyst', 'Lead AI Researcher / Machine Learning Engineer / Data Scientist')
content = content.replace('Combining structural expertise with architectural vision and data-driven insights to\n                                deliver precision engineering and premium built-environments.', 'Combining deep learning expertise with architectural vision and data-driven insights to\n                                deliver precision models and premium AI solutions.')

# 11. Engineering Section (bottom)
content = content.replace('<span class="eyebrow">OM Innoventures & Build AI technologies &amp; ENGINEERING CONSULTANTS</span>', '<span class="eyebrow">OM INNOVENTURES AI CONSULTANTS</span>')
content = content.replace('<h2 class="section-title">Engineering &amp; Built Environments</h2>', '<h2 class="section-title">Intelligence &amp; AI Environments</h2>')
content = content.replace('Engineering excellence built on trust. We provide precise, scalable\n                            engineering and architectural services.', 'Intelligence excellence built on trust. We provide precise, scalable\n                            machine learning and AI services.')

for old_title, new_title, img in services:
    content = content.replace(f'<span>{old_title}</span>', f'<span>{new_title}</span>')

# 12. Why OM
content = content.replace('<span class="eyebrow">WHY OM Innoventures & Build AI technologies</span>', '<span class="eyebrow">WHY OM INNOVENTURES</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
