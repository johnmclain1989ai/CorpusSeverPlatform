from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import sessionmaker, Session, declarative_base
import random
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./corpus.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Corpus Server Platform")

MAX_GROUP_SIZE = 20


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class QuestionResponse(BaseModel):
    id: int
    text: str


class AnswerRequest(BaseModel):
    id: int
    answer: str


class EvaluationResponse(BaseModel):
    id: int
    correct: bool


@app.get("/questions", response_model=list[QuestionResponse])
def get_questions(n: int = 5, db: Session = Depends(get_db)):
    if n > MAX_GROUP_SIZE:
        raise HTTPException(status_code=400, detail=f"Cannot request more than {MAX_GROUP_SIZE} questions at once")
    questions = db.query(Question).all()
    if not questions:
        return []
    selected = random.sample(questions, min(n, len(questions)))
    return [QuestionResponse(id=q.id, text=q.text) for q in selected]


@app.post("/evaluate", response_model=list[EvaluationResponse])
def evaluate(answers: list[AnswerRequest], db: Session = Depends(get_db)):
    if len(answers) > MAX_GROUP_SIZE:
        raise HTTPException(status_code=400, detail=f"Cannot evaluate more than {MAX_GROUP_SIZE} answers at once")
    results = []
    for ans in answers:
        q = db.query(Question).filter(Question.id == ans.id).first()
        if not q:
            raise HTTPException(status_code=404, detail=f"Question {ans.id} not found")
        correct = q.answer.strip() == ans.answer.strip()
        results.append(EvaluationResponse(id=q.id, correct=correct))
    return results


@app.get("/")
def read_root():
    return {"message": "Corpus Server Platform"}

