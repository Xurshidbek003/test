import inspect
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.categories import get_categories, create_category, update_category, delete_category
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.categories import CreateCategory, UpdateCategory
from schemas.users import CreateUser
from db import database


categories_router = APIRouter(
    prefix="/categories",
    tags=["Categories operation"]
)


@categories_router.get('/get')
def get_category(ident: int = 0, search: str = None,  page: int = 1,
                 limit: int = 25, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_categories(ident, search, page, limit, db)


@categories_router.post('/create')
def create(form: CreateCategory, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    create_category(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@categories_router.put("/update")
def update(form: UpdateCategory, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    update_category(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@categories_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    delete_category(ident, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


