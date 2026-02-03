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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Montserrat:wght@300;400;500&display=swap');
html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
    background-color: #f9fbff;
}
.hero {
    padding: 4rem 1.5rem;
    text-align: center;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    color: #1f3c88;
}
.hero p {
    font-size: 1.15rem;
    color: #3d4c66;
    max-width: 720px;
    margin: auto;
}
.section {
    padding: 3.5rem 1.5rem;
    max-width: 1100px;
    margin: auto;
}
.section h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.1rem;
    color: #1f3c88;
    margin-bottom: 1.2rem;
}
.section p {
    font-size: 1.05rem;
    color: #3d4c66;
    line-height: 1.7;
}
.card {
    background: white;
    padding: 1.8rem;
    border-radius: 16px;
    box-shadow: 0 12px 30px rgba(31,60,136,0.08);
    margin-bottom: 1.5rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 40px rgba(31,60,136,0.12);
}
.price {
    font-size: 1.3rem;
    font-weight: 600;
    color: #1f3c88;
    margin-bottom: 0.8rem;
}
.whatsapp-btn {
    display: inline-block;
    background-color: #25D366;
    color: white;
    padding: 14px 28px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 500;
    text-decoration: none;
    box-shadow: 0 6px 15px rgba(37,213,102,0.3);
    transition: all 0.3s ease;
}
.whatsapp-btn:hover {
    background-color: #20b858;
    transform: translateY(-2px);
}
.footer {
    text-align: center;
    padding: 3rem 1rem;
    color: #6b7a99;
    font-size: 0.9rem;
}
/* WhatsApp floating button */
.whatsapp {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #25D366;
    color: white;
    padding: 14px 18px;
    border-radius: 50%;
    font-size: 22px;
    text-decoration: none;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    z-index: 1000;
}
/* Mobile optimization */
@media (max-width: 768px) {
    .hero h1 { font-size: 2.2rem; }
    .section h2 { font-size: 1.8rem; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGO (OPTIONAL) ----------------
logo_path = Path("logo.png")
if logo_path.exists():
    st.image("logo.png", width=120)

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
        I offer calm, hands-on support before and during your big day — managing details, 
        coordinating vendors, and ensuring everything runs smoothly, so you don’t have to.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- WHY CHOOSE US ----------------
st.markdown("""
<div class="section">
    <h2>Why Brides Choose Posh</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center;">
        <div class="card" style="flex: 1; min-width: 280px;">
            <strong>Calm & Composed</strong><br>
            Bringing peace to your wedding day — no chaos, just support.
        </div>
        <div class="card" style="flex: 1; min-width: 280px;">
            <strong>Detail-Oriented</strong><br>
            Catching the little things so nothing slips through.
        </div>
        <div class="card" style="flex: 1; min-width: 280px;">
            <strong>Fully Present for You</strong><br>
            So you can focus on love, joy, and memories — not logistics.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- PRICING PACKAGES ----------------
st.markdown("""
<div class="section">
    <h2>Pricing Packages</h2>
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

# ---------------- REAL TESTIMONIALS ----------------
st.markdown("""
<div class="section">
    <h2>What Brides Say</h2>
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
    <h2>Ready to Make Your Day Stress-Free?</h2>
    <p style="margin-bottom: 2rem;">
        Send a message on WhatsApp — tell me about your wedding, preferred package, 
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
        📞 <strong>Call / WhatsApp:</strong> 08166344356<br>
        📸 <strong>Instagram:</strong> 
        <a href="https://www.instagram.com/posh_bridalconcierge?igsh=MXFxcDRudTdiOTZlMQ==" target="_blank">
        @posh_bridalconcierge</a><br>
        🎵 <strong>TikTok:</strong> 
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
