from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent.logic import run_agent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/search")
async def search_web(request: Request):
    data = await request.json()
    query = data.get("query", "")
    result = run_agent(query)
    return {"response": result}
