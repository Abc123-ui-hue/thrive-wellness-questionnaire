import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Thrive Medical Center",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="st-emotion-cache"] {
        font-family: 'Inter', sans-serif;
    }
    
    .st-emotion-cache-121p51f {
        background-color: #ffffff;
    }
    
    /* Header Section */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: white;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .logo {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a237e;
    }
    .nav-links {
        display: flex;
        gap: 1.5rem;
    }
    .nav-link {
        color: #4a5568;
        font-weight: 500;
        text-decoration: none;
        transition: color 0.2s;
    }
    .nav-link:hover {
        color: #4f46e5;
    }
    
    /* Hero Section */
    .hero-container {
        position: relative;
        background-color: #f0f4f8;
        padding: 5rem 2rem;
        border-radius: 10px;
        text-align: center;
        overflow: hidden;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1a237e;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        color: #4a5568;
    }

    /* Floating Stats */
    .stats-card-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: -50px; /* Overlaps with the hero section */
        position: relative;
        z-index: 10;
    }
    .stats-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        padding: 1.5rem;
        width: 250px;
        text-align: center;
        transition: transform 0.3s;
    }
    .stats-card:hover {
        transform: translateY(-5px);
    }
    .stats-number {
        font-size: 2rem;
        font-weight: 700;
        color: #4f46e5;
    }
    .stats-text {
        color: #718096;
    }

    /* Services Section */
    .services-container {
        margin-top: 5rem;
        text-align: center;
    }
    .services-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a237e;
        margin-bottom: 2rem;
    }
    .service-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        text-align: left;
        transition: transform 0.3s;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .service-card:hover {
        transform: translateY(-5px);
    }
    .service-icon {
        color: #4f46e5;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .service-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a237e;
        margin-bottom: 0.5rem;
    }
    .service-description {
        color: #4a5568;
        line-height: 1.6;
    }
    
    /* Footer */
    .footer {
        background-color: #1a237e;
        color: white;
        padding: 2rem;
        text-align: center;
        margin-top: 5rem;
    }
    .footer p {
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div class="header">
    <div class="logo">Thrive Medical Center</div>
    <div class="nav-links">
        <a href="#" class="nav-link">Home</a>
        <a href="#" class="nav-link">About</a>
        <a href="#" class="nav-link">Services</a>
        <a href="#" class="nav-link">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">Your Health, Our Priority</h1>
    <p class="hero-subtitle">Comprehensive and compassionate care for a healthier you. We are here for you.</p>
</div>
""", unsafe_allow_html=True)

# --- Floating Stats ---
st.markdown("""
<div class="stats-card-container">
    <div class="stats-card">
        <div class="stats-number">50+</div>
        <div class="stats-text">Expert Doctors</div>
    </div>
    <div class="stats-card">
        <div class="stats-number">20+</div>
        <div class="stats-text">Specialized Services</div>
    </div>
    <div class="stats-card">
        <div class="stats-number">10k+</div>
        <div class="stats-text">Happy Patients</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("""
<div class="services-container">
    <h2 class="services-title">Our Specialized Services</h2>
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <div class="service-card" style="flex-basis: 300px;">
            <div class="service-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="48" height="48">
                  <path fill-rule="evenodd" d="M11.47 2.47a.75.75 0 0 1 1.06 0l7.5 7.5a.75.75 0 1 1-1.06 1.06L12 4.06l-6.97 6.97a.75.75 0 0 1-1.06-1.06l7.5-7.5Z" clip-rule="evenodd" />
                  <path fill-rule="evenodd" d="M12 5.25v7.5a.75.75 0 0 1-1.5 0V5.25a.75.75 0 0 1 1.5 0Z" clip-rule="evenodd" />
                  <path d="m1.873 13.567 2.536 2.535a.75.75 0 0 0 1.06 0l2.493-2.492a.75.75 0 0 0-1.06-1.06L4.433 14.512l-1.92-1.921a.75.75 0 1 0-1.06 1.06Z" />
                  <path d="M12.75 12.75V12a.75.75 0 0 1 1.5 0v.75h4.5a.75.75 0 0 1 .75.75v3.375a.75.75 0 0 1-.75.75h-4.5a.75.75 0 0 1-.75-.75v-3.375ZM18 13.5h-4.5V12h4.5v1.5Z" />
                  <path d="M12 15a.75.75 0 0 1 .75.75v3.375a.75.75 0 0 1-.75.75h-4.5a.75.75 0 0 1-.75-.75v-3.375A.75.75 0 0 1 7.5 15H12Z" />
                </svg>
            </div>
            <h3 class="service-title">General Check-ups</h3>
            <p class="service-description">Regular health examinations to monitor your well-being and detect any issues early.</p>
        </div>
        <div class="service-card" style="flex-basis: 300px;">
            <div class="service-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="48" height="48">
                  <path d="M7.5 2.25c-.75 0-1.5.75-1.5 1.5v16.5c0 .75.75 1.5 1.5 1.5h9c.75 0 1.5-.75 1.5-1.5V3.75c0-.75-.75-1.5-1.5-1.5h-9ZM9 6a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0V6.75a.75.75 0 0 1 .75-.75ZM9 9.75a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0V10.5a.75.75 0 0 1 .75-.75ZM9 13.5a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0v-.75a.75.75 0 0 1 .75-.75ZM9 17.25a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0v-.75a.75.75 0 0 1 .75-.75ZM15 6a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0V6.75a.75.75 0 0 1 .75-.75ZM15 9.75a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0V10.5a.75.75 0 0 1 .75-.75ZM15 13.5a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0v-.75a.75.75 0 0 1 .75-.75ZM15 17.25a.75.75 0 0 1 .75.75v.75a.75.75 0 0 1-1.5 0v-.75a.75.75 0 0 1 .75-.75Z" />
                </svg>
            </div>
            <h3 class="service-title">Specialized Treatments</h3>
            <p class="service-description">Advanced diagnostic and treatment options for complex health conditions.</p>
        </div>
        <div class="service-card" style="flex-basis: 300px;">
            <div class="service-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="48" height="48">
                  <path d="M18.75 12.75h-12a.75.75 0 0 1 0-1.5h12a.75.75 0 0 1 0 1.5Z" />
                  <path d="M6.75 15.75a.75.75 0 0 1 0-1.5h1.5a.75.75 0 0 1 0 1.5h-1.5Z" />
                  <path d="M12.75 15.75h3a.75.75 0 0 1 0 1.5h-3a.75.75 0 0 1 0-1.5Z" />
                  <path d="M12.75 18.75a.75.75 0 0 1 0-1.5h3a.75.75 0 0 1 0 1.5h-3Z" />
                  <path fill-rule="evenodd" d="M18 3.75c.981 0 1.764.57 2.023 1.341a.75.75 0 0 1 .286.993c-.412.825-.935 1.63-1.564 2.413A17.926 17.926 0 0 0 12 10.5a17.926 17.926 0 0 0-4.495 1.997c-.629-.783-1.152-1.588-1.564-2.413a.75.75 0 0 1 .286-.993C4.236 4.32 5.019 3.75 6 3.75h12ZM6 3.75v16.5A.75.75 0 0 0 6.75 21h10.5a.75.75 0 0 0 .75-.75V3.75h-12Z" clip-rule="evenodd" />
                </svg>
            </div>
            <h3 class="service-title">Preventative Care</h3>
            <p class="service-description">Focus on maintaining your health and preventing illness with our preventative programs.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>&copy; 2024 Thrive Medical Center. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
