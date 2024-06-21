import inspect
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.answers import get_answers, create_answer, update_answer, delete_answer
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.answers import CreateAnswer, UpdateAnswer
from schemas.users import CreateUser
from db import database


answers_router = APIRouter(
    prefix="/answers",
    tags=["Answers operation"]
)


@answers_router.get('/get')
def get_answer(ident: int = 0, search: str = None,  page: int = 1,
               limit: int = 25, db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_answers(ident, search, page, limit, db)


@answers_router.post('/create')
def create(forms: List[CreateAnswer], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_answer(forms, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@answers_router.put("/update")
def update(form: UpdateAnswer, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_answer(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@answers_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_answer(ident, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
