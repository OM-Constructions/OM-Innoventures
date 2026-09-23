export function initServicesHover() {
  const allCards = document.querySelectorAll('.service-card');
  if (!allCards.length) return;

  allCards.forEach((card) => {
    card.addEventListener('click', (e) => {
      const isCtaClick = e.target.closest('.service-cta-btn');
      const isAlreadyActive = card.classList.contains('is-active');

      if (isCtaClick || isAlreadyActive) {
        const targetHref = card.getAttribute('href');
        if (targetHref && targetHref !== '#') {
          window.location.href = targetHref;
        }
        return;
      }

      e.preventDefault();
      allCards.forEach(c => c.classList.remove('is-active'));
      card.classList.add('is-active');
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initServicesHover();
});

window.initServicesHover = initServicesHover;


