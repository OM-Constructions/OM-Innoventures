document.addEventListener('DOMContentLoaded', () => {
    const viewMoreBtn = document.getElementById('view-more-btn');
    const serviceCards = document.querySelectorAll('.service-card.reveal-card');
    
    if (!viewMoreBtn || serviceCards.length === 0) return;
    
    // We already load with first 10 visible and rest hidden via inline styles (display: none)
    // Check if we even need the button initially
    let hiddenCardsCount = 0;
    serviceCards.forEach(card => {
        if (card.style.display === 'none') {
            hiddenCardsCount++;
        }
    });
    
    if (hiddenCardsCount === 0) {
        document.getElementById('view-more-container').style.display = 'none';
    }
    
    viewMoreBtn.addEventListener('click', () => {
        let revealedCount = 0;
        let remainingHiddenCount = 0;
        
        serviceCards.forEach(card => {
            if (card.style.display === 'none') {
                if (revealedCount < 10) {
                    card.style.display = ''; // Revert to natural display property
                    // Trigger reflow for animations if any
                    void card.offsetWidth;
                    revealedCount++;
                } else {
                    remainingHiddenCount++;
                }
            }
        });
        
        if (remainingHiddenCount === 0) {
            document.getElementById('view-more-container').style.display = 'none';
        }
    });
});
