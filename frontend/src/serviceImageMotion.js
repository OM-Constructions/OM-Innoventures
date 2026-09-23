/**
 * Service Image Motion & Card Navigation Handler
 * Ensures clean presentation and direct navigation to detailed service page on card tap.
 */

export function initServiceImageMotion() {
  const allCards = Array.from(document.querySelectorAll('.service-card'));

  allCards.forEach((card) => {
    // Reposition media below top header inside body so image pops right below title
    const media = card.querySelector('.service-card-media');
    const body = card.querySelector('.service-card-body');
    const top = card.querySelector('.service-card-top');
    
    if (media && body && top && media.parentElement === card) {
      top.insertAdjacentElement('afterend', media);
    }

    // Remove any leftover toggle buttons
    const strayToggle = card.querySelector('.service-image-toggle-pill, .service-preview-trigger, .service-card-preview-toggle');
    if (strayToggle) strayToggle.remove();

    card.style.cursor = 'pointer';
  });
}

function createMotionLightboxModal() {
  const modal = document.createElement('div');
  modal.id = 'service-motion-lightbox';
  modal.className = 'motion-lightbox-overlay';
  modal.setAttribute('aria-hidden', 'true');
  modal.innerHTML = `
    <div class="motion-lightbox-backdrop" id="motionLightboxBackdrop"></div>
    <div class="motion-lightbox-container" id="motionLightboxContainer">
      <button type="button" class="motion-lightbox-close" id="motionLightboxClose" aria-label="Close">&times;</button>
      
      <button type="button" class="motion-nav-btn motion-nav-prev" id="motionLightboxPrev" aria-label="Previous service">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>

      <button type="button" class="motion-nav-btn motion-nav-next" id="motionLightboxNext" aria-label="Next service">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>

      <div class="motion-lightbox-card" id="motionLightboxCard">
        <div class="motion-image-frame" id="motionImageFrame">
          <img id="motionLightboxImg" src="" alt="Service Preview" class="motion-img-element">
          <div class="motion-img-shimmer"></div>
          <div class="motion-img-overlay-bar">
            <span class="motion-badge-pill" id="motionLightboxBadge">⚡ OM Architecture</span>
            <span class="motion-counter-pill" id="motionLightboxCounter">01 / 37</span>
          </div>
        </div>

        <div class="motion-info-panel">
          <div class="motion-info-header">
            <div>
              <span class="motion-category-tag" id="motionLightboxCategory">Service Architecture</span>
              <h2 class="motion-service-title" id="motionLightboxTitle">Service Title</h2>
            </div>
            <div class="motion-price-tag" id="motionLightboxPrice">₹0</div>
          </div>

          <p class="motion-service-desc" id="motionLightboxDesc">Service Description</p>
          <div class="motion-tags-list" id="motionLightboxTags"></div>

          <div class="motion-actions-row">
            <a href="#" id="motionLightboxExploreBtn" class="btn-primary motion-explore-link">
              Explore Full Service &rarr;
            </a>
            <a href="#cta" id="motionLightboxConsultBtn" class="btn-outline motion-consult-link" onclick="closeMotionLightbox()">
              Request Quote
            </a>
          </div>
        </div>
      </div>
    </div>
  `;

  document.body.appendChild(modal);

  // Event Listeners
  document.getElementById('motionLightboxClose').addEventListener('click', closeMotionLightbox);
  document.getElementById('motionLightboxBackdrop').addEventListener('click', closeMotionLightbox);

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('active')) return;
    if (e.key === 'Escape') closeMotionLightbox();
    if (e.key === 'ArrowRight') navigateLightbox(1);
    if (e.key === 'ArrowLeft') navigateLightbox(-1);
  });

  document.getElementById('motionLightboxNext').addEventListener('click', () => navigateLightbox(1));
  document.getElementById('motionLightboxPrev').addEventListener('click', () => navigateLightbox(-1));

  // Interactive 3D tilt on card
  const cardEl = document.getElementById('motionLightboxCard');
  cardEl.addEventListener('mousemove', (e) => {
    const rect = cardEl.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    const rotateX = (-y / rect.height) * 8;
    const rotateY = (x / rect.width) * 8;
    cardEl.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1)`;
  });

  cardEl.addEventListener('mouseleave', () => {
    cardEl.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
  });
}

let currentIdx = 0;
let cardElements = [];

function openMotionLightbox(card, index, allCards) {
  cardElements = allCards;
  currentIdx = index >= 0 ? index : 0;

  const modal = document.getElementById('service-motion-lightbox');
  updateLightboxContent(cardElements[currentIdx]);

  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';

  const container = document.getElementById('motionLightboxContainer');
  container.classList.remove('motion-pop-in');
  void container.offsetWidth; // trigger reflow
  container.classList.add('motion-pop-in');
}

function updateLightboxContent(card) {
  if (!card) return;

  const img = card.querySelector('.service-card-media img');
  const badge = card.querySelector('.service-card-badge-overlay');
  const num = card.querySelector('.service-number');
  const title = card.querySelector('.service-title');
  const desc = card.querySelector('.service-desc');
  const price = card.querySelector('.price-value');
  const tags = card.querySelectorAll('.service-tag');
  const link = card.getAttribute('href') || '#';

  const modalImg = document.getElementById('motionLightboxImg');
  const modalBadge = document.getElementById('motionLightboxBadge');
  const modalCounter = document.getElementById('motionLightboxCounter');
  const modalTitle = document.getElementById('motionLightboxTitle');
  const modalDesc = document.getElementById('motionLightboxDesc');
  const modalPrice = document.getElementById('motionLightboxPrice');
  const modalTags = document.getElementById('motionLightboxTags');
  const modalExplore = document.getElementById('motionLightboxExploreBtn');

  // Trigger image transition animation
  modalImg.style.opacity = '0';
  modalImg.style.transform = 'scale(0.95)';
  setTimeout(() => {
    modalImg.src = img ? img.src : '';
    modalImg.alt = title ? title.textContent : 'Service Image';
    modalImg.style.opacity = '1';
    modalImg.style.transform = 'scale(1)';
  }, 100);

  modalBadge.textContent = badge ? badge.textContent.trim() : '⚡ Verified Architecture';
  modalCounter.textContent = `${(currentIdx + 1).toString().padStart(2, '0')} / ${cardElements.length.toString().padStart(2, '0')}`;
  modalTitle.textContent = title ? title.textContent.trim() : 'Service';
  modalDesc.textContent = desc ? desc.textContent.trim() : '';
  modalPrice.textContent = price ? price.textContent.trim() : '';
  modalExplore.href = link;

  modalTags.innerHTML = '';
  tags.forEach(t => {
    const span = document.createElement('span');
    span.className = 'motion-tag-pill';
    span.innerHTML = t.innerHTML;
    modalTags.appendChild(span);
  });
}

function navigateLightbox(direction) {
  if (!cardElements || cardElements.length === 0) return;
  currentIdx = (currentIdx + direction + cardElements.length) % cardElements.length;
  updateLightboxContent(cardElements[currentIdx]);
}

export function closeMotionLightbox() {
  const modal = document.getElementById('service-motion-lightbox');
  if (!modal) return;
  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

window.initServiceImageMotion = initServiceImageMotion;
window.closeMotionLightbox = closeMotionLightbox;

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initServiceImageMotion);
  } else {
    initServiceImageMotion();
  }
}
