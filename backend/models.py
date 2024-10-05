from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    quest = Column(Text, nullable=False) # Content
    create_date = Column(DateTime, nullable=False)
    

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    ans = Column(Text, nullable=False) # Content
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")