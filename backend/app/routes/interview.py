from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import uuid
import os

from app.services.whisper_service import transcribe_audio
from app.database.session import SessionLocal
from app.database.models import Transcript

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, "..", "media")

@router.post("/interview/audio")
async def upload_audio(file: UploadFile = File(...)):
    try:
        ext = file.filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        filepath = os.path.join(MEDIA_DIR, filename)

        os.makedirs(MEDIA_DIR, exist_ok=True)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcript = transcribe_audio(filepath)

        return {
            "filename": filename,
            "transcript": transcript
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload or transcription failed: {str(e)}")

@router.get("/interview/transcripts")
def get_transcripts():
    db = SessionLocal()
    try:
        transcripts = db.query(Transcript).all()
        return [
            {
                "id": t.id,
                "filename": t.filename,
                "transcript": t.transcript,
                "created_at": t.created_at
            }
            for t in transcripts
        ]
    finally:
        db.close()
