from pydantic import BaseModel


class CreateAnswer(BaseModel):
    answer: str
    status: bool
    question_id: int


class UpdateAnswer(BaseModel):
    id: int
    answer: str
    status: bool
    question_id: int
