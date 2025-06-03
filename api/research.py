from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from utils.summarizer import gpt_generate_query, gpt_summarize
from utils.browser import google_search_and_scrape, duckduckgo_search_and_scrape
from utils.extractor import extract_main_text

app = FastAPI()

@app.post("/research")
async def research_file(request: Request):
    try:
        data = await request.json()
        text = data.get("text", "")
        if not text:
            return JSONResponse({"summary": "No text provided.", "query": ""}, status_code=400)
        query = gpt_generate_query(text[:2000])
        html = await google_search_and_scrape(query)
        if html is None or "Blocked by Google" in (html or "") or "selector not found" in (html or ""):
            html = await duckduckgo_search_and_scrape(query)
        if html is None:
            return JSONResponse({"summary": "Failed to fetch search results from Google or DuckDuckGo.", "query": query}, status_code=502)
        web_article = extract_main_text(html)
        crosscheck_prompt = (
            f"User Content:\n{text[:1000]}\n\n---\n"
            f"Web Source Content:\n{web_article[:2000]}\n\n"
            "Compare and report agreements, disagreements, or discrepancies. Summarize the main points."
        )
        summary = gpt_summarize(crosscheck_prompt)
        return JSONResponse({"summary": summary, "query": query})
    except Exception as e:
        import traceback
        print("Exception in /research:", e)
        traceback.print_exc()
        return JSONResponse({
            "summary": f"Internal server error: {str(e)}",
            "query": ""
        }, status_code=500)
