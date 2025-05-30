from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables (OPENAI_API_KEY set in Hugging Face "Secrets")
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Query(BaseModel):
    query: str
    model: str = "gpt-3.5-turbo"  # Default, can override

@app.post("/search")
async def search(query: Query):
    try:
        resp = client.chat.completions.create(
            model=query.model,
            messages=[{"role": "user", "content": query.query}],
            max_tokens=100
        )
        text = resp.choices[0].message.content.strip()
        tokens = resp.usage.total_tokens
        model_prices = {
            "gpt-3.5-turbo": 0.002,
            "gpt-4o": 0.005,
            "gpt-4.1": 0.03
        }
        cost = round(tokens / 1000 * model_prices.get(query.model, 0.002), 6)
        return {
            "response": text,
            "tokens_used": tokens,
            "cost_usd_estimate": cost
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})