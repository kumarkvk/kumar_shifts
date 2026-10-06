#!/usr/bin/env python3
"""Generates index.html, services.html and contact.html with shared header/footer."""
from pathlib import Path

ROOT = Path(__file__).parent
P1, P2 = "7989192236", "7036672236"
ADDR = "Vakalapudi, Kakinada, Andhra Pradesh – 533005"


def ic(name, cls="icon"):
    return f'<span class="{cls}" data-icon="{name}"></span>'


def head(title, desc, active):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0f2457">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<div class="topbar">
  <div class="container">
    <div class="group">
      <a href="tel:+91{P1}">{ic('phone')} {P1}</a>
      <a href="tel:+91{P2}">{ic('phone')} {P2}</a>
    </div>
    <div class="group right">
      <span>{ic('pin')} Vakalapudi, Kakinada, Andhra Pradesh – 533005</span>
      <span class="accent">Admissions Open 2026-27</span>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Kushi Educational Consultancy – Home">
      <img src="images/logo-mark.png" alt="Kushi Educational Consultancy logo">
      <span class="brand-text"><strong>KUSHI</strong><small>Educational Consultancy</small></span>
    </a>
    <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">{ic('menu')}</button>
    <nav class="nav" aria-label="Main">
      <a href="index.html"{' class="active"' if active == 'home' else ''}>Home</a>
      <a href="services.html"{' class="active"' if active == 'services' else ''}>Our Services</a>
      <a href="contact.html"{' class="active"' if active == 'contact' else ''}>Contact Us</a>
      <a class="nav-cta" href="tel:+91{P1}">{ic('phone')} {P1}</a>
    </nav>
  </div>
</header>
"""


def foot():
    return f"""
<footer>
  <div class="container foot-grid">
    <div>
      <a class="brand" href="index.html">
        <img src="images/logo-mark.png" alt="Kushi logo" style="background:#fff;border-radius:12px;padding:4px">
        <span class="brand-text"><strong>KUSHI</strong><small>Educational Consultancy</small></span>
      </a>
      <p>Quality Education… Bright Future… Expert guidance for admissions, distance education and career planning.</p>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="index.html#courses">UG &amp; PG Courses</a></li>
        <li><a href="services.html">Our Services</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Get in Touch</h4>
      <ul class="foot-contact">
        <li>{ic('phone')}<span><a href="tel:+91{P1}">{P1}</a><br><a href="tel:+91{P2}">{P2}</a></span></li>
        <li>{ic('pin')}<span>{ADDR}</span></li>
        <li>{ic('user')}<span>Director: Hemanth Thommandra</span></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <div class="container">
      <b>YOUR DREAM | OUR GUIDANCE | YOUR SUCCESS</b><br>
      © <span data-year>2026</span> Kushi Educational Consultancy. All rights reserved.
    </div>
  </div>
</footer>

<div class="fab">
  <a class="wa" href="https://wa.me/91{P1}?text=Hello%20Kushi%20Educational%20Consultancy%2C%20I%20would%20like%20to%20know%20more%20about%20admissions." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ic('wa')}</a>
  <a class="call" href="tel:+91{P1}" aria-label="Call now">{ic('phone')}</a>
</div>

<script src="js/main.js"></script>
</body>
</html>
"""


def cta():
    return f"""
<div class="cta">
  <div class="container">
    <div>
      <h2>Your Dream Degree is Just a Call Away!</h2>
      <p>Talk to our counsellors today and take the first step.</p>
    </div>
    <div class="num">
      <span class="ic">{ic('phone')}</span>
      <div><small>Contact Us</small><a href="tel:+91{P1}">{P1}</a></div>
    </div>
  </div>
