from database import get_db
from database.models import *

def add_question_db(main_question, v1, v2, v3, v4, correct_answer, level):
    db = next(get_db())
    new_question = Question(main_question=main_question, v1=v1, v2=v2,
                             v3=v3, v4=v4, correct_answer=correct_answer, level=level)
    db.add(new_question)
    db.commit()
    return True