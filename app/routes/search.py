from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    type: str = "text"

@router.post("/search")
def search(req: SearchRequest):
    return {
        "query": req.query,
        "results": ["ok"]
    }
