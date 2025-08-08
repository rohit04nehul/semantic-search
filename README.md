# 📌 Semantic Similarity API (FastAPI + NLP)

This project implements a semantic similarity model using NLP techniques and serves it through a FastAPI endpoint. It quantifies how similar two input paragraphs are, on a scale from **0 to 1**, based on semantic understanding.

---

## 🚀 Features

- Preprocessing with **spaCy** (lemmatization, stopword removal, etc.)
- Vectorization with **TF-IDF**
- Similarity computation using **cosine similarity**
- REST API using **FastAPI**
- Deployed on **AWS EC2**
- Tested using **Postman**

---

## 🔧 Tech Stack

- Python
- FastAPI
- spaCy (`en_core_web_sm`)
- Scikit-learn
- Uvicorn

---

## 📦 Requirements

```bash
pip install -r requirement.txt
python -m spacy download en_core_web_sm


## ▶️ How to Run Locally

```bash
uvicorn app:app --host 0.0.0.0 --port 8000


## 📮 API Endpoint

- **Base URL**: `http://<your-server-ip>:8000`
- **Endpoint**: `/similarity`
- **Method**: `POST`
- **Content-Type**: `application/json`


---

### ✅ Request Example

```json
{
  "text1": "Artificial intelligence is transforming industries worldwide.",
  "text2": "AI is changing how businesses operate across the globe."
}

---

### ✅ Response Example

{
  "text1": "Artificial intelligence is transforming industries worldwide.",
  "text2": "AI is changing how businesses operate across the globe.",
  "similarity_score": 0.872
}

---
