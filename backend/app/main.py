from fastapi import FastAPI
from app.routes import interview
from app.database import models, session
from app.logging_config import get_logger

logger = get_logger()

logger.info("USTAAD backend starting...")

# ✅ DB table creation
models.Base.metadata.create_all(bind=session.engine)
logger.info("Database tables created.")

# ✅ FastAPI app setup
app = FastAPI()

# ✅ Register routes
app.include_router(interview.router)

@app.get("/")
def root():
    return {"message": "USTAAD backend is live!"}