</div>
"""


# ------------------------------------------------------------------ HOME
def home():
    adm = [
        ("10th", "Open", "10th Admissions", "SSC (10th) admissions for learners who wish to continue their education.", "var(--green)", "users"),
        ("Intermediate", "Open", "Intermediate", "Intermediate (10+2) admissions with expert guidance on the right group.", "#e8731a", "book"),
        ("Degree", "Open", "Degree", "UG degree admissions in BA, B.Com, B.Sc, BBA, BCA and BLIS.", "#1565c0", "cap"),
        ("PG", "Open", "Post Graduation", "PG admissions in MA, M.Com, M.Sc, MBA, MCA and MLIS.", "#6a2c91", "award"),
    ]
    adm_html = "\n".join(
        f"""<div class="adm-card reveal" style="--c:{c}"><div class="ic">{ic(i)}</div><small>{o} Admissions</small><h3>{t}</h3><p>{d}</p></div>"""
        for _, o, t, d, c, i in adm
    )
    fac = [
        ("APOSS Admissions", "10th (SSC) & Intermediate", "#1f7a3a", "book"),
        ("Degree Admissions", "All Recognized Universities", "#173172", "cap"),
        ("PG Admissions", "MBA, MCA, M.Com., MA, MSc & More", "#6a2c91", "users"),
        ("Engineering Admissions", "in India Deemed Universities", "#e8731a", "building"),
        ("Distance Education", "UG, PG & Diploma Courses", "#0e8fb0", "laptop"),
        ("Career Guidance", "Choose the Right Path for Your Future", "#d81b7a", "steps"),
        ("Scholarship Guidance", "Find & Apply for Best Scholarships", "#d99a00", "award"),
        ("Internship Support", "Opportunities in Top Companies", "#1f7a3a", "brief"),
        ("Documentation Support", "Guidance for all Documents", "#173172", "doc"),
        ("Education Loan Assistance", "Easy Loan Process Support", "#c8102e", "rupee"),
        ("Exam Registration Assistance", "Forms, Hall Tickets, Results & More", "#7a3b12", "clip"),
        ("Student Counselling", "Personal Guidance & Support", "#6a2c91", "headset"),
    ]
    fac_html = "\n".join(
        f"""<div class="fac reveal" style="--c:{c}"><div class="ic">{ic(i)}</div><div><h4>{t.replace('&','&amp;')}</h4><p>{d.replace('&','&amp;')}</p></div></div>"""
        for t, d, c, i in fac
    )
    return head(
        "Kushi Educational Consultancy | Online & Distance Education, Kakinada",
        "Kushi Educational Consultancy, Kakinada – admissions for 10th, Intermediate, Degree and PG. UGC/DEB approved online & distance education, expert guidance.",
        "home",
    ) + f"""
<section class="hero" style="padding:0">
  <div class="container">
    <div>
      <span class="pill">{ic('star')} Admissions Open 2026-27</span>
      <h1>Online &amp; Distance <span>Education</span> for a Bright Future</h1>
      <p class="lead">UG, PG &amp; other courses from recognised universities – with personalised counselling, exam &amp; assignment support and 100% online assistance, right from Kakinada.</p>
      <p class="tagline">“Quality Education… Bright Future…”</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="contact.html">Enquire Now {ic('arrow')}</a>
        <a class="btn btn-outline" href="tel:+91{P1}">{ic('phone')} {P1}</a>
        <a class="btn btn-outline" href="#courses">Explore Courses</a>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-photo"><img src="images/student.jpg" alt="Smiling student holding books"></div>
      <div class="float-badge fb-1"><span class="ic">{ic('shield')}</span><div>UGC / DEB<small>Approved</small></div></div>
      <div class="float-badge fb-2"><span class="ic">{ic('cap')}</span><div>Admissions Open<small>2026-27</small></div></div>
    </div>
  </div>
</section>

<div class="container strip">
  <div class="strip-grid">
    <div class="strip-item"><span class="ic">{ic('user')}</span><div><b>Expert</b><span>Guidance</span></div></div>
    <div class="strip-item"><span class="ic">{ic('book')}</span><div><b>UG &amp; PG</b><span>Courses</span></div></div>
    <div class="strip-item"><span class="ic">{ic('laptop')}</span><div><b>100%</b><span>Online Support</span></div></div>
    <div class="strip-item"><span class="ic">{ic('doc')}</span><div><b>UGC / DEB</b><span>Approved</span></div></div>
  </div>
