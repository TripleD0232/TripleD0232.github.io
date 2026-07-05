/**
 * Scroll-triggered fade-in animations using IntersectionObserver.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Fade-in sections on scroll
  const fadeSections = document.querySelectorAll('.fade-section');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px',
      }
    );

    fadeSections.forEach((section) => observer.observe(section));
  } else {
    // Fallback: show everything immediately
    fadeSections.forEach((section) => section.classList.add('visible'));
  }

  // Active nav highlighting on scroll
  const navLinks = document.querySelectorAll('.sidebar-nav a');
  const sections = document.querySelectorAll('.section[id]');

  if (sections.length > 0 && navLinks.length > 0) {
    const navObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            navLinks.forEach((link) => link.classList.remove('active'));
            const activeLink = document.querySelector(
              `.sidebar-nav a[href="#${entry.target.id}"]`
            );
            if (activeLink) activeLink.classList.add('active');
          }
        });
      },
      {
        threshold: 0.3,
      }
    );

    sections.forEach((section) => navObserver.observe(section));
  }
});
