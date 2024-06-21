import inspect
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.users import get_users, create_user_f, update_user_f, delete_user_f, create_general_user_f
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.users import CreateUser, UpdateUser, CreateGeneralUser
from db import database


users_router = APIRouter(
    prefix="/users",
    tags=["Users operation"]
)


@users_router.get('/get')
def get(ident: int = 0, search: str = None,  page: int = 1,
        limit: int = 25, role: str = None, db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_users(ident, search, page, limit, role, db)


@users_router.get('/get_own')
def get_own(current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return current_user


@users_router.post('/create')
def create_user(form: CreateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_user_f(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.post('/sign_up')
def create_general_user(form: CreateGeneralUser, db: Session = Depends(database)):
    create_general_user_f(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.put("/update")
def update_user(form: UpdateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_user_f(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.delete("/delete")
def delete_user(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_user_f(db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


