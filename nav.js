// Mobile hamburger toggle
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

hamburger.addEventListener('click', (e) => {
  e.stopPropagation();
  navLinks.classList.toggle('open');
  // Prevent body scroll when menu is open
  document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : 'auto';
});

// Close nav when a link is clicked on mobile
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    document.body.style.overflow = 'auto';
  });
});

// Close nav when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.navbar')) {
    if (navLinks.classList.contains('open')) {
      navLinks.classList.remove('open');
      document.body.style.overflow = 'auto';
    }
  }
});

// Disable menu on window resize to desktop
window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
    navLinks.classList.remove('open');
    document.body.style.overflow = 'auto';
  }
});
