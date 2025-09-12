import streamlit as st

# Helper functions for a multi-page app
def show_home_page():
    # Hero Section
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Welcome to Thrive Mental Wellness Hospital")
        st.subheader("Your mental wellness is our priority.")
        st.write("") # Spacer

        st.button("Book Appointment", help="Click to book an appointment.")
        st.button("Contact Us", help="Click to contact us.")

    with col2:
        st.image("https://images.unsplash.com/photo-1549414002-3642732997d0?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                 caption="Cecilia Wamburu, PMHNP-BC",
                 use_container_width=True)

    st.markdown("---")

    # Content section with three columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Medication Management")
        st.write("We provide comprehensive medication management to help you find the right balance and stability.")
        
    with col2:
        st.subheader("Testimonials")
        st.info("“Thrive has truly changed my life. The support and care I received were exceptional.”\n\n- A.B., Patient")

    with col3:
        st.subheader("Featured News")
        st.write("**New Study on Wellness**")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    
    st.markdown("---")


# --- Main App Logic ---
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a clean look
st.markdown("""
<style>
    body {
        background-color: #F8F9FA;
    }
    .stButton>button {
        background-color: #2F4F4F;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
        margin-right: 1rem;
    }
    .stButton>button:hover {
        background-color: #3CB371;
        transform: scale(1.05);
    }
    [data-testid="stHeader"] {
        background-color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .st-emotion-cache-1f8p9w5 {
        background: #F8F9FA;
    }
    h1, h2, h3, h4 {
        color: #2D3E50;
    }
</style>
""", unsafe_allow_html=True)

# Top navigation
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
        <span style="font-size: 2rem; font-weight: bold; color: #2D3E50;">Thrive</span>
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
<div class="footer" style="padding: 1rem 0; text-align: center; color: #555555;">
    <p>
        © 2024 Thrive Mental Health Wellness. All rights reserved.
        <br>
        <strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice.
        Always seek the advice of a qualified healthcare professional with any questions regarding a medical condition.
    </p>
</div>
""", unsafe_allow_html=True)

