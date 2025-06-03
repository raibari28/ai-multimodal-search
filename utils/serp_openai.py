from serpapi import GoogleSearch
import openai
import requests
from bs4 import BeautifulSoup

def fetch_and_summarize(query, openai_key, serpapi_key):
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "organic_results" in results and results["organic_results"]:
        url = results["organic_results"][0]["link"]
        # Fetch and extract web content
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            web_content = text[:3500]  # truncate to ~3500 chars
        except Exception as e:
            web_content = f"Unable to fetch web content: {e}\nURL: {url}"
        # Summarize with OpenAI
        client = openai.OpenAI(api_key=openai_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following web content in a factual, neutral, concise way."},
                {"role": "user", "content": web_content}
            ],
            max_tokens=256
        )
        return {
            "summary": completion.choices[0].message.content.strip(),
            "source_url": url
        }
    else:
        return {"summary": "No search results found.", "source_url": ""}
