export function initServicesHover() {
    const allCards = document.querySelectorAll('.service-card');
    if (!allCards.length) return;

    allCards.forEach((card) => {
        // Show image on mouse hover
        card.addEventListener('mouseenter', () => {
            allCards.forEach(c => c.classList.remove('is-active'));
            card.classList.add('is-active');
        });

        // Hide image when mouse leaves
        card.addEventListener('mouseleave', () => {
            card.classList.remove('is-active');
        });
    });
}



