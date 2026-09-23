document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initMetricsAnimation();
});

function initScrollReveal() {
  const revealElements = document.querySelectorAll(
    '.service-card, .capability-card, .industry-card, .work-card, .value-card, .why-tile, .founder-card, .enquiry-form-card, .contact-card-box, .section-header, .metrics-strip-card'
  );

  revealElements.forEach((el, index) => {
    el.classList.add('reveal');
    const delay = (index % 4) + 1;
    el.classList.add(`reveal-delay-${delay}`);
  });

  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.12
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        obs.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => observer.observe(el));
}

function initMetricsAnimation() {
  const metricsSection = document.getElementById('metrics-strip');
  if (!metricsSection) return;

  let hasAnimated = false;

  function isElementInViewport(el) {
    // Check if homepage container is visible (intro-splash complete)
    const hp = document.getElementById('homepage-content');
    if (hp) {
      const style = window.getComputedStyle(hp);
      if (style.visibility === 'hidden' || parseFloat(style.opacity || '1') < 0.2) {
        return false;
      }
    }

    const rect = el.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;

    // Trigger only when user scrolls so that section top is well within viewport (85% from top)
    return rect.top <= windowHeight * 0.85 && rect.bottom >= 50;
  }

  function handleCheck() {
    if (hasAnimated) return;
    if (isElementInViewport(metricsSection)) {
      hasAnimated = true;
      cleanup();
      animateAllCounters();
    }
  }

  function cleanup() {
    window.removeEventListener('scroll', handleCheck);
    window.removeEventListener('resize', handleCheck);
    if (observer) {
      observer.disconnect();
    }
  }

  let observer = null;
  if ('IntersectionObserver' in window) {
    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && isElementInViewport(metricsSection)) {
          hasAnimated = true;
          cleanup();
          animateAllCounters();
        }
      });
    }, {
      root: null,
      threshold: [0.1, 0.25, 0.5]
    });
    observer.observe(metricsSection);
  }

  // Active scroll and resize listeners ensure it triggers reliably when user reaches section
  window.addEventListener('scroll', handleCheck, { passive: true });
  window.addEventListener('resize', handleCheck, { passive: true });

  // Do not animate on load if section is off-screen. Only run if already in view.
  setTimeout(handleCheck, 600);
}

function animateAllCounters() {
  // Show pop items
  const popItems = document.querySelectorAll('.metric-pop-item');
  popItems.forEach(item => {
    item.classList.add('popped');
  });

  // Smoothly fill progress bars
  const bars = document.querySelectorAll('.metric-pop-bar-fill, .metric-bar-fill');
  bars.forEach(bar => {
    const targetWidth = bar.getAttribute('data-fill') || '100%';
    bar.style.width = targetWidth;
  });

  // Clean, simple and smooth count-up animation (no random scramble/jitter)
  const counters = document.querySelectorAll('.counter-scramble');
  counters.forEach(counter => {
    const target = parseFloat(counter.getAttribute('data-target') || '0');
    const decimals = parseInt(counter.getAttribute('data-decimals') || '0', 10);
    const suffix = counter.getAttribute('data-suffix') || '';
    
    const duration = 1600; // 1.6s smooth duration
    const startTime = performance.now();

    function updateCounter(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Smooth ease-out quad
      const easeProgress = 1 - (1 - progress) * (1 - progress);
      const currentVal = target * easeProgress;

      counter.textContent = currentVal.toFixed(decimals) + suffix;

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        counter.textContent = target.toFixed(decimals) + suffix;
      }
    }

    requestAnimationFrame(updateCounter);
  });
}

window.initScrollReveal = initScrollReveal;
window.initMetricsAnimation = initMetricsAnimation;


