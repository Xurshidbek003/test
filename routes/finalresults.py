import inspect
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from functions.results import get_final_results, get_final_final_results
from routes.login import get_current_active_user
from utils.role_verification import role_verification
from schemas.users import CreateUser
from db import database


final_results_router = APIRouter(
    prefix="/final_results",
    tags=["Final Results operation"]
)


@final_results_router.get('/get')
def get_final(ident: int = 0, page: int = 1,
              limit: int = 25, db: Session = Depends(database),
              current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_final_results(ident, page, limit, db, current_user)


@final_results_router.get('/get_final')
def get_final_final(db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
    role_verification(current_user, inspect.currentframe().f_code.co_name)
    return get_final_final_results(db, current_user)
