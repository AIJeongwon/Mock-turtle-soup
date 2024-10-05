from datetime import datetime

from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer
from database import get_db

def create_answer(question: Question, answer_create: AnswerCreate):
    with get_db() as db:
        db_answer = Answer(question=question,
                           ans=answer_create.ans)
        db.add(db_answer)
        db.commit()