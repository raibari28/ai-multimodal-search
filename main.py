from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import openai
import os

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
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=body.query,
            max_tokens=100
        )
        # Return result
        return JSONResponse(content={"response": response.choices[0].text.strip()})
    except Exception as e:
        # Handle errors gracefully
        return JSONResponse(status_code=500, content={"error": str(e)})
