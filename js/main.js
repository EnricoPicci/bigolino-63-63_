/**
 * 63-63 Party Website
 * Language toggle, lightbox gallery, and political spectrum animation.
 */

(function () {
    'use strict';

    // =====================
    // Language Toggle
    // =====================
    var langButtons = document.querySelectorAll('.lang-btn');
    var contentIt = document.querySelectorAll('.content-it');
    var contentEn = document.querySelectorAll('.content-en');

    function setLanguage(lang) {
        langButtons.forEach(function (btn) {
            btn.classList.toggle('active', btn.dataset.lang === lang);
        });
        contentIt.forEach(function (el) { el.hidden = lang !== 'it'; });
        contentEn.forEach(function (el) { el.hidden = lang !== 'en'; });
        document.documentElement.lang = lang;

        try { localStorage.setItem('63-63-lang', lang); } catch (e) { /* ignore */ }
    }

    langButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            setLanguage(this.dataset.lang);
        });
    });

    // Restore saved language preference
    try {
        var saved = localStorage.getItem('63-63-lang');
        if (saved === 'en') setLanguage('en');
    } catch (e) { /* ignore */ }

    // =====================
    // Lightbox Gallery
    // =====================
    var lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.innerHTML = '<button class="lightbox-close" aria-label="Close">&times;</button><img src="" alt="">';
    document.body.appendChild(lightbox);

    var lightboxImg = lightbox.querySelector('img');

    document.querySelectorAll('.gallery-item img').forEach(function (img) {
        img.addEventListener('click', function () {
            lightboxImg.src = this.src;
            lightboxImg.alt = this.alt;
            lightbox.classList.add('active');
        });
    });

    lightbox.addEventListener('click', function () {
        lightbox.classList.remove('active');
        lightboxImg.src = '';
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            lightbox.classList.remove('active');
            lightboxImg.src = '';
        }
    });

    // =====================
    // RSVP Reveal
    // =====================
    var rsvpBtn = document.getElementById('rsvp-cta');
    var rsvpSection = document.getElementById('rsvp');

    if (rsvpBtn && rsvpSection) {
        rsvpBtn.addEventListener('click', function () {
            rsvpSection.hidden = false;
            rsvpSection.scrollIntoView({ behavior: 'smooth' });
            rsvpBtn.classList.add('btn-rsvp-cta--active');
        });
    }

    // Hide RSVP section after Google Form submission
    var rsvpIframe = document.getElementById('rsvp-iframe');
    if (rsvpIframe && rsvpSection) {
        var iframeLoadCount = 0;
        rsvpIframe.addEventListener('load', function () {
            iframeLoadCount++;
            // First load is the initial page load; subsequent loads mean form submission
            if (iframeLoadCount > 1) {
                setTimeout(function () {
                    rsvpSection.hidden = true;
                    if (rsvpBtn) {
                        rsvpBtn.textContent = document.documentElement.lang === 'en'
                            ? 'Thank you!' : 'Grazie!';
                        rsvpBtn.disabled = true;
                    }
                }, 3000);
            }
        });
    }

    // =====================
    // Hash-based Page Routing
    // =====================
    var mainContent = document.getElementById('main-content');
    var tombaPage = document.getElementById('tomba-brion-page');

    function showPage(hash) {
        if (hash === '#tomba-brion' && mainContent && tombaPage) {
            mainContent.hidden = true;
            tombaPage.hidden = false;
            window.scrollTo(0, 0);
        }
    }

    function showMain() {
        if (mainContent && tombaPage) {
            tombaPage.hidden = true;
            mainContent.hidden = false;
            history.replaceState(null, '', window.location.pathname);
        }
    }

    // Back link click
    document.querySelectorAll('.back-link').forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            showMain();
        });
    });

    // Browser back/forward
    window.addEventListener('hashchange', function () {
        if (window.location.hash === '#tomba-brion') {
            showPage('#tomba-brion');
        } else {
            showMain();
        }
    });

    // Initial hash check (direct link support)
    if (window.location.hash === '#tomba-brion') {
        showPage('#tomba-brion');
    }

    // =====================
    // Music Player
    // =====================
    var musicBtn = document.getElementById('music-btn');
    var musicPlayer = document.getElementById('music-player');

    var musicLabel = document.getElementById('music-label');

    if (musicLabel && musicBtn) {
        musicLabel.style.cursor = 'pointer';
        musicLabel.addEventListener('click', function () {
            musicBtn.click();
        });
    }

    if (musicBtn && musicPlayer) {
        musicBtn.addEventListener('click', function () {
            if (musicPlayer.paused) {
                musicPlayer.play();
                musicBtn.classList.add('playing');
                musicBtn.setAttribute('aria-label', 'Pause music');
            } else {
                musicPlayer.pause();
                musicBtn.classList.remove('playing');
                musicBtn.setAttribute('aria-label', 'Play music');
            }
        });
    }
})();
