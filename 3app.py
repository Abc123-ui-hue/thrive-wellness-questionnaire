import streamlit as st

# Set the page configuration for a wide, clean layout
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide")

# Custom CSS to match the exact design from the image
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background-color: #F8F8F8;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    .st-emotion-cache-1f8p9w5, .st-emotion-cache-10qnf12, .st-emotion-cache-18ni7ap, .st-emotion-cache-q8s0x2, .st-emotion-cache-6q9sum, .st-emotion-cache-1cpx6h0 {
        background-color: transparent;
    }

    h1, h2, h3, h4 {
        color: #2F4F4F;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }
    p, a, span, li {
        color: #4A4A4A;
        font-family: 'Roboto', sans-serif;
        line-height: 1.6;
    }
    
    .header-container {
        background-color: white;
        padding: 1.5rem 5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .header-logo {
        display: flex;
        align-items: center;
    }
    .header-nav {
        display: flex;
        gap: 30px;
        font-size: 1.1rem;
    }
    .header-nav a {
        color: #007BFF;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .header-nav a:hover {
        color: #0056b3;
    }

    .hero-section {
        background: linear-gradient(135deg, #007BFF 0%, #3498DB 100%);
        color: white;
        padding: 6rem 5rem;
        border-radius: 15px;
        margin-top: 2rem;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 10px 10px;
    }

    .hero-content {
        display: flex;
        align-items: center;
        gap: 5rem;
        position: relative;
        z-index: 1;
    }
    .hero-text-container {
        flex: 1;
    }
    .hero-image-container {
        flex: 1;
        text-align: right;
    }
    .hero-image {
        width: 100%;
        max-width: 500px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        color: white;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    .hero-description {
        font-size: 1rem;
        color: white;
        line-height: 1.6;
        margin-bottom: 2rem;
    }
    .hero-button button {
        background-color: white;
        color: #007BFF;
        font-size: 1.2rem;
        border-radius: 8px;
        padding: 12px 30px;
        border: none;
        font-weight: bold;
        transition: all 0.2s ease-in-out;
    }
    .hero-button button:hover {
        background-color: #f0f0f0;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    """
    <div class="header-container">
        <div class="header-logo">
            <h2 style="color: #007BFF; margin: 0; padding-right: 5px;">+</h2>
            <h4 style="margin: 0;">Company Name</h4>
        </div>
        <div class="header-nav">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Join Us</a>
            <a href="#">Services</a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-text-container">
                <h1 class="hero-title">Health Professionals</h1>
                <h2 class="hero-subtitle">Your Health is Important, Take Care</h2>
                <p class="hero-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla scelerisque tempor urna, sit amet porttitor mi viverra nec. Pellentesque urna risus, tempus vitae elit tincidunt, hendrerit pharetra sapien. Vivamus dapibus tortor in nisi tincidunt, cursus molestie leo gravida.</p>
                <div class="hero-button">
                    <button>Book an Appointment</button>
                </div>
            </div>
            <div class="hero-image-container">
                <img src="https://images.unsplash.com/photo-1628148902094-1a3597b0a70f?q=80&w=2670&auto=format&fit=crop" class="hero-image" />
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("""
<div class="footer">
    <p>© 2024 Thrive Mental Health Wellness. All rights reserved.</p>
    <p><strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice. Always seek the advice of a qualified healthcare professional.</p>
</div>
""", unsafe_allow_html=True)
