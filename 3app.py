import streamlit as st

# --- Helper functions for multi-page app ---
def show_home_page():
    # Hero Section with a full-width image and overlay text
    st.markdown(
        """
        <style>
            .hero-container {
                background: linear-gradient(135deg, #E0F7FA, #B2EBF2);
                color: #003366;
                padding: 4rem 2rem;
                border-radius: 12px;
                margin-bottom: 2rem;
                display: flex;
                align-items: center;
                gap: 2rem;
            }
            .hero-text {
                flex: 2;
            }
            .hero-image {
                flex: 1;
                text-align: right;
            }
            .hero-title {
                font-size: 3rem;
                font-weight: bold;
                line-height: 1.2;
                margin-bottom: 0.5rem;
                color: #003366;
            }
            .hero-subtitle {
                font-size: 1.5rem;
                color: #005A9C;
                margin-bottom: 2rem;
            }
            .book-button, .contact-button {
                background-color: #0077B6;
                color: white;
                font-weight: bold;
                padding: 1rem 2rem;
                border-radius: 8px;
                text-decoration: none;
                margin-right: 1rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
        </style>
        <div class="hero-container">
            <div class="hero-text">
                <h1 class="hero-title">Health Professionals</h1>
                <p class="hero-subtitle">Your Health is Important, Take Care</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sceleris
                <a href="#" class="book-button">Book Appointment</a>
            </div>
            <div class="hero-image">
                <img src="https://images.unsplash.com/photo-1549414002-3642732997d0?q=80&w
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    # Content section with three columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h2 style='color:#003366;'>Medication Management</h2>", unsafe_allow_
        st.markdown("<p style='color:#555555;'>Psychotherapy</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(
            """
            <div style="display: flex; gap: 10px;">
                <a href="#"><img src="https://img.icons8.com/color/48/000000/facebook-new.
                <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png"
                <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" 
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown("<h2 style='color:#003366;'>Testimonials</h2>", unsafe_allow_html=True
        st.markdown(
            """
            <div style="background-color: #F0F0F0; padding: 15px; border-radius: 12px; mar
                <p style="font-style: italic; color: #555555;">"Thrive has truly changed m
                <p style="text-align: right; font-weight: bold; color: #555555;">- A.B., P
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.markdown("<h2 style='color:#003366;'>Featured News</h2>", unsafe_allow_html=Tru
        st.markdown(
            """
            <div style="color: #555555;">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <br>
                <h4 style='color: #0077B6;'>Featured News</h4>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
            """, unsafe_allow_html=True
        )


# --- Main App Logic ---
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide", initial_side

# Custom CSS for a professional look with a background image
st.markdown("""
<style>
    /* Main app container with a background image */
    [data-testid="stAppViewContainer"] {
        background: url("https://images.unsplash.com/photo-1549414002-3642732997d0?q=80&w=
        background-size: cover;
        background-position: center;
    }
    
    /* Content container to create a layered effect */
    [data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.85); /* Semi-transparent background for readabil
        backdrop-filter: blur(8px); /* Blur effect */
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        padding: 2rem;
    }

    /* Logo and Header Styling */
    .logo {
        font-size: 2rem;
        font-weight: bold;
        color: #003366;
    }

    /* General text and heading colors */
    h1, h2, h3, h4 {
        color: #003366;
    }
    p, a, div, span, li, ul, pre {
        color: #555555;
    }

    /* Button styles */
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #40E0D0;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Top navigation with a logo
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; paddin
        <span class="logo">Thrive</span>
        <div style="display: flex; gap: 20px;">
            <a href="#" style="font-weight: bold; color: #555555; text-decoration: none;">
            <a href="#" style="font-weight: bold; color: #555555; text-decoration: none;">
            <a href="#" style="font-weight: bold; color: #555555; text-decoration: none;">
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
    <p style='color: #003366;'>
        <br>
        © 2024 Thrive Mental Health Wellness. All rights reserved.
        <br>
        <strong>Disclaimer:</strong> This website is for informational purposes only and d
        Always seek the advice of a qualified healthcare professional with any questions r
    </p>
</div>
""", unsafe_allow_html=True)
