from datetime import datetime
from sqlalchemy.orm import Session

from domain.question.question_schema import QuestionCreate, QuestionUpdate
from models import Question, User

def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question)\
            .order_by(Question.create_date.desc())
    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list # (전체 갯수, 페이징 된 질문)

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(subject=question_create.subject,
                            quest=question_create.quest,
                            answer=question_create.answer,
                            create_date=datetime.now(),
                            user=user)
    db.add(db_question)
    db.commit()

def update_question(db: Session, db_question: Question, question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.quest = question_update.quest
    db_question.answer = question_update.answer
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()

def delete_question(db: Session, db_question: Question):
    db.delete(db_question)
    db.commit()
    
    
    