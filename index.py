from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SearchRequest(BaseModel):
    query: str
    type: str = "text"

@app.get("/")
def root():
    return {"status": "ok", "service": "multimodal-search"}

@app.post("/search")
def search(req: SearchRequest):
    return {
        "query": req.query,
        "type": req.type,
        "results": [
            f"Result for: {req.query}",
            "Multimodal search placeholder"
        ]
    }
