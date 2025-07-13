# USTAAD – AI Interview Coach

 **USTAAD**, an AI-powered platform that simulates mock interviews, processes user audio/video, and provides personalized feedback.

---

## 📦 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Whisper (Phase 2)**
- **MongoDB (coming in Phase 2)**
- **Docker (optional deployment)**

---

## 📂 Folder Structure

```plaintext
ustaad-ai-interview-coach/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   └── models/
│   ├── venv/
│   └── requirements.txt
├── media/
├── frontend/         # Will be set up later
├── docker-compose.yml
└── README.md


---

## 🚀 Getting Started (Backend)

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # (or source venv/bin/activate on Linux/Mac)
pip install -r requirements.txt
uvicorn app.main:app --reload
````

Then visit [http://127.0.0.1:8000/docs] to access Swagger UI.

---

## 📡 API Endpoints

| Method | Endpoint           | Description                     |
| ------ | ------------------ | ------------------------------- |
| GET    | `/`                | Health check                    |
| GET    | `/interview/test`  | Test custom route               |
| POST   | `/interview/audio` | Upload audio & return dummy STT |

---

## 🔮 Upcoming Features (Phase 2)

* [ ] Whisper AI transcription
* [ ] Emotion/tone detection
* [ ] Video posture and expression analysis
* [ ] GPT-4o feedback generation
* [ ] Interview history dashboard (MongoDB)

---

## 🛡️ .gitignore Template

Make sure your `.gitignore` file contains:

<details>
<summary>Click to view</summary>

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
*.env

# Frontend
node_modules/
build/

# VS Code & OS
.vscode/
.DS_Store
Thumbs.db

# Misc
media/
```

</details>
```

---