</div>

<section id="admissions">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Admissions Open</span>
      <h2>Start Your Journey at Any Level</h2>
      <div class="divider"></div>
      <p>From 10th to Post Graduation – regular and distance modes with an easy admission process.</p>
    </div>
    <div class="adm-grid">
{adm_html}
    </div>
  </div>
</section>

<section id="courses" class="bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Courses</span>
      <h2>Explore UG &amp; PG Programmes</h2>
      <div class="divider"></div>
      <p>Choose from a wide range of Arts, Commerce, Management, Science and Computer courses.</p>
    </div>
    <div class="course-tabs" role="tablist">
      <button class="tab active" data-level="UG" role="tab" aria-selected="true">UG (Degree) Courses</button>
      <button class="tab" data-level="PG" role="tab" aria-selected="false">PG Courses</button>
    </div>
    <div class="course-tools">
      <div class="search">{ic('search')}<label class="sr-only" for="courseSearch">Search courses</label><input id="courseSearch" type="search" placeholder="Search a course, e.g. MBA"></div>
    </div>
    <div class="chips" id="courseChips" style="margin-bottom:1.8rem"></div>
    <p class="note" style="margin:-.6rem 0 1.4rem"><strong id="courseCount"></strong></p>
    <div class="course-grid" id="courseGrid"></div>
    <p class="note">Not sure which course suits you? <a href="contact.html">Talk to a counsellor</a> or call <a href="tel:+91{P1}">{P1}</a>.</p>
  </div>
</section>

<section>
  <div class="container split">
    <div class="panel reveal">
      <h3><span class="ic">{ic('check')}</span> Why Choose Us?</h3>
      <ul class="tick star">
        <li>{ic('star')} Personalized Counseling</li>
        <li>{ic('star')} Wide Range of Courses</li>
        <li>{ic('star')} Flexible Learning Options</li>
        <li>{ic('star')} Exam &amp; Assignment Support</li>
        <li>{ic('star')} 100% Student Satisfaction</li>
      </ul>
      <br>
      <ul class="tick">
        <li>{ic('checkc')} Regular &amp; Distance Mode</li>
        <li>{ic('checkc')} Recognized Universities</li>
        <li>{ic('checkc')} Affordable Fees</li>
        <li>{ic('checkc')} Easy Admission Process</li>
        <li>{ic('checkc')} Student Support &amp; Guidance</li>
      </ul>
    </div>
    <div class="panel reveal">
      <h3><span class="ic">{ic('users')}</span> Who Can Join?</h3>
      <ul class="tick cap">
        <li>{ic('cap')} After 10th / Intermediate</li>
        <li>{ic('cap')} Working Professionals</li>
        <li>{ic('cap')} Job Aspirants</li>
        <li>{ic('cap')} Housewives</li>
        <li>{ic('cap')} Anyone Who Wants to Build Their Career</li>
      </ul>
      <div style="margin-top:1.6rem;display:flex;gap:.8rem;flex-wrap:wrap">
        <a class="btn btn-primary" href="contact.html">Apply Now</a>
        <a class="btn btn-outline-dark" href="services.html">Our Services</a>
      </div>
    </div>
  </div>
</section>

<section class="quote">
  <div class="container reveal">
    <h2>LEARN TODAY, LEAD TOMORROW</h2>
    <p>Take the first step towards a successful career with Kushi Educational Consultancy.</p>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">All Facilities</span>
      <h2>Everything You Need Under One Roof</h2>
      <div class="divider"></div>
      <p>Building bright futures through education – with expert guidance, trusted support and your success as our mission.</p>
    </div>
    <div class="fac-grid">
{fac_html}
    </div>
    <p class="note"><a href="services.html">View all our services →</a></p>
  </div>
</section>

