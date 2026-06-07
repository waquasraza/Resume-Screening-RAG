from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retriever import get_relevant_chunks
from app.services.chat_service import generate_answer

router = APIRouter(prefix="/chat")


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):

    docs = get_relevant_chunks(
        request.question
    )

    answer = generate_answer(
        request.question,
        docs
    )

    return {
        "question": request.question,
        "answer": answer
    }