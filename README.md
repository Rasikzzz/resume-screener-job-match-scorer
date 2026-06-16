# NLP Resume Screener & Job Match Scorer

An AI-powered Resume Screening and Job Matching application that evaluates how well a candidate's resume aligns with a job description using Natural Language Processing (NLP) and semantic similarity analysis.

Built with Sentence Transformers, Scikit-learn, and Streamlit, the system provides recruiters and job seekers with an intelligent way to assess candidate-job fit beyond simple keyword matching.

---

## Features

- 📄 PDF Resume Parsing
- 🧠 Semantic Text Embeddings using Sentence Transformers (SBERT)
- 🎯 Resume-to-Job Match Scoring
- 📊 Cosine Similarity-Based Evaluation
- ⚡ Interactive Streamlit Dashboard
- 🔍 Semantic Analysis Instead of Basic Keyword Matching

---

## Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Sentence Transformers | Text Embeddings |
| Scikit-learn | Cosine Similarity Calculation |
| PDFPlumber | PDF Text Extraction |
| Streamlit | Web Application Interface |

---

## Project Workflow

```text
Resume PDF
    │
    ▼
Text Extraction
    │
    ▼
Sentence Transformer Embeddings
    │
    ▼
Job Description Embeddings
    │
    ▼
Cosine Similarity Analysis
    │
    ▼
Match Score Generation
```

---

## How It Works

1. Upload a candidate resume in PDF format.
2. Paste a job description into the application.
3. The system extracts text from the resume.
4. Both resume and job description are converted into semantic embeddings using a pre-trained Sentence Transformer model.
5. Cosine similarity is calculated between the embeddings.
6. A match score is generated to indicate the alignment between the candidate profile and the job requirements.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/nlp-resume-matcher.git
cd nlp-resume-matcher
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Example Use Case

**Job Description**

- Python
- Machine Learning
- Deep Learning
- SQL
- NLP

**Candidate Resume**

- Python
- Machine Learning
- Computer Vision
- OpenCV
- YOLO

**Output**

```text
Match Score: 78.45%

Status: Good Match
```

---

## Future Enhancements

- Skill Gap Detection
- Resume Improvement Suggestions
- Multi-Resume Ranking
- FAISS-Based Semantic Search
- Explainable Scoring System
- Recruiter Dashboard
- Support for DOCX Resumes
- Advanced Candidate Analytics

---

## Project Structure

```text
resume-matcher/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
│
└── data/
```

---

## Key Learning Outcomes

This project demonstrates:

- Natural Language Processing (NLP)
- Semantic Search Concepts
- Text Embeddings
- Information Retrieval
- Streamlit Application Development
- End-to-End AI Product Development

---

## Author

**Rasik**

Aspiring AI & Machine Learning Engineer passionate about building practical AI solutions in Computer Vision, NLP, and Predictive Analytics.

---

## License

This project is released under the MIT License.
