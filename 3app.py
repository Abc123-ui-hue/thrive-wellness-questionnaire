import streamlit as st
import base64

# Helper function to convert local image to base64
def get_image_as_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Page functions ---
def show_home_page():
    # Hero Section with Two Columns and Image
    hero_container = st.container()
    with hero_container:
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.markdown(
                f"""
                <style>
                .hero-container {{
                    background: linear-gradient(to right, #E0F5EB, #D6F1E9);
                    color: #333333;
                    padding: 4rem 2rem;
                    border-radius: 12px;
                }}
                .hero-title {{
                    font-size: 3rem;
                    font-weight: bold;
                    line-height: 1.2;
                    margin-bottom: 0.5rem;
                    color: #008080;
                }}
                .hero-subtitle {{
                    font-size: 1.5rem;
                    color: #555555;
                    margin-bottom: 2rem;
                }}
                .book-button, .contact-button {{
                    background-color: #008080;
                    color: white;
                    font-weight: bold;
                    padding: 1rem 2rem;
                    border-radius: 8px;
                    text-decoration: none;
                    margin-right: 1rem;
                }}
                .contact-button {{
                    background-color: #3CB371;
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
                    padding: 1rem;
                    border-radius: 12px;
                    text-align: center;
                }}
                </style>
                <div class="img-container">
                    <img src="https://placehold.co/400x400/D6F1E9/333333?text=Cecilia+Wamburu" style="border-radius: 12px; display: block; margin: auto;">
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
                <h4 style='color: #008080;'>Featured News</h4>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
            """, unsafe_allow_html=True
        )


# --- Main App Logic ---
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a professional look with background image and logo
st.markdown("""
<style>
    /* Global Background Color and Image */
    body {
        background-color: #F0F8FF; /* Fallback color */
        background-image: url("https://images.unsplash.com/photo-1549414002-3642732997d0?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Streamlit container styling */
    [data-testid="stAppViewContainer"] {
        background: rgba(255, 255, 255, 0.9); /* Semi-transparent background for readability */
        backdrop-filter: blur(10px); /* Blur effect to make it more appealing */
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 2rem;
    }
    
    /* Logo and Header Styling */
    .logo {{
        font-size: 2rem;
        font-weight: bold;
        color: #008080;
    }}
    
    /* Text and Heading Colors */
    h1, h2, h3, h4 {{
        color: #008080;
    }}
    p, a, div, span, li, ul, pre {{
        color: #555555;
    }}
    
    /* Button Styles */
    .stButton>button {{
        background-color: #008080;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
    }}
    .stButton>button:hover {{
        background-color: #3CB371;
        transform: scale(1.05);
    }}

</style>
""", unsafe_allow_html=True)

# Top navigation with Logo
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
    <p style='color: #008080;'>
        <br>
        © 2024 Thrive Mental Health Wellness. All rights reserved.
        <br>
        <strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice.
        Always seek the advice of a qualified healthcare professional with any questions regarding a medical condition.
    </p>
</div>
""", unsafe_allow_html=True)
