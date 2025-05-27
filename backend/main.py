from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/search")
async def search(query: Query):
    return {"response": f"You searched for: {query.query}"}
