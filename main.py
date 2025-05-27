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

# Input schema
class RequestBody(BaseModel):
    query: str

# POST endpoint for AI search
@app.post("/search")
async def search(body: RequestBody):
    try:
        start_time = time.time()

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=body.query,
            max_tokens=100
        )

        end_time = time.time()
        duration = round(end_time - start_time, 2)
        timestamp = datetime.utcnow().isoformat()

        text = response.choices[0].text.strip()
        usage = response.to_dict().get("usage") or {}
        cost_estimate = 0.002 * usage.get("total_tokens", 0) / 1000  # ~$0.002 per 1K tokens

        # Return response with metadata
        return JSONResponse(content={
            "response": text,
            "query": body.query,
            "tokens_used": usage,
            "cost_usd_estimate": round(cost_estimate, 6),
            "timestamp_utc": timestamp,
            "duration_seconds": duration
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
