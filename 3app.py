import streamlit as st

# --- Helper functions for multi-page app ---
def show_home_page():
    # Top navigation bar (mimics the image layout)
    col_nav_1, col_nav_2, col_nav_3, col_nav_4 = st.columns([1, 1, 1, 1])
    with col_nav_2:
        st.markdown("<p style='text-align: right; font-weight: bold;'>Home</p>", unsafe_allow_html=True)
    with col_nav_3:
        st.markdown("<p style='text-align: center; font-weight: bold;'>Login</p>", unsafe_allow_html=True)
    with col_nav_4:
        st.markdown("<p style='text-align: left; font-weight: bold;'>Register</p>", unsafe_allow_html=True)

    # Hero Section with Two Columns
    hero_container = st.container()
    with hero_container:
        st.markdown(
            f"""
            <style>
            .hero-container {{
                background: linear-gradient(to right, #1a237e, #0d47a1);
                color: white;
                padding: 4rem 2rem;
                border-radius: 12px;
            }}
            .hero-title {{
                font-size: 3rem;
                font-weight: bold;
                line-height: 1.2;
                margin-bottom: 0.5rem;
                color: #B0C4DE;
            }}
            .hero-subtitle {{
                font-size: 1.5rem;
                color: #B0C4DE;
                margin-bottom: 2rem;
            }}
            .book-button {{
                background-color: #FFA500;
                color: white;
                font-weight: bold;
                padding: 1rem 2rem;
                border-radius: 8px;
                text-decoration: none;
                margin-right: 1rem;
            }}
            .contact-button {{
                background-color: #2c3e50;
                color: white;
                font-weight: bold;
                padding: 1rem 2rem;
                border-radius: 8px;
                text-decoration: none;
            }}
            </style>
            <div class="hero-container">
                <div class="row">
                    <div class="col">
                        <h1 class="hero-title">Welcome to Thrive Mental Wellness Hospital</h1>
                        <p class="hero-subtitle">Your mental wellness is our priority.</p>
                        <a href="#" class="book-button">Book Appointment</a>
                        <a href="#" class="contact-button">Contact Us</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

    # Three-Column Content Section
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Medication Management")
        st.write("Psychotherapy")
        
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
            <div style="background-color: #2c3e50; padding: 15px; border-radius: 12px; margin-bottom: 10px;">
                <p style="font-style: italic; color: #CCCCCC;">"Thrive has truly changed my life. The support and care I received were exceptional."</p>
                <p style="text-align: right; font-weight: bold; color: #CCCCCC;">- A.B., Patient</p>
            </div>
            """, unsafe_allow_html=True
        )
    
    with col3:
        st.header("Featured News")
        st.markdown(
            """
            <div style="color: #CCCCCC;">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <br>
                <h4 style='color: #B0C4DE;'>Featured News</h4>
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
        background-color: #1A237E;
    }
    
    /* Sidebar Background Color (if used) */
    [data-testid="stSidebar"] {
        background-color: #263238;
    }
    
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    h1, h2, h3, h4 {
        color: #B0C4DE;
    }
    .stButton>button {
        background-color: #FFA500;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #FF8C00;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Display pages based on selection (single page design now)
show_home_page()

# Footer Section
st.markdown("""
<div class="footer">
    <p>
        <br>
        © 2024 Thrive Mental Health Wellness. All rights reserved.
        <br>
        <strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice.
        Always seek the advice of a qualified healthcare professional with any questions regarding a medical condition.
    </p>
</div>
""", unsafe_allow_html=True)
