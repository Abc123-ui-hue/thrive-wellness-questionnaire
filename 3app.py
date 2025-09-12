import streamlit as st

# --- Page Configuration ---
# Use a wide layout to make the most of the screen space
st.set_page_config(
    page_title="Streamlit Layout",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Styling ---
# This uses st.markdown to inject custom CSS for a more polished look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="st-emotion-cache"] {
        font-family: 'Inter', sans-serif;
    }

    /* General styling for a clean look */
    .st-emotion-cache-121p51f {
        background-color: #f8f9fa;
    }
    .st-emotion-cache-r4231b {
        padding-top: 0;
        padding-bottom: 0;
        padding-left: 0;
        padding-right: 0;
    }

    /* Header styling */
    .header {
        background-color: white;
        padding: 1rem 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .logo {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
    }
    .nav-link {
        color: #4b5563;
        font-weight: 500;
        transition: color 0.2s;
    }
    .nav-link:hover {
        color: #4f46e5;
    }

    /* Hero Section styling */
    .hero-section {
        background-color: #4f46e5;
        color: white;
        padding: 5rem 2rem;
        text-align: center;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        font-weight: 300;
        margin-top: 1rem;
        max-width: 56rem;
        margin-left: auto;
        margin-right: auto;
    }
    .hero-button {
        background-color: white;
        color: #4f46e5;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 9999px;
        margin-top: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.2s;
    }
    .hero-button:hover {
        background-color: #f3f4f6;
    }

    /* Feature Cards styling */
    .feature-card {
        background-color: white;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-icon-box {
        width: 4rem;
        height: 4rem;
        background-color: #e0e7ff;
        border-radius: 9999px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem;
        color: #4f46e5;
    }
    .feature-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1f2937;
    }
    .feature-description {
        color: #6b7280;
    }
    
    /* Footer styling */
    .footer {
        background-color: white;
        padding: 2rem;
        text-align: center;
        color: #6b7280;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    st.markdown("""
        <div class="header">
            <div class="logo">Your Logo</div>
            <nav style="display: flex; gap: 1.5rem;">
                <a href="#" class="nav-link">Home</a>
                <a href="#" class="nav-link">About</a>
                <a href="#" class="nav-link">Services</a>
                <a href="#" class="nav-link">Contact</a>
            </nav>
        </div>
    """, unsafe_allow_html=True)

# --- Hero Section ---
with st.container():
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Your Compelling Headline Here</h1>
            <p class="hero-subtitle">
                A short and powerful sub-headline that explains what you do and why it matters.
            </p>
            <a href="#" class="hero-button">Get Started</a>
        </div>
    """, unsafe_allow_html=True)

# --- Main Content (Key Features) ---
st.container()
st.markdown("<h2 style='text-align: center; font-size: 1.875rem; font-weight: 700; margin-top: 3rem; color: #1f2937;'>Key Features</h2>", unsafe_allow_html=True)
st.markdown("<div style='display: flex; justify-content: space-around; gap: 2rem; padding: 2rem 0; flex-wrap: wrap;'>", unsafe_allow_html=True)

# Feature Card 1
st.markdown("""
    <div class="feature-card">
        <div class="feature-icon-box">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.674m-4.674 0L15 20m-5.337-3h4.674m-4.674 0L9.663 17"></path></svg>
        </div>
        <h3 class="feature-title">Feature One</h3>
        <p class="feature-description">Describe a key benefit or feature of your product or service here.</p>
    </div>
""", unsafe_allow_html=True)

# Feature Card 2
st.markdown("""
    <div class="feature-card">
        <div class="feature-icon-box">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        </div>
        <h3 class="feature-title">Feature Two</h3>
        <p class="feature-description">Explain another important aspect that makes your offering unique.</p>
    </div>
""", unsafe_allow_html=True)

# Feature Card 3
st.markdown("""
    <div class="feature-card">
        <div class="feature-icon-box">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.5 3-4.5s-1.343-4.5-3-4.5S9 12 9 12s1.343 4.5 3 4.5z"></path></svg>
        </div>
        <h3 class="feature-title">Feature Three</h3>
        <p class="feature-description">A final description to showcase your value proposition to customers.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class="footer">
        <p>&copy; 2024 Your Company. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
