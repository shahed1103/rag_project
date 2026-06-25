from fastapi import FastAPI
from pydantic import BaseModel

from services.rag.rag_pipeline import ask


app = FastAPI(
    title="Islamic RAG API",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = ask(
        request.question
    )

    return result