/* ===== Kushi Educational Consultancy – site script ===== */
(function () {
  'use strict';

  var PHONE_1 = '7989192236';
  var PHONE_2 = '7036672236';
  var WA_NUMBER = '917989192236'; // India country code + primary number

  /* ---------- Icon set (24x24, stroke based) ---------- */
  var P = {
    phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    pin: '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    checkc: '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
    star: '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
    cap: '<path d="M22 9 12 4 2 9l10 5 10-5z"/><path d="M6 11.5V16c0 1.5 2.7 3 6 3s6-1.5 6-3v-4.5"/><path d="M22 9v6"/>',
    book: '<path d="M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7z"/>',
    users: '<circle cx="9" cy="8" r="3.5"/><path d="M2 21v-1a6 6 0 0 1 6-6h2a6 6 0 0 1 6 6v1"/><circle cx="17.5" cy="9" r="2.5"/><path d="M18 14.2a5 5 0 0 1 4 4.8V21"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 7-7h2a7 7 0 0 1 7 7v1"/>',
    laptop: '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/>',
    doc: '<path d="M14 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7z"/><path d="M14 2v5h5M9 13h6M9 17h6"/>',
    shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    rupee: '<path d="M6 4h12M6 9h12M6 4c6 0 8 2.5 8 5s-2.5 5-8 5l8 6"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    brief: '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    plane: '<path d="M17.8 19.2 16 11l3.5-3.5A2.1 2.1 0 0 0 16.5 4.5L13 8 4.8 6.2l-1.4 1.4 6.3 3.3-3.4 3.4-3-.4-1 1 4 2 2 4 1-1-.4-3 3.4-3.4 3.3 6.3z"/>',
    bank: '<path d="m3 9 9-6 9 6"/><path d="M5 9v9M9.5 9v9M14.5 9v9M19 9v9M3 21h18M2 9h20"/>',
    headset: '<path d="M3 14v-2a9 9 0 0 1 18 0v2"/><rect x="2" y="14" width="5" height="7" rx="2"/><rect x="17" y="14" width="5" height="7" rx="2"/><path d="M19.5 21a4 4 0 0 1-4 2H13"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    menu: '<path d="M4 6h16M4 12h16M4 18h16"/>',
    close: '<path d="M18 6 6 18M6 6l12 12"/>',
    award: '<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 8 5-3 5 3-1.5-8"/>',
    target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    compass: '<circle cx="12" cy="12" r="10"/><path d="m16 8-2 6-6 2 2-6z"/>',
    chart: '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
    mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    send: '<path d="m22 2-11 11M22 2l-7 20-4-9-9-4z"/>',
    trophy: '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
    handshake: '<path d="m11 17 2 2a1.4 1.4 0 0 0 2-2"/><path d="m14 14 2.5 2.5a1.4 1.4 0 0 0 2-2l-3.8-3.8a2.8 2.8 0 0 0-4 0l-.7.7a1.4 1.4 0 0 1-2 0 1.4 1.4 0 0 1 0-2L10 6a5.7 5.7 0 0 1 4-1.5c1.3 0 2.5.5 3.5 1.5l3 3"/><path d="m3 11 2-2 5 5M2 12l5 5a1.4 1.4 0 0 0 2-2"/>',
    building: '<rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 22v-4h6v4M8 6h2M14 6h2M8 10h2M14 10h2M8 14h2M14 14h2"/>',
    steps: '<path d="M4 20h4v-4h4v-4h4V8h4"/><path d="M16 4h4v4"/>',
    arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
    clip: '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3h6v3H9zM9 12l2 2 4-4M9 17h6"/>'
  };
  var WA = '<path fill="currentColor" stroke="none" d="M12.04 2A9.9 9.9 0 0 0 3.5 17l-1.4 5 5.1-1.3A9.9 9.9 0 1 0 12.04 2zm5.8 14c-.25.7-1.4 1.35-1.95 1.4-.5.05-1.1.2-3.7-.8-3.1-1.2-5.1-4.4-5.3-4.6-.15-.2-1.25-1.7-1.25-3.2s.8-2.3 1.1-2.6c.3-.3.6-.4.8-.4h.6c.2 0 .45-.05.7.55.25.6.85 2.1.9 2.25.1.15.1.3 0 .5-.1.2-.15.3-.3.5l-.45.5c-.15.15-.3.3-.15.6.15.3.7 1.15 1.5 1.85 1 .9 1.9 1.2 2.2 1.35.3.15.45.1.6-.05.2-.2.7-.8.9-1.1.2-.3.4-.25.65-.15.25.1 1.65.8 1.95.95.3.15.5.2.55.3.1.1.1.65-.15 1.35z"/>';

  function svg(name) {
    if (name === 'wa') return '<svg viewBox="0 0 24 24" aria-hidden="true">' + WA + '</svg>';
    var body = P[name] || P.check;
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + body + '</svg>';
  }
  function paintIcons(root) {
    (root || document).querySelectorAll('[data-icon]').forEach(function (el) {
      if (el.dataset.painted) return;
      el.innerHTML = svg(el.dataset.icon);
      el.dataset.painted = '1';
    });
  }

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.innerHTML = svg(open ? 'close' : 'menu');
      toggle.firstChild.style.cssText = 'width:28px;height:28px';
    });
  }

  /* ---------- Course explorer (home page) ---------- */
  var COURSES = {
    UG: [
      ['BA English', 'Arts'], ['BA History', 'Arts'], ['BA Economics', 'Arts'],
      ['BA Political Science', 'Arts'], ['BA Public Administration', 'Arts'],
      ['B.Com General', 'Commerce & Management'], ['B.Com Banking & Management', 'Commerce & Management'],
      ['BBA', 'Commerce & Management'],
      ['BCA', 'Computers & Library'], ['BLIS', 'Computers & Library'],
      ['B.Sc Chemistry', 'Science'], ['B.Sc Botany', 'Science'], ['B.Sc Physics', 'Science'],
      ['B.Sc Zoology', 'Science'], ['B.Sc Mathematics', 'Science'],
      ['B.Sc Computer Science', 'Computers & Library'], ['B.Sc IT', 'Computers & Library'],
      ['B.Sc Geography', 'Science']
    ],
    PG: [
      ['MA English', 'Arts'], ['MA History', 'Arts'], ['MA Economics', 'Arts'],
      ['MA Political Science', 'Arts'], ['MA Public Administration', 'Arts'],
      ['MA (HRM)', 'Commerce & Management'],
      ['M.Com General', 'Commerce & Management'], ['M.Com Banking & Management', 'Commerce & Management'],
      ['M.Com Financial Management', 'Commerce & Management'], ['MBA', 'Commerce & Management'],
      ['MCA', 'Computers & Library'], ['MLIS', 'Computers & Library'],
      ['M.Sc Chemistry', 'Science'], ['M.Sc Botany', 'Science'], ['M.Sc Physics', 'Science'],
      ['M.Sc Zoology', 'Science'], ['M.Sc Mathematics', 'Science'],
      ['M.Sc Computer Science', 'Computers & Library'], ['M.Sc IT', 'Computers & Library'],
      ['M.Sc Geography', 'Science']
    ]
  };
  var CAT_ICON = { 'Arts': 'book', 'Commerce & Management': 'chart', 'Computers & Library': 'laptop', 'Science': 'target' };
  var grid = document.getElementById('courseGrid');
  if (grid) {
    var state = { level: 'UG', cat: 'All', q: '' };
    var chipsEl = document.getElementById('courseChips');
    var cats = ['All', 'Arts', 'Commerce & Management', 'Science', 'Computers & Library'];
    chipsEl.innerHTML = cats.map(function (c) {
      return '<button type="button" class="chip' + (c === 'All' ? ' active' : '') + '" data-cat="' + c + '">' + c + '</button>';
    }).join('');

    var render = function () {
      var color = state.level === 'UG' ? 'var(--green)' : '#a0174d';
      var list = COURSES[state.level].filter(function (c) {
        return (state.cat === 'All' || c[1] === state.cat) && c[0].toLowerCase().indexOf(state.q) !== -1;
      });
      grid.style.setProperty('--lc', color);
      grid.innerHTML = list.length ? list.map(function (c) {
        return '<div class="course"><span class="dot icon-box">' + svg(CAT_ICON[c[1]]).replace('<svg', '<svg width="20" height="20"') + '</span><div>' + c[0] + '<small>' + c[1] + '</small></div></div>';
      }).join('') : '<p class="empty">No matching course found. Call us – we may still be able to help!</p>';
      var count = document.getElementById('courseCount');
      if (count) count.textContent = list.length + ' ' + state.level + ' course' + (list.length === 1 ? '' : 's');
    };

    document.querySelectorAll('.tab').forEach(function (t) {
      t.addEventListener('click', function () {
        document.querySelectorAll('.tab').forEach(function (x) { x.classList.remove('active'); x.setAttribute('aria-selected', 'false'); });
        t.classList.add('active'); t.setAttribute('aria-selected', 'true');
        state.level = t.dataset.level; render();
      });
    });
    chipsEl.addEventListener('click', function (e) {
      var b = e.target.closest('.chip'); if (!b) return;
      chipsEl.querySelectorAll('.chip').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active'); state.cat = b.dataset.cat; render();
    });
    document.getElementById('courseSearch').addEventListener('input', function (e) {
      state.q = e.target.value.trim().toLowerCase(); render();
    });
    render();
  }

  /* ---------- Lightbox ---------- */
  var lb = document.getElementById('lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    document.querySelectorAll('.gallery figure').forEach(function (f) {
      f.addEventListener('click', function () {
        var im = f.querySelector('img'); lbImg.src = im.src; lbImg.alt = im.alt; lb.classList.add('open');
      });
    });
    lb.addEventListener('click', function () { lb.classList.remove('open'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('open'); });
  }

  /* ---------- Enquiry form -> WhatsApp ---------- */
  var form = document.getElementById('enquiryForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var phone = String(d.get('phone') || '').replace(/\D/g, '');
      if (phone.length < 10) {
        var m = document.getElementById('formMsg');
        m.style.display = 'block'; m.style.color = 'var(--red)';
        m.textContent = 'Please enter a valid 10-digit mobile number.';
        return;
      }
      var lines = [
        'Hello Kushi Educational Consultancy,',
        'I would like to enquire about admissions (2026-27).',
        '',
        'Name: ' + d.get('name'),
        'Mobile: ' + d.get('phone'),
        'Interested in: ' + d.get('course'),
        'Qualification: ' + (d.get('qualification') || '-'),
        'Message: ' + (d.get('message') || '-')
      ];
      var url = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(lines.join('\n'));
      var msg = document.getElementById('formMsg');
      msg.style.display = 'block'; msg.style.color = 'var(--green)';
      msg.textContent = 'Thank you! Opening WhatsApp so you can send your enquiry to our team…';
      window.open(url, '_blank', 'noopener');
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: .12 });
    items.forEach(function (el) { io.observe(el); });
  } else { items.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- Year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  paintIcons();
})();
