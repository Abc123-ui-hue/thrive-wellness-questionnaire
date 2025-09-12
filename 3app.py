import streamlit as st

# Helper functions for a multi-page app
def show_home_page():
    # Hero Section
    st.markdown(
        """
        <style>
            .hero-container {
                background-color: white;
                padding: 4rem 2rem;
                border-radius: 12px;
                margin-bottom: 2rem;
                display: flex;
                align-items: center;
                gap: 2rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            }
            .hero-text {
                flex: 2;
            }
            .hero-image {
                flex: 1;
                text-align: right;
            }
            .hero-image img {
                max-width: 100%;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            .staff-info {
                background-color: #3CB371; /* Medium Sea Green */
                color: white;
                font-weight: bold;
                padding: 0.5rem 1rem;
                border-radius: 8px;
                margin-top: 1rem;
                display: inline-block;
            }
            .hero-title {
                font-size: 3rem;
                font-weight: bold;
                line-height: 1.2;
                margin-bottom: 0.5rem;
                color: #2F4F4F; /* Dark Slate Gray */
            }
            .hero-subtitle {
                font-size: 1.5rem;
                margin-bottom: 2rem;
                color: #555555;
            }
            .book-button, .contact-button {
                background-color: #3CB371; /* Medium Sea Green */
                color: white;
                font-weight: bold;
                padding: 1rem 2rem;
                border-radius: 8px;
                text-decoration: none;
                margin-right: 1rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: all 0.2s ease-in-out;
            }
            .contact-button {
                background-color: #2F4F4F; /* Dark Slate Gray */
                border: 2px solid #2F4F4F;
                color: white;
            }
            .book-button:hover, .contact-button:hover {
                transform: translateY(-2px);
            }
        </style>
        <div class="hero-container">
            <div class="hero-text">
                <h1 class="hero-title">Welcome to Thrive Mental Wellness Hospital</h1>
                <p class="hero-subtitle">Your mental wellness is our priority.</p>
                <a href="#" class="book-button">Book Appointment</a>
                <a href="#" class="contact-button">Contact Us</a>
            </div>
            <div class="hero-image">
                <img src="https://images.unsplash.com/photo-1549414002-3642732997d0?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Cecilia Wamburu, PMHNP-BC">
                <div class="staff-info">Cecilia Wamburu, PMHNP-BC</div>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    # Content section with three columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h2 style='color:#2F4F4F;'>Medication Management</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#555555;'>We provide comprehensive medication management to help you find the right balance and stability.</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(
            """
            <div style="display: flex; gap: 10px;">
                <a href="#"><img src="https://img.icons8.com/color/48/000000/facebook-new.png" style="width: 32px; height: 32px;"></a>
                <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png" style="width: 32px; height: 32px;"></a>
                <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" style="width: 32px; height: 32px;"></a>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown("<h2 style='color:#2F4F4F;'>Testimonials</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="background-color: #F0F0F0; padding: 15px; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <p style="font-style: italic; color: #555555;">"Thrive has truly changed my life. The support and care I received were exceptional."</p>
                <p style="text-align: right; font-weight: bold; color: #555555;">- A.B., Patient</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.markdown("<h2 style='color:#2F4F4F;'>Featured News</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="color: #555555;">
                <p><strong><a href="#" style="color: #3CB371; text-decoration: none;">New Study on Wellness</a></strong></p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>
            """, unsafe_allow_html=True
        )


# --- Main App Logic ---
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a professional look with a full-page background color
st.markdown("""
<style>
    /* Full-page background color */
    body {
        background-color: #F8F8F8;
    }
    
    /* Target the main app container */
    [data-testid="stAppViewContainer"] {
        background-color: #F8F8F8;
    }
    
    /* Content container styling to give it a "block" feel */
    .block-container {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        padding: 2rem;
        margin-top: 2rem;
    }

    /* Logo and Header Styling */
    .logo {
        font-size: 2rem;
        font-weight: bold;
        color: #2F4F4F;
    }

    /* General text and heading colors */
    h1, h2, h3, h4 {
        color: #2F4F4F;
    }
    p, a, div, span, li, ul, pre {
        color: #555555;
    }

    /* Button styles - general */
    .stButton>button {
        background-color: #2F4F4F;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #3CB371;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Top navigation with a logo
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
        <span class="logo">Thrive</span>
        <div style="display: flex; gap: 20px;">
            <a href="#" style="font-weight: bold; color: #555555; text-decoration: none;">Home</a>
            <a href="#" style="font-weight: bold; color: #555555; text-decoration: none;">Login</a>
            <a href="#" style="font-weight: bold; color: #555555; text-decoration: none;">Register</a>
        </div>
    </div>
    <hr style="border: 1px solid #ccc;">
    """, unsafe_allow_html=True
)

# Display pages based on selection (single page design now)
show_home_page()

# Footer Section
st.markdown("""
<div class="footer">
    <p style='color: #2F4F4F;'>
        <br>
        © 2024 Thrive Mental Health Wellness. All rights reserved.
        <br>
        <strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice.
        Always seek the advice of a qualified healthcare professional with any questions regarding a medical condition.
    </p>
</div>
""", unsafe_allow_html=True)
