from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/search")
async def search(query: str):
    return JSONResponse(content={"response": f"You searched: {query}"})

from mangum import Mangum
handler = Mangum(app)
