import streamlit as st
import base64

# --- Helper functions for multi-page app ---
def show_home_page():
    st.image("https://placehold.co/1200x400/D0E0D7/2c3e50?text=Thrive+Mental+Health+Wellness", caption="A safe space for healing and growth", use_container_width=True)
    st.title("Thrive Mental Health Wellness")
    st.markdown("""
    <p style="font-size:1.25rem; color:#555;">
        Your path to well-being begins here. We provide compassionate and expert care for
        individuals and families in the USA, helping you find balance, resilience, and joy.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Overview and CTAs
    st.header("Our Services")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Psychotherapy: Individual, Group & Family sessions.")
    with col2:
        st.info("Medication Management: Expert evaluation and support.")
        
    st.markdown("---")
    
    st.subheader("Featured Staff")
    col3, col4 = st.columns([1, 2])
    with col3:
        st.image("https://placehold.co/200x200/B8D8D3/2c3e50?text=C.W.", caption="Cecilia Wamburu, PMHNP-BC", use_container_width=True)
    with col4:
        st.markdown(
            """
            <h4 style='color: #2c3e50;'>Cecilia Wamburu, PMHNP-BC</h4>
            <p>
                Cecilia is a board-certified Psychiatric-Mental Health Nurse Practitioner with a passion for holistic care. 
                She specializes in medication management and providing compassionate support to clients.
            </p>
            """, unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("Testimonials")
    st.markdown(
        """
        <div style="background-color: #f7f9fc; padding: 15px; border-radius: 12px; margin-bottom: 10px;">
            <p style="font-style: italic;">"Thrive has truly changed my life. The support and care I received were exceptional."</p>
            <p style="text-align: right; font-weight: bold;">- A.B., Patient</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # Social Media Links
    st.markdown(
        """
        <div style="text-align:center;">
            <p style="font-size:1.1rem;">Follow us on social media:</p>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/linkedin.png" style="width: 32px; height: 32px; margin: 0 5px;"></a>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/facebook-new.png" style="width: 32px; height: 32px; margin: 0 5px;"></a>
            <a href="#"><img src="https://img.icons8.com/color/48/000000/twitter.png" style="width: 32px; height: 32px; margin: 0 5px;"></a>
        </div>
        """, unsafe_allow_html=True
    )

def show_about_us_page():
    st.header("About Us")
    st.subheader("Our Mission")
    st.write("At Thrive, our mission is to provide accessible, evidence-based mental health care that addresses the whole person. We are committed to creating a supportive and stigma-free environment where every individual feels seen, heard, and valued.")
    
    st.subheader("Our Team")
    st.write("We have a dedicated team of licensed professionals committed to your well-being.")
    st.image("https://placehold.co/800x400/D0E0D7/2c3e50?text=Clinic+Environment", use_container_width=True)

def show_services_page():
    st.header("Our Services")
    st.markdown("---")
    
    st.subheader("Medication Management")
    st.write("Our team of psychiatrists can provide comprehensive evaluations and medication management as part of a holistic treatment plan, ensuring you receive well-rounded care.")
    
    st.subheader("Psychotherapy")
    st.write("We offer individual, group, and family counseling tailored to your unique needs and goals. Our therapists cover a wide range of issues including anxiety, depression, grief, and trauma.")
    
    st.subheader("Telehealth / Online Therapy")
    st.write("Secure and convenient online therapy sessions available from the comfort of your home. Our platform is easy to use and fully encrypted.")

def show_contact_page():
    st.header("Contact Us")
    st.subheader("Get in Touch")
    st.markdown(
        """
        <p><strong>Phone:</strong> (123) 456-7890</p>
        <p><strong>Email:</strong> info@thrivewellness.com</p>
        <p><strong>Emergency Hotline:</strong> 988 Suicide & Crisis Lifeline</p>
        <p><strong>Address:</strong> 123 Health Ave, Wellness City, USA</p>
        """, unsafe_allow_html=True
    )
    st.markdown("---")
    
    st.subheader("Send us a message")
    with st.form("contact_form"):
        name = st.text_input("Your Full Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Submit Request")
        if submitted:
            st.success("Thank you! Your request has been sent. We will be in touch shortly.")

def show_patient_portal_login():
    st.header("Patient Portal Login")
    st.warning("This is a demonstration. Please do not enter real patient data. A real-world application requires secure, HIPAA-compliant authentication and data storage.")
    
    with st.form("login_form"):
        st.write("Please enter your credentials to access the portal.")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")
        
        if login_button:
            if username and password:
                # This is a placeholder for real authentication logic.
                # For a real application, you would connect to a database here.
                st.success("Login successful! Redirecting to your dashboard...")
                st.info("Functionality for a user dashboard, appointments, and reports would be implemented here.")
            else:
                st.error("Please enter both email and password.")


# --- Main App Logic ---
st.set_page_config(page_title="Thrive Mental Health Wellness", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a professional look
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton>button {
        background-color: #6a8c7b;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #5d7a6a;
        transform: scale(1.05);
    }
    h1, h2, h3, h4 {
        color: #2c3e50;
    }
    .stExpander {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    .stImage {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stSelectbox, .stTextInput, .stTextArea {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .footer {
        text-align: center;
        padding: 10px;
        font-size: 0.9rem;
        color: #777;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", ["Home", "About Us", "Services", "Contact", "Patient Portal Login"])

# Display pages based on selection
if page_selection == "Home":
    show_home_page()
elif page_selection == "About Us":
    show_about_us_page()
elif page_selection == "Services":
    show_services_page()
elif page_selection == "Contact":
    show_contact_page()
elif page_selection == "Patient Portal Login":
    show_patient_portal_login()

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
