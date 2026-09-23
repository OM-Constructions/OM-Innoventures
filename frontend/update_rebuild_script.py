import re

with open('rebuild_services_unique.py', 'r', encoding='utf-8') as f:
    content = f.read()

css_addition = """
        .sp-enquiry-card {
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            margin-top: 40px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        .sp-enquiry-form .form-row {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        @media(max-width: 768px) {
            .sp-enquiry-form .form-row { flex-direction: column; gap: 0; }
        }
        .sp-enquiry-form .form-group {
            flex: 1;
            margin-bottom: 20px;
        }
        .sp-enquiry-form label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--navy-primary);
        }
        .sp-enquiry-form input, .sp-enquiry-form textarea {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-family: inherit;
            transition: border-color 0.3s;
        }
        .sp-enquiry-form input:focus, .sp-enquiry-form textarea:focus {
            outline: none;
            border-color: var(--gold-accent);
        }
"""

content = content.replace("        /* Layout specific styles for new sections */", css_addition + "        /* Layout specific styles for new sections */")

old_cta = """        <!-- 8. CLOSING CTA BANNER -->
        <section class="sp-section">
            <div class="container gsap-reveal">
                <div class="sp-cta-banner">
                    <h2 class="sp-title">Ready to Elevate Your Business?</h2>
                    <p>Let's discuss how our __TITLE_CLEAN__ expertise can solve your most pressing challenges and accelerate your growth.</p>
                    <a href="../../index.html#cta" class="btn-primary" style="background: var(--gold-accent); color: var(--navy-primary);">Schedule a Free Consultation</a>
                </div>
            </div>
        </section>"""

new_form = """        <!-- 8. ENQUIRY FORM -->
        <section class="sp-section sp-section-gray" id="enquire">
            <div class="container gsap-reveal">
                <span class="sp-label" style="color: var(--navy-primary);">07 &mdash; ENQUIRE NOW</span>
                <h2 class="sp-title" style="text-align: center;">Start Your __TITLE_CLEAN__ Project</h2>
                <p style="text-align: center; max-width: 600px; margin: 0 auto 30px auto;">Fill out the form below and our specialized team will get back to you within 24 hours.</p>
                
                <div class="sp-enquiry-card">
                    <form action="#" method="POST" class="sp-enquiry-form">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="name">Full Name *</label>
                                <input type="text" id="name" required placeholder="John Doe">
                            </div>
                            <div class="form-group">
                                <label for="email">Work Email *</label>
                                <input type="email" id="email" required placeholder="john@company.com">
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="phone">Phone Number</label>
                                <input type="tel" id="phone" placeholder="+1 (555) 000-0000">
                            </div>
                            <div class="form-group">
                                <label for="company">Company Name</label>
                                <input type="text" id="company" placeholder="Acme Corp">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="details">Project Details *</label>
                            <textarea id="details" required rows="4" placeholder="Tell us about your requirements..."></textarea>
                        </div>
                        <button type="submit" class="btn-primary" style="width: 100%; margin-top: 10px;">Submit Enquiry</button>
                    </form>
                </div>
            </div>
        </section>"""

content = content.replace(old_cta, new_form)

# Add "Enquire Now" to the hero button too, pointing to #enquire
hero_old = """<a href="../../index.html#cta" class="btn-primary">Discuss Your Project</a>"""
hero_new = """<a href="#enquire" class="btn-primary">Enquire Now</a>"""
content = content.replace(hero_old, hero_new)

with open('rebuild_services_unique.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script to include enquiry form")
