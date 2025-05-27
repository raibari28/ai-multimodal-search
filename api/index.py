from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from mangum import Mangum

# Create FastAPI app
app = FastAPI()

# Define request schema
class RequestBody(BaseModel):
    query: str

# Define route
@app.post("/search")
async def search(body: RequestBody):
    return JSONResponse(content={"response": f"You searched for: {body.query}"})

# Define AWS Lambda-compatible handler
handler = Mangum(app)
