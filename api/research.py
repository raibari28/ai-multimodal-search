from utils.browser import google_search_and_scrape, duckduckgo_search_and_scrape

@app.post("/research")
async def research_file(request: Request):
    try:
        data = await request.json()
        text = data.get("text", "")
        if not text:
            return JSONResponse({"summary": "No text provided.", "query": ""}, status_code=400)
        query = gpt_generate_query(text[:2000])
        # Try Google first
        html = await google_search_and_scrape(query)
        # Fallback to DuckDuckGo if Google blocks or fails
        if html is None:
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
    except RateLimitError:
        return JSONResponse({
            "summary": "OpenAI API quota exceeded or rate limit hit. Please update your API key or check your usage.",
            "query": ""
        }, status_code=429)
    except AuthenticationError:
        return JSONResponse({
            "summary": "OpenAI API authentication failed. Please check your API key.",
            "query": ""
        }, status_code=401)
    except (APIError, APIConnectionError, APITimeoutError) as oe:
        return JSONResponse({
            "summary": f"OpenAI API connection error: {oe}",
            "query": ""
        }, status_code=500)
    except Exception as e:
        import traceback
        print("Exception in /research:", e)
        traceback.print_exc()
        return JSONResponse({
            "summary": f"Internal server error: {str(e)}",
            "query": ""
        }, status_code=500)
