import inspect
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from functions.results import get_results, create_result
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.results import CreateResult
from schemas.users import CreateUser
from db import database


results_router = APIRouter(
    prefix="/results",
    tags=["Results operation"]
)


@results_router.get('/get')
def get_result(ident: int = 0, search: str = None,  page: int = 1,
               limit: int = 25, db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_results(ident, search, page, limit, db, current_user)


@results_router.post('/create')
def create_result_t(forms: List[CreateResult], db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return create_result(forms, db, current_user)
