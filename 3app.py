import streamlit as st

# Set the page configuration for a wide, clean layout
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide")

# Custom CSS to match the exact design from the image
st.markdown("""
<style>
    /* Color Variables from Image */
    :root {
        --primary-blue: #007BFF;
        --secondary-blue: #E6F0FF;
        --text-dark: #2F4F4F;
        --text-light-gray: #4A4A4A;
        --footer-gray: #777;
    }

    /* General styles for a professional look */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }

    .st-emotion-cache-1f8p9w5, .st-emotion-cache-10qnf12, .st-emotion-cache-18ni7ap, .st-emotion-cache-q8s0x2, .st-emotion-cache-6q9sum, .st-emotion-cache-1cpx6h0 {
        background-color: white;
    }

    h1, h2, h3, h4 {
        color: var(--text-dark);
        font-family: "Segoe UI", sans-serif;
        font-weight: 600;
    }
    p, a, span, li {
        color: var(--text-light-gray);
        font-family: "Segoe UI", sans-serif;
        line-height: 1.6;
    }
    
    .hero-section {
        background-color: var(--secondary-blue);
        border-radius: 12px;
        padding: 3rem 4rem;
        display: flex;
        align-items: center;
        margin-top: 2rem;
        gap: 5rem;
    }

    .hero-text-container {
        flex: 2;
        padding-right: 2rem;
    }

    .hero-image-container {
        flex: 1;
        text-align: center;
    }

    .stButton > button {
        background-color: var(--primary-blue);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 25px;
        transition: all 0.2s ease-in-out;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }
    .header-nav {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 30px;
        font-size: 1.1rem;
        padding-top: 10px;
    }
    .service-card {
        text-align: center;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        background-color: #FFFFFF;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .service-card h4 {
        margin-top: 15px;
        color: var(--primary-blue);
        font-weight: bold;
    }
    .service-card p {
        font-size: 0.9rem;
    }
    .contact-card-container {
        display: flex;
        align-items: center;
        background-color: #f7f7f7;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        margin-top: 2rem;
    }
    .contact-card-text {
        flex: 2;
        text-align: left;
    }
    .contact-card-button {
        flex: 1;
        text-align: right;
    }
    .contact-card-button .stButton > button {
        font-size: 1.2rem;
        padding: 15px 30px;
    }
    .footer {
        text-align: center;
        padding-top: 20px;
        margin-top: 40px;
        border-top: 1px solid #ddd;
        font-size: 0.9rem;
        color: var(--footer-gray);
    }
</style>
""", unsafe_allow_html=True)

# Top navigation
with st.container():
    nav_col1, nav_col2 = st.columns([1, 2])
    with nav_col1:
        st.markdown(
            f"""
            <span style="font-size: 2rem; font-weight: bold; color: {st.get_option('theme.primaryColor')}">Thrive</span><span style="font-size: 2rem; color: #4A4A4A;"> Mental Wellness</span>
            """, unsafe_allow_html=True)
    with nav_col2:
        st.markdown(
            """
            <div class="header-nav">
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Services</a>
                <a href="#">Contact</a>
                <div class="stButton">
                    <button>Get Started</button>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
st.markdown("---")

# Hero Section
with st.container():
    hero_col1, hero_col2 = st.columns([2, 1])
    with hero_col1:
        st.markdown(
            """
            <div class="hero-section" style="background-color: #E6F0FF; box-shadow: none; border-radius: 12px; padding: 3rem 4rem; display: flex; align-items: center; margin-top: 2rem; gap: 5rem;">
                <div style="flex: 2; padding-right: 2rem;">
                    <h1 style="font-size: 3.5rem; color: #2F4F4F;">Your Mental Health Matters</h1>
                    <p style="font-size: 1.2rem; color: #4A4A4A; line-height: 1.6;">Compassionate mental health care for your well-being.</p>
                    <div style="margin-top: 2.5rem;">
                        <a href="#" class="stButton"><button>Book an Appointment</button></a>
                    </div>
                </div>
                <div style="flex: 1; text-align: center;">
                    <img src="https://images.unsplash.com/photo-1559114755-325b3952a1b9?q=80&w=2836&auto=format&fit=crop" style="width: 100%; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15);" />
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# Our Services Section
st.markdown("<div style='text-align: center; padding-top: 2rem;'>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size: 2.5rem;'>Our Services</h2>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

service_col1, service_col2, service_col3 = st.columns(3)

with service_col1:
    st.markdown("<div class='service-card'>", unsafe_allow_html=True)
    st.markdown("### 💬", unsafe_allow_html=True)
    st.markdown("<h4>Individual Therapy</h4>", unsafe_allow_html=True)
    st.markdown("<p>Personalized support to help you navigate life's challenges.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with service_col2:
    st.markdown("<div class='service-card'>", unsafe_allow_html=True)
    st.markdown("### 🧠", unsafe_allow_html=True)
    st.markdown("<h4>Cognitive Behavioral Therapy</h4>", unsafe_allow_html=True)
    st.markdown("<p>Evidence-based treatment for anxiety, depression, and more.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with service_col3:
    st.markdown("<div class='service-card'>", unsafe_allow_html=True)
    st.markdown("### 💻", unsafe_allow_html=True)
    st.markdown("<h4>Teletherapy</h4>", unsafe_allow_html=True)
    st.markdown("<p>Online counseling sessions for you convenience.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Get In Touch Section
st.markdown("<div style='text-align: center; padding-top: 2rem;'>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size: 2.5rem;'>Get In Touch</h2>", unsafe_allow_html=True)
st.markdown("<p>Contact us today to schedule an appointment.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns([1, 1])
with contact_col1:
    st.markdown(
        """
        <div class="contact-card">
            <h2 style="color: white; margin-top: 0;">Get In Touch</h2>
        </div>
        """, unsafe_allow_html=True
    )
with contact_col2:
    st.markdown(
        """
        <div class="contact-card">
            <h2 style="color: white; margin-top: 0;">
                <a href="tel:+1234567890">📞 (123) 456-7890</a>
            </h2>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("---")

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>© 2024 Thrive Mental Health Wellness. All rights reserved.</p>
        <p><strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice. Always seek the advice of a qualified healthcare professional.</p>
    </div>
    """, unsafe_allow_html=True
)
