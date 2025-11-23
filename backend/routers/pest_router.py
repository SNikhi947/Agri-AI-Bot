from fastapi import APIRouter, UploadFile, File
from backend.modules.pest import analyze_pest_image
import shutil
import os

router = APIRouter(prefix="/pest", tags=["pest"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pest_image(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    
    # Save file locally
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    
    # Analyze
    diagnosis = analyze_pest_image(file.filename)
    
    return {
        "filename": file.filename,
        "diagnosis": diagnosis,
        "message": f"Detected: {diagnosis['disease']}. {diagnosis['treatment']}"
    }