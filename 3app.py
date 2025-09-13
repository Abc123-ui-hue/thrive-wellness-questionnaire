import streamlit as st

# Set a responsive page layout
st.set_page_config(layout="wide")

# Inject custom CSS for a background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Function to check if a user is logged in (placeholder) ---
def is_logged_in():
    """Placeholder function to simulate login state."""
    return st.session_state.get('logged_in', False)

# --- Define a simple dashboard for different roles (placeholder) ---
def patient_dashboard():
    st.title("Patient Dashboard")
    st.info("This is your personalized patient dashboard. Authentication is working!")
    st.write("---")
    st.header("Your Health Information")
    st.write("This is where your health records and appointments will be displayed.")

def staff_dashboard():
    st.title("Staff Dashboard")
    st.info("This is the staff dashboard. Authentication is working!")
    st.write("---")
    st.header("Team Management")
    st.write("This is where you can manage appointments and patient files.")

def admin_dashboard():
    st.title("Admin Dashboard")
    st.info("This is the admin dashboard. Authentication is working!")
    st.write("---")
    st.header("System Overview")
    st.write("This is where you can manage user accounts and system settings.")

# --- Function to handle user logout ---
def logout():
    st.session_state['logged_in'] = False
    st.session_state.pop('user_email', None)
    st.session_state.pop('user_role', None)
    st.success("You have been logged out.")
    st.rerun()

# --- Placeholder function for login ---
def login_user(email, password):
    st.info("Login functionality is not yet enabled. This is a placeholder.")
    # In a later version, this is where the Firebase authentication would happen.
    # For now, we will simulate a successful login to show the dashboard.
    st.session_state['logged_in'] = True
    st.session_state['user_email'] = email
    st.session_state['user_role'] = "patient"  # Default to patient for testing
    st.success("Login successful (simulated).")
    st.rerun()

# --- Placeholder function for registration ---
def register_user(email, password, role):
    st.info("Registration functionality is not yet enabled. This is a placeholder.")
    st.success(f"User {email} registered as {role} (simulated).")
    st.session_state['logged_in'] = True
    st.session_state['user_email'] = email
    st.session_state['user_role'] = role
    st.rerun()

# --- User Interface ---
if is_logged_in():
    user_role = st.session_state['user_role']
    st.sidebar.button("Logout", on_click=logout)

    if user_role == "patient":
        patient_dashboard()
    elif user_role == "staff":
        staff_dashboard()
    elif user_role == "admin":
        admin_dashboard()

else:
    # --- Home Page ---
    st.title("Welcome to Thrive Wellness")
    st.subheader("Your Partner in Health and Healing")
    st.write("---")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("Medication Management")
        st.write("Our expert team offers personalized medication management to ensure you receive the best care.")
        st.button("Learn More about Medication Management")

    with col2:
        st.header("Psychotherapy")
        st.write("We provide compassionate psychotherapy services to help you navigate life's challenges.")
        st.button("Learn More about Psychotherapy")

    st.write("---")
    st.header("Meet Our Team")
    st.write("Our dedicated staff is here to support you on your wellness journey.")
    st.markdown("**Cecilia Wamburu**, **Director, Psychiatric Nurse Practitioner**")
    st.write("Cecilia is passionate about providing holistic care and empowering individuals to achieve their full potential.")

    st.write("---")
    st.header("Testimonials")
    st.write("*\"Thrive Wellness changed my life. I finally feel like myself again.\"* - A.B.")
    st.write("*\"The staff is incredibly supportive and professional. I highly recommend them.\"* - C.D.")

    st.write("---")
    # --- Services Section ---
    st.title("Our Services")
    st.write("---")
    st.header("Mental Health Services")
    st.write("We offer a range of services designed to support your mental and emotional well-being.")
    st.subheader("Psychotherapy")
    st.write("Individual, couples, and group therapy to address various mental health concerns.")
    st.subheader("Medication Management")
    st.write("Professional and personalized medication plans to complement your treatment.")
    st.subheader("Telehealth")
    st.write("Secure virtual appointments for convenient and accessible care.")

    st.write("---")
    # --- About Us Section ---
    st.title("About Us")
    st.write("---")
    st.header("Our Mission")
    st.write("At Thrive Wellness, our mission is to provide compassionate, high-quality mental health care to our community. We believe in a holistic approach that treats the whole person.")
    st.header("Our Philosophy")
    st.write("We are committed to creating a safe and supportive environment where you can feel heard and understood. Our approach is collaborative and tailored to your unique needs.")

    st.write("---")
    # --- Contact Us Section ---
    st.title("Contact Us")
    st.write("---")
    st.write("Have a question? Fill out the form below or give us a call.")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button(label='Send Message')
        if submit_button:
            st.success("Your message has been sent (simulated).")

    # --- Main Navigation and Authentication Forms ---
    st.sidebar.title("Access Portals")
    login_mode = st.sidebar.radio("Select Portal", ["Login", "Register"])

    if login_mode == "Login":
        with st.sidebar.form("Login Form"):
            st.markdown("### Login")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
            if login_button:
                login_user(email, password)

    elif login_mode == "Register":
        with st.sidebar.form("Registration Form"):
            st.markdown("### Register")
            new_email = st.text_input("Email")
            new_password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            role = st.selectbox("Role", ["Patient", "Staff", "Admin"])
            register_button = st.form_submit_button("Register")

            if register_button:
                if new_password == confirm_password:
                    register_user(new_email, new_password, role)
                else:
