# routes/upload.py
from fastapi import APIRouter, UploadFile
import shutil
import os

from app.core.parsers import pdf_parser, docx_parser, pptx_parser, xlsx_parser, image_parser
from app.core.embeddings import fake_embedding
from app.core.vector_store import add_vector

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    path = f"temp/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ext = file.filename.split(".")[-1]

    if ext == "pdf":
        text = pdf_parser.parse_pdf(path)
    elif ext == "docx":
        text = docx_parser.parse_docx(path)
    elif ext == "pptx":
        text = pptx_parser.parse_pptx(path)
    elif ext == "xlsx":
        text = xlsx_parser.parse_xlsx(path)
    elif ext in ["jpg", "png", "gif"]:
        text = image_parser.parse_image(path)
    else:
        return {"error": "Unsupported file"}

    vector = fake_embedding(text)

    add_vector(vector, {"filename": file.filename, "preview": text[:200]})

    return {"status": "indexed"}
