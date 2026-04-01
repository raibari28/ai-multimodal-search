# api/search.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SearchRequest(BaseModel):
    query: str

@app.post("/")
def search(req: SearchRequest):
    return {"query": req.query}
