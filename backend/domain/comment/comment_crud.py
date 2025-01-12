from datetime import datetime
from sqlalchemy.orm import Session

from domain.comment.comment_schema import CommentCreate
from models import Question, Comment

def create_comment(db: Session, question: Question, comment_create: CommentCreate):
    db_comment = Comment(question=question,
                        content=comment_create.content,
                        create_date=datetime.now())
    db.add(db_comment)
    db.commit()
