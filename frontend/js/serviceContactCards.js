/**
 * OM Innoventures - Contact Cards Quick Actions (Copy / Dial)
 */

document.addEventListener('DOMContentLoaded', () => {
  initContactCardActions();
});

function initContactCardActions() {
  document.querySelectorAll('[data-copy]').forEach(el => {
    el.addEventListener('click', (e) => {
      const textToCopy = el.getAttribute('data-copy');
      if (!textToCopy) return;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast(`Copied "${textToCopy}" to clipboard!`);
      }).catch(() => {
        showToast(`Selected: ${textToCopy}`);
      });
    });
  });
}

function showToast(message) {
  let toast = document.getElementById('omToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'omToast';
    toast.style.position = 'fixed';
    toast.style.bottom = '24px';
    toast.style.right = '24px';
    toast.style.background = '#0A1F3D';
    toast.style.color = '#4FC3F7';
    toast.style.padding = '12px 20px';
    toast.style.borderRadius = '8px';
    toast.style.border = '1px solid #4FC3F7';
    toast.style.boxShadow = '0 8px 24px rgba(0,0,0,0.6)';
    toast.style.zIndex = '9999';
    toast.style.fontFamily = 'var(--font-heading)';
    toast.style.fontSize = '0.88rem';
    toast.style.transition = 'all 0.3s ease';
    document.body.appendChild(toast);
  }

  toast.textContent = message;
  toast.style.opacity = '1';
  toast.style.transform = 'translateY(0)';

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
  }, 2500);
}

window.showToast = showToast;
