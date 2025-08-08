from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# FastAPI app instance
app = FastAPI()

# Request body schema
class TextPair(BaseModel):
    text1: str
    text2: str

# Lemmatization function
def lemmatize_text(text: str) -> str:
    doc = nlp(text.lower())
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

# Route to compute similarity
@app.post("/similarity")
def get_similarity(data: TextPair):
    if not data.text1 or not data.text2:
        raise HTTPException(status_code=400, detail="Both text1 and text2 are required.")
    
    text1_clean = lemmatize_text(data.text1)
    text2_clean = lemmatize_text(data.text2)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1_clean, text2_clean])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    return {
        "text1": data.text1,
        "text2": data.text2,
        "similarity_score": round(score, 3)
    }
