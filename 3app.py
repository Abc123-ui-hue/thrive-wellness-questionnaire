import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore

# --- Firebase Initialization ---
# This part of the code is for demonstration. In a real application,
# you would securely load your Firebase credentials.
if not firebase_admin._apps:
    # Use the provided global variables for Firebase configuration
    try:
        firebase_config = st.secrets["firebase_config"]
        cred = credentials.Certificate(firebase_config)
        firebase_admin.initialize_app(cred)
    except:
        st.error("Firebase credentials not found. Please add them to your Streamlit secrets.")
        st.stop()

db = firestore.client()

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'user_email' not in st.session_state:
    st.session_state.user_email = None
if 'page' not in st.session_state:
    st.session_state.page = 'home'

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
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
    }
    .logo {
        font-size: 2.5rem;
        font-weight: 800;
        color: #4f46e5;
        text-decoration: none;
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
        background-color: #eef2ff;
        padding: 5rem 2rem;
        border-radius: 10px;
        text-align: center;
        overflow: hidden;
        margin-top: 1rem;
    }
    .hero-title {
        font-size: 4rem;
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
        margin-top: -50px;
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
    
    /* Featured Staff Section */
    .staff-section {
        margin-top: 5rem;
        text-align: center;
    }
    .staff-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a237e;
        margin-bottom: 2rem;
    }
    .staff-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .staff-photo {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin-bottom: 1rem;
    }
    .staff-name {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a237e;
    }
    .staff-credentials {
        font-size: 1rem;
        color: #4f46e5;
        margin-bottom: 0.5rem;
    }
    .staff-bio {
        color: #4a5568;
    }

    /* Testimonials Section */
    .testimonials-section {
        background-color: #eef2ff;
        padding: 4rem 2rem;
        margin-top: 5rem;
        border-radius: 10px;
        text-align: center;
    }
    .testimonial-quote {
        font-style: italic;
        color: #4a5568;
        font-size: 1.25rem;
    }
    .testimonial-author {
        margin-top: 1rem;
        font-weight: 600;
        color: #1a237e;
    }

    /* Call to Action Section */
    .cta-section {
        margin-top: 5rem;
        text-align: center;
        background-color: #4f46e5;
        color: white;
        padding: 4rem 2rem;
        border-radius: 10px;
    }
    .cta-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .cta-button {
        background-color: white;
        color: #4f46e5;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        transition: background-color 0.2s, color 0.2s;
    }
    .cta-button:hover {
        background-color: #eef2ff;
    }

    /* Footer */
    .footer {
        background-color: #1a237e;
        color: white;
        padding: 2rem;
        text-align: center;
        margin-top: 5rem;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }
    .footer p {
        margin: 0;
    }

    /* Forms */
    .form-container {
        max-width: 500px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: #f8f9fa;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .form-title {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1.5rem;
        color: #1a237e;
    }
