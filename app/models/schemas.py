from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    type: str = "text"

class SearchResponse(BaseModel):
    query: str
    type: str
    results: list[str]
