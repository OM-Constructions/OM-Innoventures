/**
 * OM Innoventures & Build AI Technologies - Brand Logo Generator
 * Renders circular AI/circuit icon mark with navy ring, cyan circuit motif, and gold accent
 */

function renderBrandLogoMark(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const svg = `
    <svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Outer Navy Ring -->
      <circle cx="22" cy="22" r="20" stroke="#164075" stroke-width="2.5" fill="#0A1F3D"/>
      <circle cx="22" cy="22" r="16.5" stroke="#4FC3F7" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="2 3"/>
      
      <!-- Circuit Nodes and Traces -->
      <!-- Center Core Node -->
      <circle cx="22" cy="22" r="3.5" fill="#4FC3F7" />
      
      <!-- Top Trace to Gold Accent Node -->
      <line x1="22" y1="18.5" x2="22" y2="10" stroke="#4FC3F7" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="22" cy="10" r="2" fill="#C9A34E" />

      <!-- Bottom Left Branch -->
      <path d="M19 24.5L14 29.5H10" stroke="#4FC3F7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="9.5" cy="29.5" r="2" fill="#4FC3F7" />

      <!-- Bottom Right Branch -->
      <path d="M25 24.5L30 29.5H34" stroke="#4FC3F7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="34.5" cy="29.5" r="2" fill="#4FC3F7" />

      <!-- Left Horizontal Micro Trace -->
      <line x1="18.5" y1="22" x2="12" y2="22" stroke="#4FC3F7" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="12" cy="22" r="1.5" fill="#4FC3F7" />

      <!-- Right Horizontal Micro Trace -->
      <line x1="25.5" y1="22" x2="32" y2="22" stroke="#4FC3F7" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="32" cy="22" r="1.5" fill="#4FC3F7" />
    </svg>
  `;

  container.innerHTML = svg;
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.nav-logo-mark').forEach(el => {
    renderBrandLogoMark(el.id || (el.id = 'logoMark_' + Math.random().toString(36).substr(2, 5)));
  });
});

window.renderBrandLogoMark = renderBrandLogoMark;
