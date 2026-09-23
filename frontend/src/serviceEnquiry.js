import { submitEnquiry } from './api.js';

// Canonical service slugs mapping
const SERVICE_SLUGS = {
    "Data Analytics & Data Scientist & AI Solutions": "data-analytics-bi",
    "Data analytics & Data Sciencitist & AI solutions": "data-analytics-bi",
    "Data Analytics & AI Solutions": "data-analytics-bi",
    "Data Analytics & BI": "data-analytics-bi",
    "Data Science": "data-science",
    "AI / ML Solutions": "ai-ml-solutions",
    "Software Development": "software-development",
    "Full Stack Development": "full-stack-development",
    "Product Development": "product-development",
    "UI / UX Design": "ui-ux-design",
    "SaaS & AI Solutions": "saas-ai-solutions",
    "Cybersecurity": "cybersecurity",
    "Finance & Accounting": "finance-accounting",
    "Auditing & Assurance": "auditing-assurance",
    "Construction Analytics": "construction-analytics",
    "Graphic Design": "graphic-design",
    "Project Planning": "project-planning",
    "General Consultation": "general-consultation"
};

// Global submission lock to guarantee only 1 request is sent at a time
let globalEnquirySubmitting = false;

/**
 * Resolves visible service title to canonical name and slug.
 */
function resolveServiceSlug(rawTitle) {
    if (!rawTitle) return { name: 'General Consultation', slug: 'general-consultation' };
    const trimmed = rawTitle.trim();
    if (SERVICE_SLUGS[trimmed]) {
        return { name: trimmed, slug: SERVICE_SLUGS[trimmed] };
    }
    const lower = trimmed.toLowerCase();
    for (const [name, slug] of Object.entries(SERVICE_SLUGS)) {
        if (name.toLowerCase() === lower || lower.includes(name.toLowerCase())) {
            return { name, slug };
        }
    }
    const slugified = trimmed.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    return { name: trimmed, slug: slugified || 'general-consultation' };
}

/**
 * Detects current service slug from URL path if on a service detail page.
 */
function detectCurrentServiceSlug() {
    if (typeof window === 'undefined') return 'general-consultation';
    const path = window.location.pathname;
    const match = path.match(/\/services\/([^\/]+)/);
    if (match && match[1]) {
        return match[1].replace(/\.html$/, '');
    }
    const h1 = document.querySelector('h1');
    if (h1 && h1.textContent) {
        return resolveServiceSlug(h1.textContent).slug;
    }
    return 'general-consultation';
}

/**
 * Main initialization entry point.
 */
export function initServiceContactCards() {
    initServiceDetailPageEnquiry();
    initGlobalEnquiryForm();
}

/**
 * Initializes enquiry forms on Service Detail Pages (/services/[slug]/index.html)
 */
