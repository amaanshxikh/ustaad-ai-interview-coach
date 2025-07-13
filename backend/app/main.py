from fastapi import FastAPI
from app.routes import interview

app = FastAPI()

# Register routes
app.include_router(interview.router)

@app.get("/")
def root():
    return {"message": "USTAAD backend is live!"}
