import streamlit as st

# Set the page configuration for a wide, clean layout
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide")

# --- Custom CSS for a professional and modern look ---
st.markdown("""
<style>
    /* Google Fonts Import for a clean, professional font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="st-emotion-cache"] {
        font-family: 'Inter', sans-serif;
    }

    /* Full-page light blue background */
    .stApp {
        background-color: #F0F8FF; /* Light blue */
    }

    /* Main container styling to center content and add padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }

    /* General text and heading colors */
    h1, h2, h3, h4 {
        color: #004488; /* Dark professional blue */
        font-weight: 700;
    }
    p, li {
        color: #333333; /* Dark gray for body text */
    }

    /* Button styling for a modern, rounded look */
    .stButton > button {
        background-color: #007BFF; /* A friendly, professional blue */
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px; /* Slightly rounded */
        padding: 0.75rem 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-2px);
    }
    
    /* Hero Section styling with a clean, centered look */
    .hero-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 4rem 2rem;
        margin-top: 2rem;
        background-color: white;
        border-radius: 1rem;
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.05);
    }
    .hero-title {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        color: #004488;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        margin-bottom: 1.5rem;
        color: #333333;
    }

    /* Custom styling for cards */
    .card {
        background-color: white;
        border-radius: 1rem;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        text-align: center;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: translateY(-5px);
    }

    /* Footer styling */
    .footer {
        text-align: center;
        padding-top: 2rem;
        margin-top: 2rem;
        border-top: 1px solid #E2E8F0;
        color: #718096;
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
with st.container():
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Thrive Mental Health Wellness</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Your Path to Well-being Starts Here</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='max-width: 600px; font-size:1.1rem;'>We offer compassionate and personalized mental health care to help you thrive.</p>", unsafe_allow_html=True)
    
    # Adding the buttons
    button_col1, button_col2 = st.columns([1, 1])
    with button_col1:
        st.button("Book Appointment", use_container_width=True)
    with button_col2:
        st.button("Contact Us", use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("<h2 style='text-align: center; margin-top: 4rem;'>Our Services</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>We provide a range of services to support your mental health journey.</p>", unsafe_allow_html=True)

service_col1, service_col2, service_col3 = st.columns(3)

with service_col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Individual Therapy")
    st.markdown("---")
    st.write("Personalized counseling to help you navigate life's challenges.")
    st.markdown("</div>", unsafe_allow_html=True)

with service_col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Medication Management")
    st.markdown("---")
    st.write("Comprehensive evaluations and ongoing support for medication.")
    st.markdown("</div>", unsafe_allow_html=True)

with service_col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Telehealth")
    st.markdown("---")
    st.write("Convenient and secure virtual appointments from your home.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Call to Action Section ---
st.markdown("<h2 style='text-align: center; margin-top: 4rem;'>Ready to Begin Your Journey?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Contact us today to schedule your first appointment.</p>", unsafe_allow_html=True)
st.button("Schedule Now", use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2024 Thrive Mental Health Wellness. All rights reserved.</p>
    <p>Disclaimer: This website is for informational purposes only and does not provide medical advice. Always seek the advice of a qualified healthcare professional.</p>
</div>
""", unsafe_allow_html=True)
