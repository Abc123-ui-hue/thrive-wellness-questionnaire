%%writefile app.py
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# --- Gmail Config ---
EMAIL_SENDER = "meshmuth18@gmail.com"
EMAIL_PASSWORD = "ybvtflhdkccpblv"   # Your Google App Password (no spaces)
EMAIL_RECEIVER = "meshmuth18@gmail.com"

st.set_page_config(page_title="Thrive Mental Wellness – Client Questionnaire", layout="centered")

st.title("🧠 Thrive Mental Wellness LLC – Website Requirements Questionnaire")
st.write("Please answer the following questions to help us understand your requirements for the hospital website.")

# --- FORM ---
with st.form("questionnaire_form", clear_on_submit=True):
    st.subheader("1. General Information")
    purpose = st.text_area("What is the main purpose of your website?")
    domain = st.text_input("Do you already have a domain name? If yes, what is it?")
    hosting = st.text_input("Do you already have hosting, or should we set it up for you?")
    branding = st.text_input("Do you have a logo and branding (colors, fonts), or should we create it?")

    st.subheader("2. Website Content")
    pages = st.text_area("What pages should your website include?")
    services = st.text_area("What specific services should be highlighted on the site?")
    content = st.text_area("Do you already have written content (text, images, staff bios, etc.)?")
    staff_profiles = st.text_area("Should the website include staff profiles (psychiatrists, therapists, doctors, nurses)?")

    st.subheader("3. Patient Interaction Features")
    contact = st.text_area("How should patients or visitors contact you?")
    booking = st.text_input("Would you like an online appointment booking system?")
    portal = st.text_input("Do you want a secure patient portal?")
    payments = st.text_input("Should patients be able to make online payments?")

    st.subheader("4. Admin & Staff Features")
    dashboard = st.text_input("Do you want an admin dashboard where staff can manage patients, appointments, and content?")
    access_levels = st.text_input("Should different staff members have different access levels?")
    reminders = st.text_input("Would you like appointment reminders (SMS/email)?")

    st.subheader("5. Design & Branding")
    colors = st.text_input("Do you have preferred colors, fonts, or style guidelines?")
    inspiration = st.text_area("Do you have examples of websites you like?")
    tone = st.text_area("What overall tone should the design convey (professional, welcoming, calming, modern, etc.)?")

    st.subheader("6. Compliance & Security")
    hipaa = st.text_input("Does the website need to be HIPAA compliant?")
    legal = st.text_input("Should we include privacy policy and terms of service pages?")
    security = st.text_input("Do you need data encryption and secure login features?")

    st.subheader("7. Future Growth & Scalability")
    expansion = st.text_area("Do you plan to expand services (e.g., add more psychiatrists or treatments)?")
    telehealth = st.text_input("Would you like to add telehealth / virtual consultation features?")
    multilingual = st.text_input("Do you need multilingual support?")

    st.subheader("8. Other Requirements")
    blog = st.text_input("Do you need a blog or resource center?")
    social = st.text_input("Do you need social media integration?")
    analytics = st.text_input("Should the website include analytics?")
    extras = st.text_area("Any additional features or ideas you would like included?")

    submitted = st.form_submit_button("📩 Submit")

# --- ON SUBMIT ---
if submitted:
    st.success("✅ Thank you! Your responses have been submitted.")

    # Build email message
    submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"""
    Thrive Mental Wellness LLC - Client Questionnaire

    Submitted at: {submission_time}

    Purpose: {purpose}
    Domain: {domain}
    Hosting: {hosting}
    Branding: {branding}

    Pages: {pages}
    Services: {services}
    Content: {content}
    Staff Profiles: {staff_profiles}

    Contact: {contact}
    Booking: {booking}
    Patient Portal: {portal}
    Payments: {payments}

    Dashboard: {dashboard}
    Access Levels: {access_levels}
    Reminders: {reminders}

    Colors/Fonts: {colors}
    Inspiration: {inspiration}
    Tone: {tone}

    HIPAA: {hipaa}
    Legal: {legal}
    Security: {security}

    Expansion: {expansion}
    Telehealth: {telehealth}
    Multilingual: {multilingual}

    Blog: {blog}
    Social Media: {social}
    Analytics: {analytics}
    Extras: {extras}
    """

    # --- SEND EMAIL ---
    try:
        msg = MIMEText(message)
        msg["Subject"] = "New Client Questionnaire Submission - Thrive Mental Wellness"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        st.info("📧 The response has also been sent to your email.")
    except Exception as e:
        st.error(f"❌ Email failed: {e}")
