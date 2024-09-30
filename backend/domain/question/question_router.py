from fastapi import APIRouter

from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list():
    _question_list = question_crud.get_question_list()
    return _question_list