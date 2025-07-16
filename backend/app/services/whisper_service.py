import os
import subprocess
import whisper
import traceback
import numpy as np
import tempfile

from app.database.session import SessionLocal
from app.database.models import Transcript
from app.logging_config import get_logger

logger = get_logger()

model = whisper.load_model("base")

FFMPEG_PATH = r"C:\Users\Amaan Shaikh\ustaad-ai-interview-coach\backend\venv\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

# ✅ Patch load_audio to use your FFMPEG binary (Windows-safe)
import whisper.audio as whisper_audio

def custom_load_audio(path: str, sr: int = 16000) -> np.ndarray:
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    temp_wav.close()  # ❗ CLOSE IT so it's not locked on Windows

    try:
        # ✅ Use FFmpeg to convert
        command = [
            FFMPEG_PATH, "-y", "-i", path,
            "-f", "wav", "-ac", "1", "-ar", str(sr),
            "-acodec", "pcm_s16le", temp_wav.name
        ]
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # ✅ Now load it
        audio_data = np.memmap(temp_wav.name, dtype=np.int16, mode='r')
        audio = audio_data.astype(np.float32) / 32768.0
        return audio

    finally:
        try:
            os.remove(temp_wav.name)
        except Exception as e:
            logger.warning(f"Could not delete temp file: {temp_wav.name} — {e}")

# ✅ Patch Whisper
whisper_audio.load_audio = custom_load_audio


def convert_to_wav(input_path: str) -> str:
    output_path = input_path.rsplit(".", 1)[0] + ".wav"
    command = [FFMPEG_PATH, "-y", "-i", input_path, "-ar", "16000", "-ac", "1", output_path]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path


def transcribe_audio(file_path: str) -> str:
    try:
        logger.info(f"[Whisper] Transcribing file: {file_path}")
        wav_path = os.path.abspath(convert_to_wav(file_path))

        if not os.path.exists(wav_path):
            raise FileNotFoundError(f"WAV file not found after conversion: {wav_path}")
        if os.path.getsize(wav_path) == 0:
            raise ValueError(f"WAV file is empty: {wav_path}")

        result = model.transcribe(wav_path)
        transcript_text = result["text"]
        save_transcript_to_db(os.path.basename(file_path), transcript_text)
        return transcript_text

    except Exception as e:
        logger.error("Transcription failed:")
        logger.error(traceback.format_exc())
        raise RuntimeError(f"Transcription failed: {e}")


def save_transcript_to_db(filename: str, transcript: str) -> None:
    db = SessionLocal()
    try:
        entry = Transcript(filename=filename, transcript=transcript)
        db.add(entry)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error("Failed to save transcript to DB", exc_info=True)
        raise e
    finally:
        db.close()
