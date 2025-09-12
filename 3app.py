import streamlit as st

# Set the page configuration for a wide, clean layout
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide")

# Custom CSS for a clean, minimalist look
st.markdown("""
<style>
    .st-emotion-cache-1f8p9w5 {
        background-color: #E6F0FF;
    }
    .st-emotion-cache-10qnf12 {
        background-color: #E6F0FF;
    }
    .st-emotion-cache-18ni7ap {
        background-color: #E6F0FF;
    }
    .st-emotion-cache-q8s0x2{
        background-color: #E6F0FF;
    }
    .st-emotion-cache-6q9sum{
        background-color: #E6F0FF;
    }
    
    /* General styles for a clean look */
    h1, h2, h3, h4 {
        color: #2F4F4F; /* Dark Slate Gray */
        font-family: sans-serif;
    }
    p {
        color: #555555;
        font-family: sans-serif;
    }
    .stButton>button {
        background-color: #3CB371; /* Medium Sea Green */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
        margin-right: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2F4F4F;
        transform: translateY(-2px);
    }
    a {
        text-decoration: none;
        color: #555555;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding-top: 20px;
        margin-top: 50px;
        border-top: 1px solid #ccc;
        font-size: 0.8rem;
        color: #777;
    }
</style>
""", unsafe_allow_html=True)

# Top navigation
st.columns([1, 4])
with st.container():
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
            <span style="font-size: 2rem; font-weight: bold; color: #2F4F4F;">Thrive</span>
            <div style="display: flex; gap: 20px;">
                <a href="#">Home</a>
                <a href="#">Login</a>
                <a href="#">Register</a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
st.markdown("---")

# Hero Section
st.markdown(
    """
    <div style="text-align: center; padding: 4rem 2rem;">
        <h1 style="font-size: 3rem;">Welcome to Thrive Mental Wellness Hospital</h1>
        <p style="font-size: 1.5rem; color: #555555;">Your mental wellness is our priority.</p>
        <div style="margin-top: 2rem;">
            <a href="#" style="background-color: #3CB371; color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; margin-right: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">Book Appointment</a>
            <a href="#" style="background-color: #2F4F4F; color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">Contact Us</a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

# Content sections
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Medication Management")
    st.write("We provide comprehensive medication management to help you find the right balance and stability.")
    st.markdown("---")
    st.markdown(
        """
        <div style="display: flex; gap: 10px;">
            <a href="#"><img src="https://img.icons8.com/color/48/000000/facebook-new.png" width="32" height="32" /></a>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="32" height="32" /></a>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" width="32" height="32" /></a>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.subheader("Testimonials")
    st.info("“Thrive has truly changed my life. The support and care I received were exceptional.”\n\n- A.B., Patient")

with col3:
    st.subheader("Featured News")
    st.write("**New Study on Wellness**")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>© 2024 Thrive Mental Health Wellness. All rights reserved.</p>
        <p><strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice. Always seek the advice of a qualified healthcare professional.</p>
    </div>
    """, unsafe_allow_html=True
)