export function initServiceDetailPageEnquiry() {
    const forms = document.querySelectorAll('.sp-enquiry-form, #form-service-detail-enquiry, .service-enquiry-box form, .sp-enquiry-card form');
    if (!forms || forms.length === 0) return;

    forms.forEach((form) => {
        // Strict deduplication guard
        if (form._enquiryBound || form.dataset.enquiryBound === 'true') return;
        form._enquiryBound = true;
        form.dataset.enquiryBound = 'true';

        const cardContainer = form.closest('.sp-enquiry-card') || form.closest('.service-enquiry-box') || form.parentElement;
        const currentServiceSlug = form.getAttribute('data-service-slug') ||
            (cardContainer && cardContainer.getAttribute('data-service-slug')) ||
            detectCurrentServiceSlug();

        const submitBtn = form.querySelector('button[type="submit"], .btn-primary, .service-enquiry-submit-btn');
        let errorEl = form.querySelector('.service-enquiry-error, .sp-form-error');
        let successEl = (cardContainer && cardContainer.querySelector('.service-enquiry-success, .sp-enquiry-success')) || null;

        if (!errorEl) {
            errorEl = document.createElement('div');
            errorEl.className = 'sp-form-error';
            errorEl.style.cssText = 'display:none; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); color:#ef4444; padding:10px 14px; border-radius:6px; margin-bottom:14px; font-size:0.9rem;';
            form.insertBefore(errorEl, form.firstChild);
        }

        let isCardSubmitting = false;

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            e.stopPropagation();

            if (isCardSubmitting || globalEnquirySubmitting) return;

            const nameInput = form.querySelector('input[name="name"], input#name');
            const emailInput = form.querySelector('input[name="email"], input#email');
            const phoneInput = form.querySelector('input[name="phone"], input#phone');
            const companyInput = form.querySelector('input[name="company"], input#company, input[name="location"], input#location');
            const detailsInput = form.querySelector('textarea[name="details"], textarea#details, textarea[name="message"], textarea#message');
            const honeypotInput = form.querySelector('input[name="website"], input[name="honeypot"]');

            const name = nameInput ? nameInput.value.trim() : '';
            const email = emailInput ? emailInput.value.trim() : '';
            const phone = phoneInput ? phoneInput.value.trim() : '';
            const companyOrLocation = companyInput ? companyInput.value.trim() : '';
            const message = detailsInput ? detailsInput.value.trim() : '';
            const honeypot = honeypotInput ? honeypotInput.value : '';

            if (!name) {
                errorEl.textContent = 'Please enter your full name.';
                errorEl.style.display = 'block';
                return;
            }

            if (!email) {
                errorEl.textContent = 'Please enter a valid email address.';
                errorEl.style.display = 'block';
                return;
            }

            if (!message && message.length < 3) {
                errorEl.textContent = 'Please provide brief details about your project or requirements.';
                errorEl.style.display = 'block';
                return;
            }

            errorEl.style.display = 'none';

            isCardSubmitting = true;
            globalEnquirySubmitting = true;

            const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Submit Enquiry';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = 'Sending enquiry...';
            }

            try {
                const payload = {
                    name,
                    email,
                    phone: phone || null,
                    serviceSlug: currentServiceSlug,
                    location: companyOrLocation || "Direct Service Enquiry",
                    message: companyOrLocation ? `[Company / Location: ${companyOrLocation}]\n\n${message}` : message,
                    honeypot: honeypot || ''
                };

                await submitEnquiry(payload);

                if (cardContainer) {
                    cardContainer.innerHTML = `
                        <div style="text-align: center; padding: 40px 20px; background: rgba(16, 185, 129, 0.06); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; animation: fadeIn 0.4s ease;">
                            <div style="width: 56px; height: 56px; background: #10b981; color: white; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 28px; margin-bottom: 16px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);">
                                ✓
                            </div>
                            <h3 style="font-size: 1.5rem; margin-bottom: 10px; color: #0f172a; font-weight: 700;">Request Sent Successfully!</h3>
                            <p style="font-size: 1rem; color: #475569; max-width: 500px; margin: 0 auto; line-height: 1.6;">
                                Thank you <strong>${escapeHTML(name)}</strong>! We've received your project enquiry. Our engineering team will review your scope and contact you at <strong>${escapeHTML(email)}</strong> within 24 hours.
                            </p>
                        </div>
                    `;
                } else {
                    form.reset();
                    if (successEl) successEl.style.display = 'block';
                }
            } catch (err) {
                console.error('Service page enquiry submission error:', err);
                errorEl.textContent = err.message || 'Failed to submit enquiry. Please check your connection or contact us directly.';
                errorEl.style.display = 'block';
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                }
            } finally {
                isCardSubmitting = false;
                globalEnquirySubmitting = false;
            }
        });
    });
}

/**
 * Initializes the global project enquiry form on the Homepage (#cta / #global-enquiry-box)
 */