<section id="brochures">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Brochures</span>
      <h2>Take a Look at Our Brochures</h2>
      <div class="divider"></div>
      <p>Tap any brochure to view it full size.</p>
    </div>
    <div class="gallery">
      <figure class="reveal"><img src="images/poster-courses.jpg" alt="Online and Distance Education brochure with UG and PG course list"><figcaption>Courses Brochure <span>Tap to enlarge</span></figcaption></figure>
      <figure class="reveal"><img src="images/poster-services.jpg" alt="Our Services brochure"><figcaption>Our Services <span>Tap to enlarge</span></figcaption></figure>
      <figure class="reveal"><img src="images/banner-facilities.jpg" alt="All Facilities banner – Admissions Open 2026-27"><figcaption>All Facilities 2026-27 <span>Tap to enlarge</span></figcaption></figure>
    </div>
  </div>
</section>

{cta()}

<div class="lightbox" id="lightbox" role="dialog" aria-label="Brochure preview"><button aria-label="Close">✕</button><img src="" alt=""></div>
""" + foot()


# ------------------------------------------------------------------ SERVICES
def services():
    svc = [
        ("Admissions", "var(--navy)", "cap", ["SSC (10th)", "Intermediate (10+2)", "Degree (UG)", "Post Graduation (PG)"], None),
        ("Distance Education", "var(--green)", "globe", ["UGC-Recognized Universities", "Flexible Learning Programs", "Wide Range of Courses"], None),
        ("Overseas Education", "var(--green)", "plane", ["University Selection", "Admission Guidance", "Visa Assistance", "Pre-Departure Support"], None),
        ("Internship Programmes", "var(--navy)", "brief", ["Industry Training", "Practical Exposure", "Skill Development"], None),
        ("Certificate &amp; Diploma Courses", "var(--navy)", "doc", None, "Short Term &amp; Long Term Certification Programs."),
        ("Career Counselling", "var(--green)", "users", None, "Personalized counselling to help you choose the right career path."),
        ("Application &amp; Documentation Support", "var(--green)", "clip", None, "Complete support for application &amp; documentation at every step."),
        ("University Admission Assistance", "var(--navy)", "bank", None, "Guidance for top universities and a smooth admission process."),
    ]
    cards = []
    for t, c, i, lst, txt in svc:
        body = (
            "<ul>" + "".join(f"<li>{ic('check')} {x}</li>" for x in lst) + "</ul>" if lst else f"<p>{txt}</p>"
        )
        cards.append(f'<div class="svc reveal" style="--c:{c}"><div class="ic">{ic(i)}</div><h3>{t}</h3>{body}</div>')
    cards.append(
        f'<div class="svc reveal" style="--c:var(--red)"><div class="ic">{ic("headset")}</div>'
        f'<h3>Student Support &amp; Guidance</h3><p>End-to-end support until you achieve your academic goals.</p></div>'
    )
    cards_html = "\n".join(cards)

    fac = [
        ("APOSS Admissions", "10th (SSC) & Intermediate", "#1f7a3a", "book"),
        ("Degree Admissions", "All Recognized Universities", "#173172", "cap"),
        ("PG Admissions", "MBA, MCA, M.Com., MA, MSc & More", "#6a2c91", "users"),
        ("Engineering Admissions", "in India Deemed Universities", "#e8731a", "building"),
        ("Distance Education", "UG, PG & Diploma Courses", "#0e8fb0", "laptop"),
        ("Career Guidance", "Choose the Right Path for Your Future", "#d81b7a", "steps"),
        ("Scholarship Guidance", "Find & Apply for Best Scholarships", "#d99a00", "award"),
        ("Internship Support", "Opportunities in Top Companies", "#1f7a3a", "brief"),
        ("Documentation Support", "Guidance for all Documents", "#173172", "doc"),
        ("Education Loan Assistance", "Easy Loan Process Support", "#c8102e", "rupee"),
        ("Exam Registration Assistance", "Forms, Hall Tickets, Results & More", "#7a3b12", "clip"),
        ("Student Counselling", "Personal Guidance & Support", "#6a2c91", "headset"),
    ]
    fac_html = "\n".join(
        f"""<div class="fac reveal" style="--c:{c}"><div class="ic">{ic(i)}</div><div><h4>{t.replace('&','&amp;')}</h4><p>{d.replace('&','&amp;')}</p></div></div>"""
        for t, d, c, i in fac
    )
    why = [("Trusted Guidance", "shield"), ("Experienced Counselling", "users"), ("Affordable Fees", "rupee"), ("Quick Admission Process", "clock"), ("Student-Centric Support", "cap")]
    why_html = "\n".join(f'<div class="why reveal"><div class="ic">{ic(i)}</div><h4>{t}</h4></div>' for t, i in why)
    steps = [
        ("Call or Message", "Reach us on call or WhatsApp with your questions."),
        ("Get Counselled", "Personalised counselling to choose the right course."),
        ("Submit Documents", "We support your application & documentation."),
        ("Secure Admission", "Smooth admission into a recognised university."),
        ("Keep Going", "Exam & assignment help until you reach your goal."),
    ]
    steps_html = "\n".join(f'<div class="step reveal"><h4>{t}</h4><p>{d}</p></div>' for t, d in steps)

    return head(
        "Our Services | Kushi Educational Consultancy, Kakinada",
        "Admissions, distance education, overseas education, internships, certificate & diploma courses, career counselling and student support – Kushi Educational Consultancy.",
        "services",
    ) + f"""
