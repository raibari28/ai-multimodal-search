from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

from utils.serp_openai import fetch_and_summarize

app = FastAPI()

@app.get("/")
async def root_info():
    """Return basic usage information."""
    return {
        "message": "Use POST /research with JSON {'text': 'your content'} to summarize"
    }

@app.get("/research")
async def research_get_info():
    """Provide instructions for the research endpoint."""
    return {
        "detail": "Send a POST request with a JSON body {'text': '<your text>'}"}

@app.post("/research")
async def research_file(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return JSONResponse({"summary": "No text provided.", "source_url": ""}, status_code=400)
    openai_key = os.environ.get("OPENAI_API_KEY")
    serp_key = os.environ.get("SERPAPI_KEY")
    if not openai_key or not serp_key:
        missing = []
        if not openai_key:
            missing.append("OPENAI_API_KEY")
        if not serp_key:
            missing.append("SERPAPI_KEY")
        detail = f"Missing required environment variables: {', '.join(missing)}"
        return JSONResponse({"detail": detail}, status_code=500)

    result = fetch_and_summarize(
        text,
        openai_key=openai_key,
        serpapi_key=serp_key,
    )
    return JSONResponse(result)
