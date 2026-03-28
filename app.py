import streamlit as st
import tempfile

from my_utils import extract_resume_text, clean_text, get_similarity, get_missing_skills
from skills import skills_list


st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Smart Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")


# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description
job_desc = st.text_area("Paste Job Description")


if uploaded_file is not None and job_desc.strip() != "":
    
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Extract and clean text
    resume_text = extract_resume_text(tmp_path)
    resume_text = clean_text(resume_text)

    job_desc_clean = clean_text(job_desc)

    # Calculate similarity
    score = get_similarity(resume_text, job_desc_clean)

    # Missing skills
    missing_skills = get_missing_skills(resume_text, skills_list)

    # Display results
    st.subheader("📊 Match Score")
    st.write(f"{score:.2f}%")
    st.progress(min(int(score), 100))

    st.subheader("⚠️ Missing Skills")
    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.success("No major skills missing 🎉")

    st.subheader("💡 Suggestions")
    if score < 50:
        st.warning("Your resume needs improvement. Add relevant skills and projects.")
    elif score < 75:
        st.info("Good, but can be improved by adding more relevant keywords.")
    else:
        st.success("Excellent match! Your resume fits the job well.")
        






        #dot_product
        
        import numpy as np

        list1= [3,4,5]
        vector1=np.array(list1)

        list2=[7,8,-9]
        vector2=np.array(list2)

        dot_product = 0

        for i in range(3):
             dot_product += vector1[i] * vector2[i]

        print("vector1 1 =", vector1)
        print("vector2 2 =",vector2)
        print("Dot Product =",dot_product)



