from pydantic import BaseModel


class CreateResult(BaseModel):
    question_id: int
    answer_id: int
    category_id: int



