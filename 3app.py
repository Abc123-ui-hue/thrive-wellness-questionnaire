import streamlit as st

# --- Page Configuration and Styles ---
st.set_page_config(
    page_title="Thrive Mental Wellness LLC",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS for a modern, clean look and feel, and to use Tailwind classes
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body {
        font-family: 'Inter', sans-serif;
    }

    .st-emotion-cache-121p51f {
        background-color: #f9fafb;
    }

    .st-emotion-cache-18ni7ap {
        background-color: #ffffff;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    }

    .st-emotion-cache-r4231b {
        padding-top: 0rem;
    }

    .st-emotion-cache-16p64u8 {
        padding-top: 2rem;
    }

    .st-emotion-cache-1wivd2d {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }

    /* Additional custom styles to mimic Tailwind components */
    .container {
        width: 100%;
        max-width: 1280px;
        margin-left: auto;
        margin-right: auto;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .text-center { text-align: center; }
    .text-xl { font-size: 1.25rem; line-height: 1.75rem; }
    .text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
    .text-4xl { font-size: 2.25rem; line-height: 2.5rem; }
    .text-5xl { font-size: 3rem; line-height: 1; }
    .font-bold { font-weight: 700; }
    .font-extrabold { font-weight: 800; }
    .rounded-full { border-radius: 9999px; }
    .shadow-lg { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }
    .bg-indigo-600 { background-color: #4f46e5; }
    .text-white { color: #ffffff; }
    .text-gray-900 { color: #111827; }
    .text-gray-600 { color: #4b5563; }
    .p-8 { padding: 2rem; }
    .rounded-xl { border-radius: 0.75rem; }
    .shadow-lg { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }
    .hover\:scale-105:hover { transform: scale(1.05); }
    .transition-transform { transition-property: transform; transition-duration: 300ms; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); }
    .transform { transform: var(--tw-transform); }
    .flex { display: flex; }
    .flex-col { flex-direction: column; }
    .lg\:flex-row { flex-direction: row; }
    .items-center { align-items: center; }
    .gap-12 { gap: 3rem; }
    .lg\:w-1\/2 { width: 50%; }
    .text-center { text-align: center; }
    .mt-4 { margin-top: 1rem; }
    .py-20 { padding-top: 5rem; padding-bottom: 5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.markdown(
    """
    <header style="background-color: #ffffff; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06); position: sticky; top: 0; z-index: 50;">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <a href="#" style="font-size: 1.25rem; line-height: 1.75rem; font-weight: 700; color: #4f46e5;">Thrive Mental Wellness</a>
            <a href="#" style="background-color: #4f46e5; color: #ffffff; padding: 0.5rem 1.25rem; border-radius: 9999px; font-weight: 500; transition-colors: 0.2s;">
                Schedule a Consultation
            </a>
        </div>
    </header>
    """,
    unsafe_allow_html=True,
)

# --- Main Content ---
# Hero Section
st.markdown('<section style="background-color: #eef2ff; padding: 6rem 1rem;">', unsafe_allow_html=True)
st.markdown('<div class="container text-center">', unsafe_allow_html=True)
st.markdown(
    """
    <h1 style="font-size: 3.75rem; line-height: 1; font-weight: 800; color: #111827;">
        Find Your Path to Mental Wellness
    </h1>
    <p style="margin-top: 1rem; font-size: 1.5rem; line-height: 2rem; color: #4b5563; max-width: 42rem; margin-left: auto; margin-right: auto;">
        Compassionate and evidence-based psychiatric care for a healthier mind.
    </p>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style="margin-top: 2rem;">
        <a href="#" style="background-color: #4f46e5; color: #ffffff; font-size: 1.125rem; font-weight: 700; padding: 1rem 2rem; border-radius: 9999px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05); transition: transform 0.3s ease-in-out;">
            Schedule an Appointment
        </a>
    </div>
    </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# About Us/Philosophy Section
st.markdown('<section style="padding: 5rem 1rem;">', unsafe_allow_html=True)
about_col1, about_col2 = st.columns(2)
with about_col1:
    st.image("https://placehold.co/600x400/D1D5DB/1F2937?text=Professional+Office+Photo", caption="Professional Office", use_column_width=True)
with about_col2:
    st.markdown(
        """
        <div style="text-align: left;">
            <h2 style="font-size: 2.25rem; line-height: 2.5rem; font-weight: 700; color: #111827;">Our Compassionate Approach</h2>
            <p style="margin-top: 1rem; color: #4b5563; font-size: 1.125rem;">
                At Thrive Mental Wellness, we believe in a holistic and personalized approach to mental health. Our team is dedicated to providing a safe, supportive, and confidential environment where you can explore your challenges and develop effective strategies for a happier, more fulfilling life.
            </p>
            <a href="#" style="margin-top: 1.5rem; display: inline-block; color: #4f46e5; font-weight: 500; text-decoration: underline;">
                Learn More About Us &rarr;
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown('</section>', unsafe_allow_html=True)

# Services Section
st.markdown('<section style="background-color: #f3f4f6; padding: 5rem 1rem;">', unsafe_allow_html=True)
st.markdown('<div class="container text-center">', unsafe_allow_html=True)
st.markdown(
    """
    <h2 style="font-size: 2.25rem; line-height: 2.5rem; font-weight: 700; color: #111827;">What We Treat</h2>
    <p style="margin-top: 1rem; color: #4b5563; font-size: 1.125rem; max-width: 48rem; margin-left: auto; margin-right: auto;">
        Our team provides expert care for a wide range of mental health concerns, using evidence-based practices to support your well-being.
    </p>
    """,
    unsafe_allow_html=True,
)

service_cols = st.columns(3)
service_data = [
    ("Anxiety Disorders", "We offer support for generalized anxiety, panic disorders, and social anxiety through therapy and medication management.", "M13 10V3L4 14h7v7l9-11h-7z"),
    ("Depression Care", "Our team uses an integrated approach to provide support and management for various forms of depression.", "M9.663 17h4.674m-4.674 0l-1.393 2.322a1.5 1.5 0 00.902 2.122l4.674-2.322m-4.674 0H5.508c-1.125 0-2.046-1.071-1.905-2.224l.43-3.664M9.663 17H8.27a1.5 1.5 0 01-1.16-2.528l.182-.364a1.5 1.5 0 011.16-2.528h2.388c1.125 0 2.046-1.071 1.905-2.224l-.43-3.664M9.663 17h4.674m-4.674 0L15.75 7.5l-.265-.133a1.5 1.5 0 01-.115-2.224L15.75 5.25m-1.42 2.25L17.25 1.5"),
    ("Trauma & PTSD", "We provide compassionate, trauma-informed care to help you process and heal from past experiences.", "M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.5 3-4.5s-1.343-4.5-3-4.5S9 12 9 12s1.343 4.5 3 4.5z"),
]
for i, (title, description, svg_path) in enumerate(service_data):
    with service_cols[i]:
        st.markdown(
            f"""
            <div class="bg-white p-8 rounded-xl shadow-lg hover:scale-105 transform transition-transform duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-indigo-500 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="{svg_path}" />
                </svg>
                <h3 style="margin-top: 1.5rem; font-size: 1.25rem; font-weight: 700; color: #111827;">{title}</h3>
                <p style="margin-top: 0.5rem; color: #4b5563;">{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown('</div></section>', unsafe_allow_html=True)

# Testimonial Section
st.markdown('<section style="padding: 5rem 1rem;">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="container text-center" style="max-width: 56rem;">
        <blockquote style="font-size: 2.25rem; font-weight: 600; color: #111827; font-style: italic;">
            "Thrive Mental Wellness provided the compassionate, expert care I needed to feel like myself again. I am so grateful for their support."
        </blockquote>
        <p style="margin-top: 2rem; font-size: 1.25rem; color: #4b5563;">- Anonymized Client</p>
    </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Final CTA Section
st.markdown('<section style="background-color: #4f46e5; padding: 5rem 1rem;">', unsafe_allow_html=True)
st.markdown('<div class="container text-center">', unsafe_allow_html=True)
st.markdown(
    """
    <h2 style="font-size: 2.25rem; font-weight: 700; color: #ffffff;">Ready to Begin Your Journey?</h2>
    <p style="margin-top: 1rem; color: #ffffff; font-size: 1.125rem; max-width: 48rem; margin-left: auto; margin-right: auto;">
        Taking the first step is often the hardest. Contact us today to schedule a confidential consultation.
    </p>
    <a href="#" style="margin-top: 2rem; display: inline-block; background-color: #ffffff; color: #4f46e5; font-size: 1.125rem; font-weight: 700; padding: 1rem 2rem; border-radius: 9999px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05); transition: transform 0.3s ease-in-out;">
        Contact Us Today
    </a>
    </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# --- Footer ---
st.markdown(
    """
    <footer style="background-color: #111827; color: #d1d5db; padding: 3rem 1rem; text-align: center;">
        <div class="container mx-auto">
            <p>&copy; 2024 Thrive Mental Wellness LLC. All Rights Reserved.</p>
            <div style="margin-top: 1rem; display: flex; justify-content: center; gap: 1.5rem;">
                <a href="#" style="color: #6b7280; transition-colors: 0.2s;">Privacy Policy</a>
                <a href="#" style="color: #6b7280; transition-colors: 0.2s;">HIPAA Compliance</a>
                <a href="#" style="color: #6b7280; transition-colors: 0.2s;">Terms of Service</a>
            </div>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
