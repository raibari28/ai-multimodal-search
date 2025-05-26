# AI Multimodal Web Search Agent

A full-stack project that uses OpenAI GPT-4 and DuckDuckGo to search the web, summarize results, and interact through a web UI.

## Features
- FastAPI backend with LangChain and OpenAI
- React + Tailwind frontend
- DuckDuckGo-based real-time search
- Agent-style reasoning and summary
- Extendable with Whisper, OCR, and more

## Stack
- Frontend: React, Tailwind CSS, Axios
- Backend: FastAPI, LangChain, OpenAI API
- Tools: DuckDuckGoSearchRun (can add Playwright, Whisper, OCR)

## Quick Start

```bash
# In /backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# In /frontend
npm install
npm start
```

Backend will run on `http://localhost:8000`  
Frontend will run on `http://localhost:3000`
