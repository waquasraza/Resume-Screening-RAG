from fastapi import FastAPI
from app.api.resume import router as resume_router
from app.api.chat import router as chat_router



app = FastAPI(
    title="Resume Screening RAG"
)
    
app.include_router(resume_router)
app.include_router(chat_router)

@app.get("/")
def health():
    return {"status": "running"}