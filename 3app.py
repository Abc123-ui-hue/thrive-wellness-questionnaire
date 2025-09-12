import streamlit as st

# --- Page Configuration and Styles ---
st.set_page_config(
    page_title="Medical Center",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS for the exact look of the image
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="st-emotion-cache"] {
        font-family: 'Inter', sans-serif;
    }

    /* Overall page background and padding */
    .main .st-emotion-cache-121p51f {
        background-color: #ffffff;
        padding: 0;
    }

    /* Remove default Streamlit padding from main content area */
    .st-emotion-cache-r4231b {
        padding-top: 0;
        padding-bottom: 0;
        padding-left: 0;
        padding-right: 0;
    }

    /* Custom classes for layout and styling */
    .container {
        width: 100%;
        max-width: 1280px;
        margin-left: auto;
        margin-right: auto;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .text-center { text-align: center; }
    .text-4xl { font-size: 2.25rem; }
    .text-5xl { font-size: 3rem; }
    .text-6xl { font-size: 4rem; }
    .font-bold { font-weight: 700; }
    .font-extrabold { font-weight: 800; }
    .rounded-full { border-radius: 9999px; }
    .shadow-lg { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }

    /* Custom Hero section styling */
    .hero-container {
        display: flex;
        align-items: center;
        background-color: #e6f7ff;
        padding-top: 5rem;
        padding-bottom: 5rem;
    }

    .hero-content {
        padding-right: 2rem;
    }

    .hero-image-container {
        position: relative;
        flex-shrink: 0;
    }

    .stat-circle {
        position: absolute;
        width: 150px;
        height: 150px;
        border-radius: 50%;
        color: white;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        padding: 1rem;
    }

    .stat-circle h3 {
        font-size: 2rem;
        margin-bottom: 0.25rem;
    }
    .stat-circle p {
        font-size: 0.875rem;
    }

    .circle-1 {
        background-color: #ff3366;
        top: 25%;
        left: -10%;
        transform: translateY(-50%);
    }

    .circle-2 {
        background-color: #33aaff;
        top: 30%;
        right: -10%;
        transform: translateY(-50%);
    }

    .circle-3 {
        background-color: #cc0066;
        bottom: 10%;
        right: 0;
        transform: translateY(-50%);
    }

    /* Services Section Styling */
    .services-grid {
        display: flex;
        justify-content: space-around;
        padding: 2rem 0;
    }

    .service-card {
        text-align: center;
        padding: 2rem;
        border-radius: 1rem;
        background-color: #fff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 30%;
    }
    .service-card .icon {
        font-size: 2.5rem;
        color: #ff3366;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header Section ---
st.markdown(
    """
    <header style="background-color: #ffffff; padding: 1.5rem 0;">
        <div class="container flex justify-between items-center">
            <div style="font-size: 1.25rem; font-weight: 700; color: #4b5563;">
                #1 Medical Center
            </div>
            <nav style="display: flex; gap: 1.5rem;">
                <a href="#" style="color: #4b5563;">Home</a>
                <a href="#" style="color: #4b5563;">About us</a>
                <a href="#" style="color: #4b5563;">Services</a>
                <a href="#" style="color: #4b5563;">Doctors</a>
                <a href="#" style="color: #4b5563;">Contact us</a>
            </nav>
            <div style="background-color: #4f46e5; color: #ffffff; padding: 0.5rem 1.25rem; border-radius: 9999px; font-weight: 500;">
                Sign Up
            </div>
        </div>
    </header>
    """,
    unsafe_allow_html=True,
)

# --- Hero Section ---
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
hero_col1, hero_col2 = st.columns([1, 1])

with hero_col1:
    st.markdown(
        """
        <div class="hero-content">
            <h1 style="color: #1a202c; font-size: 3rem; font-weight: 800; line-height: 1.2;">
                WE CARE ABOUT<br>YOUR HEALTH
            </h1>
            <p style="color: #4b5563; margin-top: 1rem;">
                Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt.
            </p>
            <div style="margin-top: 2rem; display: flex; gap: 1rem;">
                <button style="background-color: #4f46e5; color: white; padding: 0.75rem 2rem; border-radius: 9999px; font-weight: 600; border: none;">Get An Appointment</button>
                <button style="background-color: #ff007f; color: white; padding: 0.75rem 2rem; border-radius: 9999px; font-weight: 600; border: none;">More Info</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_col2:
    st.markdown(
        """
        <div class="hero-image-container">
            <img src="https://placehold.co/400x500/E5E7EB/4B5563?text=Professional+Doctor" alt="Doctor" style="width: 100%; height: auto; border-radius: 1rem;">
            <div class="stat-circle circle-1" style="background-color: #ff007f;">
                <h3>120+</h3>
                <p>Doctors & Nurses</p>
            </div>
            <div class="stat-circle circle-2" style="background-color: #4f46e5;">
                <h3>800+</h3>
                <p>Patients Beds</p>
            </div>
            <div class="stat-circle circle-3" style="background-color: #ff007f;">
                <h3>45+</h3>
                <p>Years of Experience</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown('</div>', unsafe_allow_html=True)


# --- Services Section ---
st.markdown('<div class="container services-grid">', unsafe_allow_html=True)

service_data = [
    {
        "title": "DIAGNOSIS",
        "description": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt.",
        "icon": "🩺",
    },
    {
        "title": "MEDICINE",
        "description": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt.",
        "icon": "💊",
    },
    {
        "title": "PATHOLOGY",
        "description": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt.",
        "icon": "➕",
    },
]

for service in service_data:
    st.markdown(
        f"""
        <div class="service-card">
            <div class="icon">{service["icon"]}</div>
            <h3 style="margin-top: 1rem; font-weight: 700; color: #1a202c;">{service["title"]}</h3>
            <p style="margin-top: 0.5rem; color: #4b5563;">{service["description"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)
