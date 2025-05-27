from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Query(BaseModel):
    query: str

@app.post("/search")
async def search(body: Query):
    return JSONResponse(content={"response": f"Received query: {body.query}"})

# Vercel will look for this handler
handler = Mangum(app)
