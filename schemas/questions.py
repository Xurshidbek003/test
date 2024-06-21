from pydantic import BaseModel


class CreateQuestion(BaseModel):
    question: str
    category_id: int


class UpdateQuestion(BaseModel):
    id: int
    question: str
    category_id: int
