from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from database import get_db
from domain.comment import comment_schema, comment_crud
from domain.question import question_crud

router = APIRouter(
    prefix="/api/comment",
)

@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _comment_create: comment_schema.CommentCreate,
                  db: Session = Depends(get_db)):

    # create comment
    question = question_crud.get_question(db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    comment_crud.create_comment(question=question, comment_create=_comment_create)