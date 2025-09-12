import streamlit as st

# Set the page configuration for a wide, clean layout
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide")

# Custom CSS for a clean, minimalist look with a new color palette
st.markdown("""
<style>
    /* Color Variables */
    :root {
        --primary-teal: #008080; /* Teal */
        --secondary-orange: #FF7F50; /* Coral */
        --text-dark: #2F4F4F; /* Dark Slate Gray */
        --text-light: #F8F8F8; /* Light gray for contrast */
        --background-light: #E6F0FF; /* Light blue */
        --background-hero: #E6F0FF; /* Light blue-gray for hero */
    }

    /* Full-page background color */
    .st-emotion-cache-1f8p9w5 {
        background-color: var(--background-light);
    }
    .st-emotion-cache-10qnf12 {
        background-color: var(--background-light);
    }
    .st-emotion-cache-18ni7ap {
        background-color: var(--background-light);
    }
    .st-emotion-cache-q8s0x2 {
        background-color: var(--background-light);
    }
    .st-emotion-cache-6q9sum {
        background-color: var(--background-light);
    }

    /* General styles for a professional look */
    h1, h2, h3, h4 {
        color: var(--text-dark);
        font-family: sans-serif;
    }
    p, a {
        color: var(--text-dark);
        font-family: sans-serif;
    }
    .stButton > button {
        background-color: var(--primary-teal);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 25px;
        transition: all 0.2s ease-in-out;
        margin-right: 15px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: var(--secondary-orange);
        transform: translateY(-2px);
    }
    .stButton.orange > button {
        background-color: var(--secondary-orange);
    }
    .stButton.orange > button:hover {
        background-color: var(--primary-teal);
    }
    a {
        text-decoration: none;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding-top: 30px;
        margin-top: 60px;
        border-top: 1px solid #ddd;
        font-size: 0.9rem;
        color: #777;
    }
    .hero-container {
        padding: 6rem 2rem;
        background: var(--background-hero);
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
        display: flex;
        align-items: center;
    }
    .content-section {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        min-height: 250px;
    }
    .st-info {
        background-color: #E6F0FF;
        border-left: 5px solid var(--primary-teal);
        padding: 15px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Top navigation
with st.container():
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
            <span style="font-size: 2.5rem; font-weight: bold; color: var(--text-dark);">Thrive</span>
            <div style="display: flex; gap: 30px; font-size: 1.1rem;">
                <a href="#">Home</a>
                <a href="#">Services</a>
                <a href="#">Contact</a>
                <a href="#">Login</a>
                <a href="#">Register</a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
st.markdown("---")

# Hero Section with two columns
hero_col1, hero_col2 = st.columns([2, 1])

with hero_col1:
    st.markdown(
        """
        <div class="hero-container" style="background: none; box-shadow: none; display: block; padding: 0;">
            <h1 style="font-size: 3.5rem; color: var(--primary-teal);">Welcome to Thrive Mental Wellness</h1>
            <p style="font-size: 1.6rem; color: var(--text-dark); margin-top: -10px;">Your mental wellness is our priority. We provide compassionate care and support to help you navigate your journey to a healthier mind.</p>
            <div style="margin-top: 2.5rem;">
                <a href="#" class="stButton"><button>Book Appointment</button></a>
                <a href="#" class="stButton orange"><button>Contact Us</button></a>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

with hero_col2:
    st.image("https://images.unsplash.com/photo-1559114755-325b3952a1b9?q=80&w=2836&auto=format&fit=crop", width=350)
    st.markdown(
        """
        <p style="text-align: center; margin-top: 10px; font-weight: bold; color: var(--text-dark);">Cecilia Wamburu PMHNP-BC</p>
        """, unsafe_allow_html=True
    )

# Content sections
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown("<div class='content-section'>", unsafe_allow_html=True)
        st.subheader("Medication Management")
        st.write("We provide comprehensive medication management to help you find the right balance and stability on your wellness journey.")
        st.markdown("---")
        st.write("Connect with us:")
        st.markdown(
            """
            <div style="display: flex; gap: 15px;">
                <a href="#"><img src="https://img.icons8.com/color/48/000000/facebook-new.png" width="35" height="35" /></a>
                <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="35" height="35" /></a>
                <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" width="35" height="35" /></a>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown("<div class='content-section'>", unsafe_allow_html=True)
        st.subheader("Testimonials")
        st.markdown("""
        <div class="st-info">
            <p>“Thrive has truly changed my life. The support and care I received were exceptional.”</p>
            <p style="text-align: right; font-weight: bold;">- A.B., Patient</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown("<div class='content-section'>", unsafe_allow_html=True)
        st.subheader("Featured News")
        st.write("### **New Study on Wellness**")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        st.markdown("</div>", unsafe_allow_html=True)

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>© 2024 Thrive Mental Health Wellness. All rights reserved.</p>
        <p><strong>Disclaimer:</strong> This website is for informational purposes only and does not provide medical advice. Always seek the advice of a qualified healthcare professional.</p>
    </div>
    """, unsafe_allow_html=True
)
