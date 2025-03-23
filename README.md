# Enhancing Search Engine Relevance for Video Subtitles (Cloning Shazam) 🎥🎶

## 🚀 Overview
This project enhances search engine relevance by **indexing video subtitles** and **identifying audio using AI-based fingerprinting (like Shazam).**

## 🔥 Features
- **Search within video subtitles** using embeddings & vector DBs.
- **Upload videos** and extract SRT subtitles.
- **Identify audio from video clips**.
- **FastAPI backend** with a **Gemini AI-powered search**.
- **Interactive frontend** for user-friendly searching.

## 🛠 Tech Stack
- FastAPI (Backend)
- Maestra AI (Speech-to-Text)
- Gemini AI (Search Intelligence)
- Pinecone (Vector Database for search)
- FAISS (Embedding-based search)
- AcoustID (Audio Fingerprinting)
- FFmpeg (Audio Extraction)
- React.js (Frontend)

## 📦 Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Run the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```
3. Start the frontend:
   ```bash
   cd frontend && npm install && npm start
   ```
