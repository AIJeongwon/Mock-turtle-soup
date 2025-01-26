from datetime import datetime
from sqlalchemy import and_
from sqlalchemy.orm import Session

from domain.question.question_schema import QuestionCreate, QuestionUpdate
from models import Question, Comment, User

def get_question_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = ''):
    question_list = db.query(Question)
    if keyword:
        search = '%%{}%%'.format(keyword)
        sub_query = db.query(Comment.question_id, Comment.content, User.username) \
            .outerjoin(User, and_(Comment.user_id == User.id)).subquery()
        question_list = question_list \
            .outerjoin(User) \
            .outerjoin(sub_query, and_(sub_query.c.question_id == Question.id)) \
            .filter(Question.subject.ilike(search) |        # 질문제목
                    Question.quest.ilike(search) |          # 질문
                    Question.answer.ilike(search) |         # 정답
                    User.username.ilike(search) |           # 질문작성자
                    sub_query.c.content.ilike(search) |     # 댓글내용
                    sub_query.c.username.ilike(search)      # 댓글작성자
                    )
    total = question_list.distinct().count()
    question_list = question_list.order_by(Question.create_date.desc())\
        .offset(skip).limit(limit).distinct().all()
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

def vote_question(db: Session, db_question: Question, db_user: User):
    db_question.voter.append(db_user)
    db.commit()