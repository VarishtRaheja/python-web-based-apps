// site.js

function showFlash(message, category = 'info', timeout = 3000) {
  const container = document.getElementById('flash-container');
  if (!container) return;

  const alertDiv = document.createElement('div');
  alertDiv.className = `alert alert-${category}`;
  alertDiv.textContent = message;
  container.appendChild(alertDiv);

  setTimeout(() => alertDiv.remove(), timeout);
}

document.addEventListener('DOMContentLoaded', () => {
  const shopBtn = document.getElementById('shopNow');
  const marketUrl = shopBtn.dataset.marketUrl;
  if (!shopBtn) return;

  shopBtn.addEventListener('click', (e) => {
    if (!isLoggedIn) {
      e.preventDefault();
      showFlash('You need to login before viewing the market', 'warning', 4000);
    }

    if(window.isLoggedIn == 'true'){
      window.location.href = marketUrl;
    }
  });
});