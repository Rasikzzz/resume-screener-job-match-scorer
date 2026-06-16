from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pdfplumber

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from uploaded PDF.
    """
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def get_embedding(text):
    """
    Convert text into embedding vector.
    """
    return model.encode(text)


def compute_match_score(resume_text, jd_text):
    """
    Calculate cosine similarity score.
    """
    resume_embedding = get_embedding(resume_text)
    jd_embedding = get_embedding(jd_text)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(similarity * 100, 2)