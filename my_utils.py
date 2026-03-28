import re
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_resume_text(file_path):
    text = extract_text(file_path)
    return text if text else ""


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text


def get_similarity(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return similarity[0][0] * 100


def get_missing_skills(resume_text, skills_list):
    missing = []
    for skill in skills_list:
        if skill.lower() not in resume_text:
            missing.append(skill)
    return missing