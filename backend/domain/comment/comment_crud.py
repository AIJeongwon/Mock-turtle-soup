from datetime import datetime
from sqlalchemy.orm import Session

from domain.comment.comment_schema import CommentCreate
from models import Question, Comment, User

def create_comment(db: Session, question: Question, comment_create: CommentCreate, user: User):
    db_comment = Comment(question=question,
                        content=comment_create.content,
                        create_date=datetime.now(),
                        user=user)
    db.add(db_comment)
    db.commit()