<section class="page-banner" style="padding:3.8rem 0 4.2rem">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> / Our Services</div>
    <h1>Our Services</h1>
    <p>Complete educational guidance – from admission to graduation and beyond. Your dream, our guidance, your success.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">What We Offer</span>
      <h2>Services Designed Around Students</h2>
      <div class="divider"></div>
    </div>
    <div class="svc-grid">
{cards_html}
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">All Facilities · Admissions Open 2026-27</span>
      <h2>All Facilities at a Glance</h2>
      <div class="divider"></div>
    </div>
    <div class="fac-grid">
{fac_html}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">How It Works</span>
      <h2>Your Path to Admission</h2>
      <div class="divider"></div>
    </div>
    <div class="steps">
{steps_html}
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Why Choose Us?</span>
      <h2>The Kushi Advantage</h2>
      <div class="divider"></div>
    </div>
    <div class="why-grid">
{why_html}
    </div>
  </div>
</section>

<section class="quote">
  <div class="container reveal">
    <h2>YOUR DREAM · OUR GUIDANCE · YOUR SUCCESS</h2>
    <p>Building bright futures through education.</p>
    <div style="margin-top:1.8rem"><a class="btn btn-gold" href="contact.html">Book a Free Counselling Call {ic('arrow')}</a></div>
  </div>
</section>

{cta()}
""" + foot()


# ------------------------------------------------------------------ CONTACT
def contact():
    return head(
        "Contact Us | Kushi Educational Consultancy, Vakalapudi, Kakinada",
        "Contact Kushi Educational Consultancy – call 7989192236 / 7036672236 or visit us at Vakalapudi, Kakinada, Andhra Pradesh 533005.",
        "contact",
    ) + f"""
<section class="page-banner" style="padding:3.8rem 0 4.2rem">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> / Contact Us</div>
    <h1>Contact Us</h1>
    <p>We are just a message away. Call, WhatsApp or visit us – our counsellors will be happy to help.</p>
  </div>
</section>

