import inspect
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.questions import get_questions, create_question, update_question, delete_question
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.questions import CreateQuestion, UpdateQuestion
from schemas.users import CreateUser
from db import database


questions_router = APIRouter(
    prefix="/questions",
    tags=["Questions operation"]
)


@questions_router.get('/get')
def get_question(ident: int = 0, search: str = None,  page: int = 1,
                 limit: int = 25, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_questions(ident, search, page, limit, db)


@questions_router.post('/create')
def create(forms: List[CreateQuestion], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_question(forms, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@questions_router.put("/update")
def update(form: UpdateQuestion, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_question(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@questions_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_question(ident, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
