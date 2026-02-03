import streamlit as st

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
    background-color: #fffaf7;
}

.hero {
    padding: 5rem 2rem;
    text-align: center;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    color: #3d2b1f;
}

.hero p {
    font-size: 1.2rem;
    color: #5a4a42;
    max-width: 700px;
    margin: auto;
}

.section {
    padding: 4rem 2rem;
    max-width: 1100px;
    margin: auto;
}

.section h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: #3d2b1f;
    margin-bottom: 1.5rem;
}

.section p {
    font-size: 1.05rem;
    color: #5a4a42;
    line-height: 1.7;
}

.card {
    background: white;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
}

.footer {
    text-align: center;
    padding: 3rem 1rem;
    color: #7a6a60;
    font-size: 0.9rem;
}

.button {
    display: inline-block;
    margin-top: 1.5rem;
    padding: 0.8rem 1.8rem;
    background-color: #d4a373;
    color: white;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>Posh Bridal Concierge</h1>
    <p>
        Your calm, trusted support on the most important day of your life.
        We ensure your wedding day flows beautifully — stress-free, seamless, and unforgettable.
    </p>
    <a class="button" href="#contact">Book a Consultation</a>
</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
st.markdown("""
<div class="section">
    <h2>About Posh Bridal Concierge</h2>
    <p>
        At <strong>Posh Bridal Concierge</strong>, we believe every bride deserves to feel calm,
        confident, and fully present on her wedding day.
    </p>
    <p>
        I’m a professional bridal assistant with a passion for supporting brides through the most
        emotional and meaningful moments of their lives. From the quiet moments of getting dressed
        to the excitement just before walking down the aisle, I’m there — ensuring every detail is handled
        and every worry is eased.
    </p>
    <p>
        This is more than a service. It’s personal care, calm reassurance, and dependable support —
        all wrapped into one trusted presence by your side.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- SERVICES ----------------
st.markdown("""
<div class="section">
    <h2>Services</h2>

    <div class="card">
        <strong>Wedding Day Bridal Assistance</strong><br>
        Hands-on support from start to finish so you can enjoy every moment.
    </div>

    <div class="card">
        <strong>Dress & Veil Styling</strong><br>
        Perfect adjustments, flawless draping, and calm handling of your gown.
    </div>

    <div class="card">
        <strong>Timeline Coordination</strong><br>
        Ensuring everything stays on schedule without stress or rushing.
    </div>

    <div class="card">
        <strong>Emergency Bridal Support</strong><br>
        From quick fixes to unexpected issues — you’re covered.
    </div>

    <div class="card">
        <strong>Emotional Support</strong><br>
        A calm, reassuring presence when emotions run high.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- WHY CHOOSE US ----------------
st.markdown("""
<div class="section">
    <h2>Why Brides Choose Posh</h2>
    <p>• A calm and professional presence under pressure</p>
    <p>• Attention to the smallest details</p>
    <p>• Genuine care for the bride’s comfort and happiness</p>
    <p>• Experience supporting both practical and emotional needs</p>
    <p>• A luxury experience without feeling overwhelming</p>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------
st.markdown("""
<div class="section" id="contact">
    <h2>Get in Touch</h2>
    <p>
        Let’s talk about how I can support you on your special day.
        Reach out to book a consultation or ask any questions.
    </p>
    <p>
        📞 <strong>WhatsApp:</strong> +234-XXX-XXX-XXXX<br>
        📸 <strong>Instagram:</strong> @poshbridalconcierge<br>
        ✉️ <strong>Email:</strong> poshbridalconcierge@gmail.com
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    © 2026 Posh Bridal Concierge • Crafted with care and quiet tech ✨
</div>
""", unsafe_allow_html=True)
