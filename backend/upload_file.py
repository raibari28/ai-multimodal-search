from fastapi import UploadFile, File
import shutil
import os
import textract

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Try to extract text from uploaded file
    try:
        extracted_text = textract.process(file_location).decode("utf-8", errors="ignore")
        return {
            "filename": file.filename,
            "status": "uploaded",
            "extracted_text": extracted_text[:3000]  # Limit output for response
        }
    except Exception as e:
        return {
            "filename": file.filename,
            "status": "uploaded",
            "error": f"Text extraction failed: {str(e)}"
        }
