from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Query(BaseModel):
    query: str
    model: str = "gpt-3.5-turbo"

@app.post("/search")
async def search(query: Query):
    model_used = query.model
    model_prices = {
        "gpt-3.5-turbo": 0.002,
        "gpt-4": 0.03,
        "gpt-4o": 0.005,
        "gpt-4.1": 0.03
    }
    try:
        resp = client.chat.completions.create(
            model=query.model,
            messages=[{"role": "user", "content": query.query}],
            max_tokens=100
        )
    except Exception as e:
        # Fallback to gpt-3.5-turbo if any error occurs
        model_used = "gpt-3.5-turbo"
        try:
            resp = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query.query}],
                max_tokens=100
            )
        except Exception as e2:
            return JSONResponse(status_code=500, content={
                "error": f"Both requested model ({query.model}) and fallback (gpt-3.5-turbo) failed: {str(e2)}"
            })

    text = resp.choices[0].message.content.strip()
    tokens = resp.usage.total_tokens
    cost = round(tokens / 1000 * model_prices.get(model_used, 0.002), 6)
    return {
        "response": text,
        "tokens_used": tokens,
        "cost_usd_estimate": cost,
        "model_used": model_used
    }

@app.get("/")
def root():
    return {"message": "Hello from AI Multimodal Search! The API is running."}
