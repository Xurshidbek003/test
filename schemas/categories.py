from pydantic import BaseModel


class CreateCategory(BaseModel):
    name: str


class UpdateCategory(BaseModel):
    id: int
    name: str

