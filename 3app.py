import streamlit as st
import base64

# --- Helper functions for multi-page app ---
def show_home_page():
    # Top navigation bar
    col_nav_spacer, col_nav_home, col_nav_login, col_nav_register = st.columns([2, 1, 1, 1])
    with col_nav_home:
        st.markdown("<p style='text-align: center; font-weight: bold; color: #555555;'>Home</p>", unsafe_allow_html=True)
    with col_nav_login:
        st.markdown("<p style='text-align: center; font-weight: bold; color: #555555;'>Login</p>", unsafe_allow_html=True)
    with col_nav_register:
        st.markdown("<p style='text-align: center; font-weight: bold; color: #555555;'>Register</p>", unsafe_allow_html=True)

    # Hero Section with Two Columns and Image
    hero_container = st.container()
    with hero_container:
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.markdown(
                f"""
                <style>
                .hero-container {{
                    background: linear-gradient(to right, #E8F8F5, #D6F1E9);
                    color: #555555;
                    padding: 4rem 2rem;
                    border-radius: 12px;
                }}
                .hero-title {{
                    font-size: 3rem;
                    font-weight: bold;
                    line-height: 1.2;
                    margin-bottom: 0.5rem;
                    color: #2E8B57;
                }}
                .hero-subtitle {{
                    font-size: 1.5rem;
                    color: #555555;
                    margin-bottom: 2rem;
                }}
                .book-button, .contact-button {{
                    background-color: #2E8B57;
                    color: white;
                    font-weight: bold;
                    padding: 1rem 2rem;
                    border-radius: 8px;
                    text-decoration: none;
                    margin-right: 1rem;
                }}
                .contact-button {{
                    background-color: #8B4513;
                }}
                </style>
                <div class="hero-container">
                    <h1 class="hero-title">Welcome to Thrive Mental Wellness Hospital</h1>
                    <p class="hero-subtitle">Your mental wellness is our priority.</p>
                    <a href="#" class="book-button">Book Appointment</a>
                    <a href="#" class="contact-button">Contact Us</a>
                </div>
                """, unsafe_allow_html=True
            )
        with col_img:
            st.markdown(
                f"""
                <style>
                .img-container {{
                    background: #F0F0F0;
                    padding: 1rem;
                    border-radius: 12px;
                    text-align: center;
                }}
                </style>
                <div class="img-container">
                    <img src="https://placehold.co/400x400/E8F8F5/555555?text=Cecilia+Wamburu" style="border-radius: 12px; display: block; margin: auto;">
                    <p style="text-align: center; color: #555555; margin-top: 10px;">Cecilia Wamburu, PMHNP-BC</p>
                </div>
                """, unsafe_allow_html=True
            )

    # Three-Column Content Section
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Medication Management")
        st.markdown("<p style='color: #555555;'>Psychotherapy</p>", unsafe_allow_html=True)
        
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
        st.header("Testimonials")
        st.markdown(
            """
            <div style="background-color: #E6F0F2; padding: 15px; border-radius: 12px; margin-bottom: 10px;">
                <p style="font-style: italic; color: #555555;">"Thrive has truly changed my life. The support and care I received were exceptional."</p>
                <p style="text-align: right; font-weight: bold; color: #555555;">- A.B., Patient</p>
            </div>
            """, unsafe_allow_html=True
        )
    
    with col3:
        st.header("Featured News")
        st.markdown(
            """
            <div style="color: #555555;">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <br>
                <h4 style='color: #2E8B57;'>Featured News</h4>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
            """, unsafe_allow_html=True
        )


# --- Main App Logic ---
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a professional look
st.markdown("""
<style>
    /* Global Background Color */
    [data-testid="stAppViewContainer"] {
        background-color: #F8F8F8;
    }
    
    /* Sidebar Background Color (if used) */
    [data-testid="stSidebar"] {
        background-color: #F0F0F0;
    }
    
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    h1, h2, h3, h4 {
        color: #2E8B57;
    }
    p, a, div, span, li, ul, pre {
        color: #555555;
    }

    .stButton>button {
        background-color: #2E8B57;
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

# Display pages based on selection (single page design now)
show_home_page()

# Footer Section
st.markdown("""
<div class="footer">
    <p style='color: #2E8B57;'>
        <br>
        © 2024 Thrive Mental Health Wellness. All rights reserved.
        <br>
        <strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice.
        Always seek the advice of a qualified healthcare professional with any questions regarding a medical condition.
    </p>
</div>
