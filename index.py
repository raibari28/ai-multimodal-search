# api/index.py
from fastapi import FastAPI
from app.routes.search import router as search_router

app = FastAPI()
app.include_router(search_router)

# This is what Vercel uses
app = app
