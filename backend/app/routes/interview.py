from fastapi import APIRouter, UploadFile, File
import shutil
import uuid
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/
MEDIA_DIR = os.path.join(BASE_DIR, "..", "media")  # go one level up

@router.get("/interview/test")
def test_interview():
    return {"message": "Interview route is working!"}

@router.post("/interview/audio")
async def upload_audio(file: UploadFile = File(...)):
    ext = file.filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = os.path.join(MEDIA_DIR, filename)

    os.makedirs(MEDIA_DIR, exist_ok=True)  # safety check

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    dummy_transcript = "This is a placeholder transcript."

    return {
        "filename": filename,
        "transcript": dummy_transcript
    }
