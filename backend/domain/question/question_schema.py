import datetime

from pydantic import BaseModel, field_validator

from domain.comment.comment_schema import Comment
from domain.user.user_schema import User

class Question(BaseModel):
    id: int
    subject: str
    quest: str
    answer: str
    create_date: datetime.datetime
    comments: list[Comment] = []
    user: User | None

class QuestionCreate(BaseModel):
    subject: str
    quest: str
    answer: str

    @field_validator('subject', 'quest', 'answer')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v;

class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []