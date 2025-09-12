import streamlit as st

# Set the page configuration for a wide, clean layout
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide")

# Custom CSS for a clean, minimalist look with a new color palette
st.markdown("""
<style>
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
    
    .st-emotion-cache-1f8p9w5 {
        background-color: white;
    }
    .st-emotion-cache-10qnf12 {
        background-color: white;
    }
    .st-emotion-cache-18ni7ap {
        background-color: white;
    }
    .st-emotion-cache-q8s0x2 {
        background-color: white;
    }
    .st-emotion-cache-6q9sum {
        background-color: white;
    }

    h1, h2, h3, h4 {
        color: #2F4F4F; /* Dark Slate Gray */
        font-family: "Segoe UI", sans-serif;
    }
    p, a, span, li {
        color: #4A4A4A; /* Slightly lighter gray for text */
        font-family: "Segoe UI", sans-serif;
        line-height: 1.6;
    }
    .stButton > button {
        background-color: #007BFF;
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
    a {
        text-decoration: none;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding-top: 20px;
        margin-top: 40px;
        border-top: 1px solid #ddd;
        font-size: 0.9rem;
        color: #777;
    }
    .hero-container {
        padding: 4rem 0;
    }
    .service-card {
        text-align: center;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        background-color: #FFFFFF;
    }
    .service-card h4 {
        margin-top: 15px;
        color: #007BFF;
    }
    .service-card p {
        font-size: 0.9rem;
    }
    .st-info {
        background-color: #E6F0FF;
        border-left: 5px solid #007BFF;
        padding: 15px;
        border-radius: 8px;
    }
    .contact-card {
        background-color: #007BFF;
        color: white;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .contact-card h2, .contact-card p, .contact-card a {
        color: white;
    }
    .contact-card .stButton > button {
        background-color: white;
        color: #007BFF;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Top navigation
with st.container():
    nav_col1, nav_col2 = st.columns([1, 2])
    with nav_col1:
        st.markdown('<span style="font-size: 2rem; font-weight: bold; color: #007BFF;">Thrive</span><span style="font-size: 2rem; color: #4A4A4A;"> Mental Wellness</span>', unsafe_allow_html=True)
    with nav_col2:
        st.markdown(
            """
            <div style="display: flex; justify-content: flex-end; align-items: center; gap: 30px; font-size: 1.1rem; padding-top: 10px;">
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Services</a>
                <a href="#">Contact</a>
                <div class="stButton">
                    <button style="background-color: #007BFF; color: white;">Get Started</button>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# Hero Section with two columns
hero_col1, hero_col2 = st.columns([2, 1])

with hero_col1:
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 3.5rem; color: #2F4F4F;">Your Mental Health Matters</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.2rem; color: #4A4A4A;">Compassionate mental health care for your well-being.</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="margin-top: 2.5rem;">
            <a href="#" class="stButton"><button>Book an Appointment</button></a>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

with hero_col2:
    st.image("https://images.unsplash.com/photo-1559114755-325b3952a1b9?q=80&w=2836&auto=format&fit=crop", width=350)
    st.markdown(
        """
        <p style="text-align: center; margin-top: 10px; font-weight: bold; color: #4A4A4A;">Cecilia Wamburu PMHNP-BC</p>
        """, unsafe_allow_html=True
    )
st.markdown("---")

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
