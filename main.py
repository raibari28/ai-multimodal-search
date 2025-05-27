from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class RequestBody(BaseModel):
    query: str

@app.post("/search")
async def search(body: RequestBody):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=body.query,
            max_tokens=100
        )
        return JSONResponse(content={"response": response.choices[0].text.strip()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
