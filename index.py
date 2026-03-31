from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SearchRequest(BaseModel):
    query: str
    type: str = "text"

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/search")
def search(req: SearchRequest):
    return {
        "query": req.query,
        "results": ["result1", "result2"]
    }

# 👇 REQUIRED for Vercel
def handler(request, response):
    return app
