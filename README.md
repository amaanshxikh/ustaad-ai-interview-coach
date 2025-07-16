# 🤖 USTAAD – AI Interview Coach

**USTAAD** is an AI-powered interview preparation platform. It simulates mock interviews using user-submitted audio, performs speech-to-text transcription, and will soon provide smart feedback via GPT and video-based posture/emotion analysis.

---

## 🧠 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **OpenAI Whisper**
- **SQLite** (Temporary DB for storing transcripts)
- **MongoDB** *(planned in Phase 2)*
- **Docker** *(optional deployment)*

---

## 📁 Folder Structure

```
ustaad-ai-interview-coach/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   └── interview.py
│   │   ├── services/
│   │   │   └── whisper_service.py
│   │   ├── database/
│   │   │   ├── models.py
│   │   │   └── session.py
│   │   └── logging_config.py
│   ├── venv/
│   └── requirements.txt
├── media/                 # Uploaded audio files
├── logs/                  # Log files
├── frontend/              # Placeholder for future frontend
├── docker-compose.yml     # (Planned)
└── README.md
```

---

## 🚀 Getting Started (Backend)

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate         # On Windows
# Or: source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open your browser and visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to use the Swagger UI.

---

## 📡 API Endpoints

| Method | Endpoint                 | Description                          |
|--------|--------------------------|--------------------------------------|
| GET    | `/`                      | Health check                         |
| POST   | `/interview/audio`       | Upload MP3 audio and get transcript  |
| GET    | `/interview/transcripts` | View all saved transcripts (from DB) |

---

## 🔮 Upcoming Features (Phase 2)

- [x] Whisper-based transcription
- [ ] Emotion and tone analysis
- [ ] Posture & facial expression detection (video)
- [ ] Smart feedback via GPT-4o
- [ ] MongoDB-based interview dashboard
- [ ] Frontend integration (React)

---

## 📦 Sample Transcription Flow

1. Send `.mp3` audio to `/interview/audio`
2. It will be converted to `.wav` and passed through OpenAI Whisper
3. The transcript is returned and saved to a database
4. Retrieve all transcripts via `/interview/transcripts`

---

## 🛡️ .gitignore Suggestions

<details>
<summary>Click to expand</summary>

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env

# FastAPI & Logs
logs/
media/

# Node/React (frontend)
node_modules/
build/

# VS Code & OS
.vscode/
.DS_Store
Thumbs.db
```

</details>

---

## 👥 Contributors

Made with ❤️ by Amaan Shaikh & Team  
KJSCE Final Year Project – 2025-26

---
