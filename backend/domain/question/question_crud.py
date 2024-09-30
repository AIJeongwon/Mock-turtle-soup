from models import Question
from database import get_db

def get_question_list():
    with get_db as db:
        question_list = db.query(Question)\
            .order_by(Question.create_date.desc())\
            .all()
    return question_list