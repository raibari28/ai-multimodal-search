from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import openai
import os
import time
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class RequestBody(BaseModel):
    query: str

@app.post("/search")
async def search(body: RequestBody):
    try:
        start_time = time.time()
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=body.query,
            max_tokens=100
        )
        response_dict = response.to_dict()
        usage = response_dict.get("usage") or {}
        tokens = usage.get("total_tokens", 0)
        cost_estimate = 0.002 * tokens / 1000

        return JSONResponse(content={
            "response": response_dict["choices"][0]["text"].strip(),
            "query": body.query,
            "tokens_used": usage,
            "cost_usd_estimate": round(cost_estimate, 6),
            "timestamp_utc": datetime.utcnow().isoformat(),
            "duration_seconds": round(time.time() - start_time, 2)
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "error": str(e),
            "help": "Check if OPENAI_API_KEY is correctly set and OpenAI is reachable."
        })
