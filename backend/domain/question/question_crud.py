from datetime import datetime

from domain.question.question_schema import QuestionCreate
from domain.answer import answer_schema, answer_crud
from models import Question
from database import get_db

def get_question_list(skip: int = 0, limit: int = 10):
    with get_db() as db:
        _question_list = db.query(Question)\
            .order_by(Question.create_date.desc())
    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list # (전체 갯수, 페이징 된 질문)

def get_question(question_id: int):
    with get_db() as db:
        question = db.query(Question).get(question_id)
    return question

def create_question(question_create: QuestionCreate, answer_create: answer_schema.AnswerCreate):
    with get_db() as db:
        db_question = Question(subject=question_create.subject,
                               quest=question_create.quest,
                               create_date=datetime.now())
        db.add(db_question)
        db.commit()

    answer_crud.create_answer(question=db_question,
                              answer_create=answer_create)    

    
    
    