import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

saas_section = """
        <!-- SAAS PRODUCTS -->
        <section id="saas-products" class="section-gray" style="background-color: var(--navy-primary); color: white;">
            <div class="container">
                <span class="eyebrow" style="color: var(--gold-accent);">OUR FLAGSHIP PRODUCTS</span>
                <h2 class="section-title" style="color: white;">SaaS Solutions</h2>
                <p class="section-subtitle" style="color: #ccc;">Powerful, AI-driven platforms currently transforming industries.</p>
                
                <div class="services-grid" style="margin-top: 40px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <!-- Sentinel AI -->
                    <a href="https://sentinalguardai.lovable.app/" target="_blank" class="service-card reveal-card" style="background: white; color: var(--navy-primary); text-decoration: none;">
                        <div style="height: 250px; overflow: hidden; border-radius: 8px 8px 0 0; margin: -30px -30px 20px -30px;">
                            <img src="assets/saas/sentinel.jpg" alt="Sentinel AI" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        </div>
                        <h3 class="service-title" style="color: var(--navy-primary); font-size: 1.5rem; margin-bottom: 10px;">Sentinel AI</h3>
                        <p style="color: #666; margin-bottom: 20px; line-height: 1.5;">AI-powered workforce monitoring platform with real-time GPS tracking and QR verification.</p>
                        <span class="btn-primary" style="display: inline-block; padding: 10px 20px; font-size: 0.9rem;">Visit Website &rarr;</span>
                    </a>
                    
                    <!-- StayHub -->
                    <a href="https://stayhub-ai.lovable.app/" target="_blank" class="service-card reveal-card" style="background: white; color: var(--navy-primary); text-decoration: none;">
                        <div style="height: 250px; overflow: hidden; border-radius: 8px 8px 0 0; margin: -30px -30px 20px -30px;">
                            <img src="assets/saas/stayhub.jpg" alt="StayHub" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        </div>
                        <h3 class="service-title" style="color: var(--navy-primary); font-size: 1.5rem; margin-bottom: 10px;">StayHub</h3>
                        <p style="color: #666; margin-bottom: 20px; line-height: 1.5;">Smart PG Management platform to run your properties efficiently from anywhere, anytime.</p>
                        <span class="btn-primary" style="display: inline-block; padding: 10px 20px; font-size: 0.9rem;">Visit Website &rarr;</span>
                    </a>

                    <!-- EasyBuild -->
                    <a href="https://easybuild.lovable.app/" target="_blank" class="service-card reveal-card" style="background: white; color: var(--navy-primary); text-decoration: none;">
                        <div style="height: 250px; overflow: hidden; border-radius: 8px 8px 0 0; margin: -30px -30px 20px -30px;">
                            <img src="assets/saas/easybuild.jpg" alt="EasyBuild" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                        </div>
                        <h3 class="service-title" style="color: var(--navy-primary); font-size: 1.5rem; margin-bottom: 10px;">EasyBuild</h3>
                        <p style="color: #666; margin-bottom: 20px; line-height: 1.5;">The Operating System for modern  companies to build smarter and manage better.</p>
                        <span class="btn-primary" style="display: inline-block; padding: 10px 20px; font-size: 0.9rem;">Visit Website &rarr;</span>
                    </a>
                </div>
            </div>
        </section>

"""

pattern = r'(<!-- SELECTED WORK -->)'
content = re.sub(pattern, saas_section + r'\1', content)

# Change "About" link in the nav to "SaaS" or just add "SaaS Products" to the nav
nav_pattern = r'(<a href="#services" class="nav-link-item">Services</a>)'
content = re.sub(nav_pattern, r'\1\n                <a href="#saas-products" class="nav-link-item">SaaS Products</a>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected SaaS products section")
