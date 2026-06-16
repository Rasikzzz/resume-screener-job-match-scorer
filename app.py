import streamlit as st
from utils import extract_text_from_pdf, compute_match_score

st.set_page_config(
    page_title="Resume Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Screener & Job Match Scorer")

st.markdown(
    """
    Upload a resume and paste a job description.
    The system uses NLP embeddings to calculate semantic similarity.
    """
)

# Upload PDF
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job Description
jd_text = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Calculate Match Score"):

    if resume_file is None:
        st.warning("Please upload a resume.")
        st.stop()

    if not jd_text.strip():
        st.warning("Please enter a job description.")
        st.stop()

    with st.spinner("Analyzing..."):

        resume_text = extract_text_from_pdf(resume_file)

        score = round(
            compute_match_score(
                resume_text,
                jd_text
            ),
            2
        )

    st.success(f"Match Score: {score:.2f}%")

    # Interpretation
    if score >= 80:
        st.success("🟢 Excellent Match")
    elif score >= 60:
        st.info("🟡 Good Match")
    elif score >= 40:
        st.warning("🟠 Moderate Match")
    else:
        st.error("🔴 Poor Match")

    # Show extracted resume text
    with st.expander("View Resume Text"):
        st.write(resume_text)

    # Show Job Description
    with st.expander("View Job Description"):
        st.write(jd_text)
