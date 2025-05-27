from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from openai import OpenAI
import os
import time
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load local .env for local dev; on Railway, only Variables tab matters
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logger.error("OPENAI_API_KEY not set! Check your Railway Variables tab.")
else:
    logger.info("OPENAI_API_KEY loaded.")

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()

class RequestBody(BaseModel):
    query: str

@app.post("/search")
async def search(body: RequestBody):
    try:
        logger.info(f"Received query: {body.query}")
        start_time = time.time()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": body.query}],
            max_tokens=100
        )

        end_time = time.time()

        text = response.choices[0].message.content.strip() if response.choices else "No response"
        tokens_used = getattr(response.usage, "total_tokens", 0)
        cost_estimate = (tokens_used / 1000) * 0.002  # gpt-3.5-turbo price estimate

        logger.info(f"Tokens used: {tokens_used}, Cost: ${cost_estimate}")

        return JSONResponse(content={
            "response": text,
            "query": body.query,
            "tokens_used": tokens_used,
            "cost_usd_estimate": round(cost_estimate, 6),
            "timestamp_utc": datetime.utcnow().isoformat(),
            "duration_seconds": round(end_time - start_time, 2)
        })
    except Exception as e:
        import traceback
        logger.error(traceback.format_exc())
        return JSONResponse(status_code=500, content={
            "error": str(e),
            "help": "Check Railway Variables tab for OPENAI_API_KEY, model permissions, and see logs."
        })