</style>
""", unsafe_allow_html=True)

# --- Functions for Authentication ---

def set_page(page_name):
    st.session_state.page = page_name

def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_email = None
    set_page('home')
    st.rerun()

def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        # In a real app, you would use a secure sign-in method.
        # This is a placeholder for demonstration.
        # Here we verify the password with a database query
        user_doc_ref = db.collection('users').document(user.uid)
        user_doc = user_doc_ref.get()
        if user_doc.exists and user_doc.to_dict().get('password') == password:
            user_data = user_doc.to_dict()
            st.session_state.logged_in = True
            st.session_state.user_role = user_data.get('role', 'patient')
            st.session_state.user_email = email
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid email or password.")
    except Exception as e:
        st.error(f"Error logging in: {e}")

def register_user(email, password, role="patient"):
    try:
        user = auth.create_user(email=email, password=password)
        # Store user details in Firestore
        user_data = {
            "email": email,
            "role": role,
            "password": password # In a real app, do NOT store plain text passwords
        }
        db.collection('users').document(user.uid).set(user_data)
        st.success("Registration successful! You can now log in.")
        set_page('login')
        st.rerun()
    except Exception as e:
        st.error(f"Error registering user: {e}")

# --- Page Rendering Functions ---

def render_home_page():
    # --- Header Section ---
    st.markdown("""
    <div class="header">
        <a href="#" class="logo">Thrive Mental Wellness</a>
        <div class="nav-links">
            <a href="#" class="nav-link">Home</a>
            <a href="#" class="nav-link">About Us</a>
            <a href="#" class="nav-link">Services</a>
            <a href="#" class="nav-link">Contact</a>
        </div>
        <div class="st-emotion-cache-1f19p2e">
            <a href="javascript:void(0)" onclick="window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'page', value: 'login'}, '*')" style="
                background-color: #4f46e5;
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
            ">Log In</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Hero Section ---
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">A Space for Your Healing</h1>
        <p class="hero-subtitle">Compassionate and evidence-based mental healthcare for a healthier you.</p>
        <div style="margin-top: 2rem;">
            <a href="#" style="
                background-color: #4f46e5;
                color: white;
                padding: 1rem 2rem;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
                margin-right: 1rem;
            ">Book Appointment</a>
            <a href="#" style="
                background-color: #ffffff;
                color: #4f46e5;
                padding: 1rem 2rem;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
                border: 2px solid #4f46e5;
            ">Contact Us</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Services Section ---
    st.markdown("""
    <div class="services-container">
        <h2 class="services-title">Our Services</h2>
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
            <div class="service-card" style="flex-basis: 350px;">
                <div class="service-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="48" height="48">
                        <path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM12 4.5a.75.75 0 0 1 .75.75V12h5.75a.75.75 0 0 1 0 1.5H12a.75.75 0 0 1-.75-.75V5.25a.75.75 0 0 1 .75-.75Z" />
                    </svg>
                </div>
                <h3 class="service-title">Medication Management</h3>
                <p class="service-description">Personalized medication plans for anxiety, depression, bipolar disorder, and other complex mental health issues. We focus on finding the right balance for your well-being.</p>
            </div>
            <div class="service-card" style="flex-basis: 350px;">
                <div class="service-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="48" height="48">
                        <path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM12 4.5a.75.75 0 0 1 .75.75V12h5.75a.75.75 0 0 1 0 1.5H12a.75.75 0 0 1-.75-.75V5.25a.75.75 0 0 1 .75-.75Z" />
                    </svg>
                </div>
                <h3 class="service-title">Psychotherapy</h3>
                <p class="service-description">Individual, group, and family therapy sessions with a focus on evidence-based practices like CBT and DBT to help you navigate life's challenges.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Featured Staff Section ---
    st.markdown("""
    <div class="staff-section">
        <h2 class="staff-title">Meet Our Founder</h2>
        <div style="display: flex; justify-content: center;">
            <div class="staff-card" style="flex-basis: 400px;">
                <img src="https://placehold.co/150x150/eef2ff/4f46e5?text=Staff+Photo" class="staff-photo">
                <h3 class="staff-name">Cecilia Wamburu</h3>
                <p class="staff-credentials">Psychiatric Mental Health Nurse Practitioner (PMHNP-BC)</p>
                <p class="staff-bio">Cecilia is a dedicated and compassionate PMHNP with a passion for helping individuals achieve mental wellness. She brings a wealth of experience in managing complex mental health issues through a blend of medication and therapy.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Testimonials Section ---
    st.markdown("""
    <div class="testimonials-section">
        <h2 class="services-title" style="color: #1a237e;">What Our Patients Say</h2>
        <div style="display: flex; justify-content: center;">
            <div style="max-width: 800px;">
                <p class="testimonial-quote">“Thrive Mental Wellness gave me a fresh start. The support and guidance I received was life-changing. Highly recommend.”</p>
                <p class="testimonial-author">- A.B., Patient</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Final Call to Action ---
    st.markdown("""
    <div class="cta-section">
        <h2 class="cta-title">Ready to Begin Your Journey?</h2>
        <p style="margin-bottom: 1.5rem;">Take the first step towards a healthier, happier you.</p>
        <a href="#" class="cta-button">Book Your Appointment Now</a>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Footer ---
    st.markdown("""
    <div class="footer">
        <p>&copy; 2024 Thrive Mental Wellness. All Rights Reserved.</p>
        <div style="margin-top: 1rem;">
            <a href="#" style="color: white; margin: 0 0.5rem;">Privacy Policy</a> |
            <a href="#" style="color: white; margin: 0 0.5rem;">Terms of Service</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_login_page():
    st.markdown('<div class="header"> <a href="#" class="logo">Thrive Mental Wellness</a> </div>', unsafe_allow_html=True)
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="form-title">Log In to Your Account</h2>', unsafe_allow_html=True)

    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        st.form_submit_button("Log In", on_click=login_user, args=(email, password))
    
    st.markdown('<div style="text-align:center; margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("Don't have an account? <a href='javascript:void(0)' onclick='window.parent.postMessage({type: \"streamlit:setComponentValue\", key: \"page\", value: \"register\"}, \"*\")'>Register here</a>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

def render_register_page():
    st.markdown('<div class="header"> <a href="#" class="logo">Thrive Mental Wellness</a> </div>', unsafe_allow_html=True)
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="form-title">Create a New Account</h2>', unsafe_allow_html=True)
    
    with st.form("register_form"):
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm_password")
        
        if st.form_submit_button("Register"):
            if password != confirm_password:
                st.error("Passwords do not match.")
            else:
                register_user(email, password)
    
    st.markdown('<div style="text-align:center; margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("Already have an account? <a href='javascript:void(0)' onclick='window.parent.postMessage({type: \"streamlit:setComponentValue\", key: \"page\", value: \"login\"}, \"*\")'>Log in here</a>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_patient_dashboard():
    st.markdown('<div class="header"> <a href="#" class="logo">Thrive Mental Wellness</a> </div>', unsafe_allow_html=True)
    st.markdown(f"<h2>Welcome, Patient {st.session_state.user_email}!</h2>", unsafe_allow_html=True)
    st.markdown("This is your patient dashboard. You can view your medical history, appointments, and communicate with your provider here.")
    if st.button("Logout"):
        logout()

def render_staff_dashboard():
    st.markdown('<div class="header"> <a href="#" class="logo">Thrive Mental Wellness</a> </div>', unsafe_allow_html=True)
    st.markdown(f"<h2>Welcome, Staff Member {st.session_state.user_email}!</h2>", unsafe_allow_html=True)
    st.markdown("This is your staff dashboard. You can manage patient profiles and schedules here.")
    if st.button("Logout"):
        logout()

def render_admin_dashboard():
    st.markdown('<div class="header"> <a href="#" class="logo">Thrive Mental Wellness</a> </div>', unsafe_allow_html=True)
    st.markdown(f"<h2>Welcome, Admin {st.session_state.user_email}!</h2>", unsafe_allow_html=True)
    st.markdown("This is your admin dashboard. You have full control over the system.")
    if st.button("Logout"):
        logout()

# --- Main Application Logic ---

if st.session_state.logged_in:
    if st.session_state.user_role == 'patient':
        render_patient_dashboard()
    elif st.session_state.user_role == 'staff':
        render_staff_dashboard()
    elif st.session_state.user_role == 'admin':
        render_admin_dashboard()
else:
    if st.session_state.page == 'login':
        render_login_page()
    elif st.session_state.page == 'register':
        render_register_page()
    else:
        render_home_page()
