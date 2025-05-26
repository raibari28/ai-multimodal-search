# Setup Instructions for AI Multimodal Search Agent

## 1. Prerequisites
- Python 3.9+
- Node.js 18+
- OpenAI API Key
- (Optional) Whisper, Tesseract, Playwright for extended tools

## 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### Add `.env` with OpenAI key:
```
OPENAI_API_KEY=your-key-here
```

### Run FastAPI server:
```bash
uvicorn main:app --reload
```

## 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

Make sure backend is running at `localhost:8000`.

## 4. Optional Enhancements
- Add Playwright to `/backend/agent/tools.py` for advanced web crawling
- Add Whisper for audio transcript
- Add image captioning or OCR for image-based search

## 5. Build & Deploy
- Backend: Render, Railway, Heroku
- Frontend: Netlify, Vercel, Firebase
