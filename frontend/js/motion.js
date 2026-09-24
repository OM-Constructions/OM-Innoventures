/**
 * OM Innoventures & Build AI Technologies
 * Professional Motion System - GSAP ScrollTrigger Integration
 */

export function initMotion() {
    // Register GSAP ScrollTrigger
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
    } else {
        console.warn('GSAP or ScrollTrigger not loaded. Motion animations will fallback to CSS transitions.');
        document.querySelectorAll('.reveal-up, .reveal-fade, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        return;
    }

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
        document.querySelectorAll('.reveal-up, .reveal-fade, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        return;
    }

    // 1. Explicit Reveal Up Elements
    document.querySelectorAll('.reveal-up').forEach((el) => {
        gsap.to(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 88%",
                toggleActions: "play none none none"
            },
            y: 0,
            opacity: 1,
            duration: 0.85,
            ease: "power3.out",
            clearProps: "transform,opacity"
        });
    });

    // 2. Section Headers Auto-Reveal (eyebrow, section-title, section-subtitle)
    const sectionHeaders = document.querySelectorAll('section .container > .eyebrow, section .container > .section-title, section .container > .section-subtitle, .section-header, .saas-eyebrow, .saas-title, .saas-subtitle');
    sectionHeaders.forEach((header) => {
        if (!header.classList.contains('reveal-up') && !header.classList.contains('no-anim')) {
            gsap.fromTo(header,
                { y: 24, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: header,
                        start: "top 90%",
                        toggleActions: "play none none none"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 0.8,
                    ease: "power3.out",
                    clearProps: "transform,opacity"
                }
            );
        }
    });

    // 3. Staggered Grid Reveals (Cards & Lists)
    const gridContainers = document.querySelectorAll('.services-grid, .products-grid, .capabilities-grid, .industries-grid, .stagger-grid, .grid-3, .grid-4, .tech-grid, .stats-grid');
    gridContainers.forEach(grid => {
        const items = Array.from(grid.children);
        if (items.length > 0) {
            gsap.fromTo(items,
                { y: 35, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: grid,
                        start: "top 82%",
                        toggleActions: "play none none none"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 0.7,
                    stagger: 0.08,
                    ease: "power3.out",
                    clearProps: "transform,opacity"
                }
            );
        }
    });

    // 4. Subtle 3D Tilt on Hover for Cards
    const interactiveCards = document.querySelectorAll('.service-card, .product-card, .hover-card, .feature-card, .saas-card');
    interactiveCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            const rotateX = (-y / rect.height) * 8;
            const rotateY = (x / rect.width) * 8;
            card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0px)';
        });
    });

    // 5. Parallax for background or accent visuals
    const parallaxBgs = document.querySelectorAll('.parallax-bg, .accent-glow');
    parallaxBgs.forEach(el => {
        gsap.to(el, {
            scrollTrigger: {
                trigger: el.parentElement || el,
                start: "top bottom",
                end: "bottom top",
                scrub: 0.6
            },
            y: "20%",
            ease: "none"
        });
    });

    // 6. Number Counter Animation for Stats (if any .stat-number or .counter)
    document.querySelectorAll('.stat-number, .counter').forEach(stat => {
        const targetText = stat.innerText.trim();
        const num = parseFloat(targetText.replace(/[^0-9.]/g, ''));
        if (!isNaN(num) && num > 0) {
            const prefix = targetText.match(/^[^\d]*/) ? targetText.match(/^[^\d]*/)[0] : '';
            const suffix = targetText.match(/[^\d.]*$/) ? targetText.match(/[^\d.]*$/)[0] : '';
            const isFloat = targetText.includes('.');

            gsap.fromTo(stat, 
                { textContent: 0 },
                {
                    scrollTrigger: {
                        trigger: stat,
                        start: "top 85%",
                        toggleActions: "play none none none"
                    },
                    textContent: num,
                    duration: 1.8,
                    ease: "power2.out",
                    snap: { textContent: isFloat ? 0.1 : 1 },
                    onUpdate: function() {
                        const current = isFloat ? parseFloat(this.targets()[0].textContent).toFixed(1) : Math.round(this.targets()[0].textContent);
                        stat.innerText = prefix + current + suffix;
                    }
                }
            );
        }
    });
}

/**
 * Handles graceful skeleton loading and smooth image crossfades
 */
export function initImageLoaders() {
    const images = document.querySelectorAll('.img-lazy-load, .service-hover-image img, .gallery-item img');
    
    images.forEach(img => {
        const parent = img.parentElement;
        if (parent && !parent.classList.contains('skeleton-wrapper')) {
            parent.classList.add('skeleton-wrapper');
        }
        
        img.classList.add('img-loading');

        if (img.complete) {
            handleImageLoaded(img);
        } else {
            img.addEventListener('load', () => handleImageLoaded(img));
            img.addEventListener('error', () => handleImageError(img));
        }
    });
}

function handleImageLoaded(img) {
    img.classList.remove('img-loading');
    img.classList.add('img-loaded');
    
    const parent = img.parentElement;
    if (parent && parent.classList.contains('skeleton-wrapper')) {
        parent.classList.remove('skeleton-wrapper');
    }
}

function handleImageError(img) {
    img.classList.remove('img-loading');
    const parent = img.parentElement;
    if (parent && parent.classList.contains('skeleton-wrapper')) {
        parent.classList.remove('skeleton-wrapper');
    }
}
