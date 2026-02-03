import streamlit as st
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Posh Bridal Concierge",
    page_icon="💐",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Montserrat:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif !important;
    background-color: #ffffff !important;
}
.stApp {
    background-color: #ffffff !important;
}
.hero {
    padding: 5rem 1.5rem;
    text-align: center;
    background: linear-gradient(to bottom, #f0f4ff, #ffffff);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    color: #0f2a6e;
    font-weight: 600;
}
.hero p {
    font-size: 1.2rem;
    color: #2c3e50;
    max-width: 720px;
    margin: auto;
}
.section {
    padding: 4rem 1.5rem;
    max-width: 1200px;
    margin: auto;
}
.section h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: #0f2a6e;
    margin-bottom: 1.5rem;
    text-align: center;
}
.section p {
    font-size: 1.1rem;
    color: #34495e;
    line-height: 1.8;
}
.card {
    background: #ffffff !important;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(15,42,110,0.12) !important;
    margin-bottom: 2rem;
    border: 1px solid #e8f0ff;
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 50px rgba(15,42,110,0.18) !important;
}
.price {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0f2a6e;
    margin-bottom: 1rem;
}
ul {
    color: #2c3e50;
    font-size: 1.05rem;
    line-height: 1.8;
}
.whatsapp-btn {
    display: inline-block;
    background-color: #25D366;
    color: white;
    padding: 16px 32px;
    border-radius: 50px;
    font-size: 1.2rem;
    font-weight: 600;
    text-decoration: none !important;  /* No underline */
    box-shadow: 0 8px 20px rgba(37,213,102,0.35);
    transition: all 0.3s ease;
}
.whatsapp-btn:hover {
    background-color: #20b858;
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(37,213,102,0.45);
    text-decoration: none !important;
}
.social-icon {
    width: 24px;
    height: 24px;
    vertical-align: middle;
    margin-right: 8px;
}
.footer {
    text-align: center;
    padding: 4rem 1rem;
    color: #7f8c8d;
    font-size: 1rem;
    border-top: 1px solid #eee;
}
/* WhatsApp floating */
.whatsapp {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    color: white;
    padding: 16px 20px;
    border-radius: 50%;
    font-size: 26px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    z-index: 1000;
}
.logo-container {
    text-align: center;
    padding: 2rem 0 1rem 0;
}
.logo-img {
    max-width: 180px;
    width: 100%;
    height: auto;
}
@media (max-width: 768px) {
    .hero h1 { font-size: 2.5rem; }
    .section h2 { font-size: 2rem; }
    .card { padding: 1.5rem; }
    .logo-img { max-width: 140px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- BRAND LOGO ----------------
logo_path = Path("posh logo.png")
if logo_path.exists():
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("posh logo.png", use_column_width=False, width=180, output_format="PNG")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>Posh Bridal Concierge</h1>
    <p>
        Your calm, trusted support on the most important day of your life.<br>
        We help brides feel confident, supported, and fully present.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
st.markdown("""
<div class="section">
    <h2>About Posh Bridal Concierge</h2>
    <p>
        Posh Bridal Concierge provides professional bridal assistance designed to remove stress 
        and allow brides to fully enjoy their wedding experience.
    </p>
    <p>
        I offer calm, hands-on support before and during your big day, managing details, 
        coordinating vendors, and ensuring everything runs smoothly, so you don’t have to.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- WHY CHOOSE US ----------------
st.markdown("""
<div class="section">
    <h2>Why Brides Choose Us</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center;">
        <div class="card" style="flex: 1; min-width: 280px;">
            <strong>Calm & Composed</strong><br>
            Bringing peace to your wedding day, no chaos, just support.
        </div>
        <div class="card" style="flex: 1; min-width: 280px;">
            <strong>Detail-Oriented</strong><br>
            Catching the little things so nothing slips through.
        </div>
        <div class="card" style="flex: 1; min-width: 280px;">
            <strong>Fully Present for You</strong><br>
            So you can focus on love, joy, and memories. Not logistics.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- PRICING PACKAGES ----------------
st.markdown("""
<div class="section">
    <h2>Our Packages</h2>
    <div class="card">
        <div class="price">Basic Package — ₦100,000</div>
        <strong>On-the-Day Support</strong>
        <ul>
            <li>Bridal morning prep supervision & assistance</li>
            <li>Vendor coordination & management during the event</li>
            <li>Managing schedule & timeline adherence</li>
            <li>Running errands & real-time troubleshooting</li>
        </ul>
    </div>
    <div class="card">
        <div class="price">Standard Package — ₦150,000</div>
        <strong>Extended Bridal Support</strong>
        <ul>
            <li>All services included in the Basic Package</li>
            <li>Pre-wedding support (photoshoot)</li>
            <li>One cloth fitting</li>
            <li>Final checklist & timeline confirmation</li>
            <li>Bridal party coordination & support</li>
        </ul>
    </div>
    <div class="card">
        <div class="price">Premium Package — ₦250,000</div>
        <strong>Full Bridal Concierge Experience</strong>
        <ul>
            <li>Vendor recommendations & liaising</li>
            <li>Wedding timelines & checklist creation</li>
            <li>Virtual wedding consultation sessions</li>
            <li>Hotel booking assistance</li>
            <li>Bridal outfit & accessories sourcing coordination</li>
            <li>Engagement & pre-wedding event support</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- TESTIMONIALS ----------------
st.markdown("""
<div class="section">
    <h2>What Our Brides Say</h2>
    <div class="card">
        “I honestly don’t know how I would have gotten through my wedding morning without her. 
        From calming my nerves to making sure everything was in place, she was truly my safe space.”
        <br><br><strong>— Tolu, Lagos</strong>
    </div>
    <div class="card">
        “She handled my dress, coordinated vendors, and kept everyone on schedule while I just enjoyed my day. 
        Having Posh Bridal Concierge was one of the best decisions I made for my wedding.”
        <br><br><strong>— Amaka, Traditional & White Wedding</strong>
    </div>
    <div class="card">
        “Professional, gentle, and extremely attentive. 
        She noticed details I would never have thought of and handled issues before they became problems.”
        <br><br><strong>— Sade, Ibadan</strong>
    </div>
    <div class="card">
        “What stood out the most was how calm she was. 
        That calmness transferred to me and my bridal party. I felt supported emotionally and physically throughout the day.”
        <br><br><strong>— Blessing, Wedding Day Client</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- INQUIRY / WHATSAPP CTA ----------------
st.markdown("""
<div class="section" style="text-align: center;">
    <h2>Ready to Experience/Have a Seamless and Stress-Free Day?</h2>
    <p style="margin-bottom: 2rem;">
        Send a message on WhatsApp. Tell me about your wedding, preferred package, 
        and wedding date. I’ll reply within a few hours.
    </p>
    <a href="https://wa.me/2348166344356?text=Hi%20Posh%20Bridal%20Concierge!%20I'm%20interested%20in%20your%20services.%20My%20name%20is%20[Your%20Name],%20my%20wedding%20is%20on%20[Date],%20and%20I'm%20interested%20in%20the%20[Basic/Standard/Premium]%20package.%20Here's%20a%20bit%20about%20my%20wedding:" 
       target="_blank" class="whatsapp-btn">
       Chat on WhatsApp Now 💬
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------
st.markdown("""
<div class="section">
    <h2>Contact</h2>
    <p>
         <strong>Call / WhatsApp:</strong> 08166344356<br>
         <strong>Instagram:</strong> 
        <svg class="social-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="24" height="24" rx="6" fill="url(#grad)"/>
            <defs>
                <radialGradient id="grad" cx="0.5" cy="0.5" r="0.8">
                    <stop offset="0%" stop-color="#feda75"/>
                    <stop offset="30%" stop-color="#fa7e1e"/>
                    <stop offset="60%" stop-color="#d62976"/>
                    <stop offset="100%" stop-color="#962fbf"/>
                </radialGradient>
            </defs>
            <circle cx="12" cy="12" r="5" stroke="white" stroke-width="2"/>
            <circle cx="18" cy="6" r="1.5" fill="white"/>
        </svg>
        <a href="https://www.instagram.com/posh_bridalconcierge?igsh=MXFxcDRudTdiOTZlMQ==" target="_blank">
        @posh_bridalconcierge</a><br>
         <strong>TikTok:</strong> 
        <svg class="social-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.53 2C12.53 2 12.53 12.5 12.53 12.5C12.53 14.5 10.9 16 8.8 16C6.7 16 5 14.5 5 12.5C5 10.5 6.7 9 8.8 9C9.5 9 10.1 9.2 10.6 9.6L12.53 2Z" fill="black"/>
            <path d="M19 5.5C19 5.5 16.5 8 13.5 8V12.5C13.5 15 16 17.5 19 17.5" stroke="black" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <a href="https://www.tiktok.com/@posh_bridal_concierge" target="_blank">
        @posh_bridal_concierge</a>
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- WHATSAPP FLOATING BUTTON ----------------
st.markdown("""
<a href="https://wa.me/2348166344356" target="_blank" class="whatsapp">💬</a>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    © Posh Bridal Concierge • Crafted with care & quiet technology ✨
</div>
""", unsafe_allow_html=True)
