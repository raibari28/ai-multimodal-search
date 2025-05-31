from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.summarizer import gpt_generate_query, gpt_summarize
from utils.browser import google_search_and_scrape
from utils.extractor import extract_main_text

app = FastAPI()

@app.post("/research")
async def research_file(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return JSONResponse({"summary": "No text provided.", "query": ""})
    query = gpt_generate_query(text[:2000])
    html = google_search_and_scrape(query)
    web_article = extract_main_text(html)
    crosscheck_prompt = (
        f"User Content:\n{text[:1000]}\n\n---\n"
        f"Web Source Content:\n{web_article[:2000]}\n\n"
        "Compare and report agreements, disagreements, or discrepancies. Summarize the main points."
    )
    summary = gpt_summarize(crosscheck_prompt)
    return JSONResponse({"summary": summary, "query": query})