<section>
  <div class="container contact-grid">
    <div>
      <div class="info-card reveal" style="--c:var(--red)">
        <div class="ic">{ic('phone')}</div>
        <div><h3>Call Now</h3>
          <a class="big" href="tel:+91{P1}">{P1}</a>
          <a class="big" href="tel:+91{P2}">{P2}</a></div>
      </div>
      <div class="info-card reveal" style="--c:#25d366">
        <div class="ic">{ic('wa')}</div>
        <div><h3>WhatsApp</h3>
          <p>We are just a message away!</p>
          <p style="margin-top:.6rem"><a class="btn btn-green" style="color:#fff;padding:.55rem 1.2rem;font-size:.9rem" href="https://wa.me/91{P1}?text=Hello%20Kushi%20Educational%20Consultancy" target="_blank" rel="noopener">Chat on WhatsApp</a></p></div>
      </div>
      <div class="info-card reveal" style="--c:var(--navy)">
        <div class="ic">{ic('pin')}</div>
        <div><h3>Visit Us</h3>
          <p>Vakalapudi, Kakinada<br>Andhra Pradesh – 533005</p></div>
      </div>
      <div class="info-card reveal" style="--c:var(--green)">
        <div class="ic">{ic('user')}</div>
        <div><h3>Director</h3>
          <p>Hemanth Thommandra</p></div>
      </div>
    </div>

    <div class="form-card reveal">
      <h2>Admission Enquiry 2026-27</h2>
      <p>Fill in your details and send them to our team on WhatsApp – we’ll get back to you with the right guidance.</p>
      <form id="enquiryForm" novalidate>
        <div class="form-row">
          <div class="field"><label for="name">Full Name *</label><input id="name" name="name" type="text" required placeholder="Your name"></div>
          <div class="field"><label for="phone">Mobile Number *</label><input id="phone" name="phone" type="tel" required inputmode="numeric" placeholder="10-digit mobile number"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="course">Interested In *</label>
            <select id="course" name="course" required>
              <option value="">Select an option</option>
              <option>10th (SSC) Admission</option>
              <option>Intermediate Admission</option>
              <option>Degree (UG) Admission</option>
              <option>PG Admission</option>
              <option>Engineering Admission</option>
              <option>Distance Education</option>
              <option>Certificate / Diploma Course</option>
              <option>Overseas Education</option>
              <option>Internship Programme</option>
              <option>Scholarship / Education Loan Guidance</option>
              <option>Career Counselling</option>
              <option>Other</option>
            </select></div>
          <div class="field"><label for="qualification">Highest Qualification</label>
            <select id="qualification" name="qualification">
              <option value="">Select</option>
              <option>Below 10th</option><option>10th / SSC</option><option>Intermediate (10+2)</option><option>Degree</option><option>Post Graduation</option><option>Other</option>
            </select></div>
        </div>
        <div class="field"><label for="message">Message</label><textarea id="message" name="message" placeholder="Tell us which course or service you are looking for…"></textarea></div>
        <button class="btn btn-primary" type="submit">{ic('send')} Send Enquiry via WhatsApp</button>
        <p class="form-msg" id="formMsg" role="status"></p>
      </form>
    </div>
  </div>

  <div class="container">
    <div class="map reveal">
      <iframe title="Kushi Educational Consultancy location – Vakalapudi, Kakinada" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=Vakalapudi,+Kakinada,+Andhra+Pradesh+533005&amp;output=embed"></iframe>
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Quick Answers</span>
      <h2>Frequently Asked Questions</h2>
      <div class="divider"></div>
    </div>
    <div class="faq">
      <details class="reveal"><summary>Who can join?</summary><p>Students after 10th / Intermediate, working professionals, job aspirants, housewives and anyone who wants to build their career.</p></details>
      <details class="reveal"><summary>Which admissions are open?</summary><p>Admissions are open for 10th, Intermediate, Degree (UG) and Post Graduation (PG) for the 2026-27 academic year.</p></details>
      <details class="reveal"><summary>Do you offer regular and distance modes?</summary><p>Yes – we offer regular and distance mode options through recognised universities, with UGC / DEB approved programmes.</p></details>
      <details class="reveal"><summary>What support do I get after admission?</summary><p>Our student support covers exam &amp; assignment support, exam registration assistance (forms, hall tickets, results) and end-to-end guidance until you achieve your academic goals.</p></details>
      <details class="reveal"><summary>How do I get started?</summary><p>Call us on {P1} or {P2}, message us on WhatsApp, or send the enquiry form above and our team will contact you.</p></details>
    </div>
  </div>
</section>

{cta()}
""" + foot()


for name, html in (("index.html", home()), ("services.html", services()), ("contact.html", contact())):
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name, len(html))
