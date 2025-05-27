from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

class RequestBody(BaseModel):
    query: str

@app.post("/search")
async def search(body: RequestBody):
    return JSONResponse(content={"response": f"You searched for: {body.query}"})

handler = Mangum(app)
