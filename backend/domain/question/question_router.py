from fastapi import APIRouter
from starlette import status
from domain.question import question_schema, question_crud
from domain.answer import answer_schema

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list():
    _question_list = question_crud.get_question_list()
    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int):
    question = question_crud.get_question(question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate):
    _answer_create = answer_schema.AnswerCreate(**{
        'ans': _question_create.ans
    })
    question_crud.create_question(question_create=_question_create, answer_create=_answer_create)