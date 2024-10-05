import datetime

from pydantic import BaseModel, field_validator


class Question(BaseModel):
    id: int
    subject: str
    quest: str
    create_date: datetime.datetime

class QuestionCreate(BaseModel):
    subject: str
    quest: str
    ans: str

    @field_validator('subject', 'quest', 'ans')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v;