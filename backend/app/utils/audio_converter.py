import subprocess
import os
import uuid

FFMPEG_PATH = os.path.join(
    os.getcwd(),
    "venv",
    "Lib",
    "site-packages",
    "imageio_ffmpeg",
    "binaries",
    "ffmpeg-win-x86_64-v7.1.exe"
)

def convert_to_wav(input_path: str) -> str:
    output_path = input_path.replace(".mp3", f".wav")
    try:
        subprocess.run(
            [FFMPEG_PATH, "-y", "-i", input_path, "-ar", "16000", "-ac", "1", output_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return output_path
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"FFmpeg conversion failed: {e}")
