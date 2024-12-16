from fastapi import APIRouter
from database.testservice import *
test_router = APIRouter(prefix="/test",
                        tags=["Административная часть"])


@test_router.post("/add_q")
async def add_question(main_question: str, v1: str, v2: str,
                       v3: str, v4: str, correct_answer: int, level: str):
    result = add_question_db(main_question=main_question, v1=v1, v2=v2,
                             v3=v3, v4=v4, correct_answer=correct_answer, level=level)
    if result:
        return {"status": 1, "message": "успешно зарегистрированы"}
    return {"status": 0, "message": "ошибка регистрации"}
