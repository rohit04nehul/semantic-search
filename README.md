# 📌 Semantic Similarity API (FastAPI + NLP)

This project implements a semantic similarity model using NLP techniques and serves it through a FastAPI endpoint. It quantifies how similar two input paragraphs are, on a scale from **0 to 1**, based on semantic understanding.

---

## 🚀 Features

- Preprocessing with **spaCy** (lemmatization, stopword removal, etc.)
- Vectorization using **TF-IDF**
- Similarity computation using **cosine similarity**
- REST API built with **FastAPI**
- Deployed on **AWS EC2**
- Tested using **Postman**

---

## 🔧 Tech Stack

- Python
- FastAPI
- spaCy (`en_core_web_sm`)
- scikit-learn
- Uvicorn

---

## 📦 Requirements

```bash
pip install -r requirement.txt
python -m spacy download en_core_web_sm