export function initGlobalEnquiryForm() {
    const card = document.getElementById('global-enquiry-box');
    const form = document.getElementById('global-enquiry-form');
    if (!form) return;

    // Strict deduplication guard
    if (form._enquiryBound || form.dataset.enquiryBound === 'true') return;
    form._enquiryBound = true;
    form.dataset.enquiryBound = 'true';

    form.style.display = 'block';

    const successEl = card ? card.querySelector('.global-enquiry-success') : null;
    let errorEl = form.querySelector('.global-enquiry-error, .ge-error');
    const submitBtn = form.querySelector('.global-enquiry-submit-btn, button[type="submit"]');

    if (!errorEl) {
        errorEl = document.createElement('div');
        errorEl.className = 'global-enquiry-error';
        errorEl.style.cssText = 'display:none; background:rgba(239,68,68,0.12); border:1px solid rgba(239,68,68,0.3); color:#f87171; padding:12px 16px; border-radius:8px; margin-bottom:16px; font-size:0.9rem;';
        form.insertBefore(errorEl, form.firstChild);
    }

    let isGlobalSubmitting = false;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        e.stopPropagation();

        if (isGlobalSubmitting || globalEnquirySubmitting) return;

        const name = form.elements.name ? form.elements.name.value.trim() : '';
        const email = form.elements.email ? form.elements.email.value.trim() : '';
        const phone = form.elements.phone ? form.elements.phone.value.trim() : '';
        const serviceSlug = form.elements.service_slug ? form.elements.service_slug.value : 'general-consultation';
        const locationVal = form.elements.location ? form.elements.location.value.trim() : '';
        const areaVal = form.elements.area ? form.elements.area.value.trim() : '';
        const rawMessage = form.elements.message ? form.elements.message.value.trim() : '';
        const honeypot = form.elements.website ? form.elements.website.value : '';

        if (!name) {
            errorEl.textContent = 'Please enter your name.';
            errorEl.style.display = 'block';
            return;
        }

        if (!email) {
            errorEl.textContent = 'Please enter your email address.';
            errorEl.style.display = 'block';
            return;
        }

        if (!phone) {
            errorEl.textContent = 'Please enter your Phone / WhatsApp number.';
            errorEl.style.display = 'block';
            return;
        }

        const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Project Enquiry &rarr;';
        errorEl.style.display = 'none';

        isGlobalSubmitting = true;
        globalEnquirySubmitting = true;

        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Sending enquiry...';
        }

        const metaParts = [];
        if (locationVal) metaParts.push(`Location: ${locationVal}`);
        if (areaVal) metaParts.push(`Approx. Area / Type: ${areaVal}`);

        let message = rawMessage || 'Project Consultation Request';
        if (metaParts.length > 0) {
            message = `[${metaParts.join(' | ')}]\n\n${message}`;
        }

        try {
            await submitEnquiry({
                name,
                email,
                phone: phone || null,
                serviceSlug: serviceSlug,
                location: locationVal || "Direct Consultation",
                message: message,
                honeypot: honeypot || ''
            });

            if (card) {
                card.innerHTML = `
                    <div style="text-align: center; padding: 48px 24px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 16px; animation: fadeIn 0.4s ease;">
                        <div style="width: 64px; height: 64px; background: #10b981; color: white; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 32px; margin-bottom: 20px; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);">
                            ✓
                        </div>
                        <h3 style="font-size: 1.8rem; margin-bottom: 12px; color: #07152f; font-weight: 700; font-family: var(--font-heading, inherit);">Request Sent Successfully!</h3>
                        <p style="font-size: 1.05rem; color: #334155; max-width: 580px; margin: 0 auto; line-height: 1.6;">
                            Thank you <strong style="color: #07152f;">${escapeHTML(name)}</strong>! We've received your project details. Our senior engineering &amp; AI team will review your scope and get in touch at <strong style="color: #07152f;">${escapeHTML(email)}</strong> within 24 hours.
                        </p>
                    </div>
                `;
            } else {
                form.reset();
                if (successEl) successEl.style.display = 'block';
            }
        } catch (err) {
            console.error('Global enquiry submission error:', err);
            errorEl.textContent = err.message || 'Failed to send your enquiry. Please check your network connection or email us directly at omengineeringconsultants06@gmail.com.';
            errorEl.style.display = 'block';
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        } finally {
            isGlobalSubmitting = false;
            globalEnquirySubmitting = false;
        }
    });
}

function escapeHTML(str) {
    if (!str) return '';
    return str.replace(/[&<>'"]/g,
        tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag));
}

// Auto-run once on DOM ready
if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initServiceContactCards);
    } else {
        initServiceContactCards();
    }
}
