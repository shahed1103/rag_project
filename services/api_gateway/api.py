from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from services.rag.rag_pipeline import ask


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # أثناء التطوير
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QuestionRequest):

    return ask(request.question)