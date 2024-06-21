from fastapi import APIRouter
from routes.login import login_router
from routes.users import users_router
from routes.answers import answers_router
from routes.categories import categories_router
from routes.finalresults import final_results_router
from routes.questions import questions_router
from routes.results import results_router


api = APIRouter()


api.include_router(categories_router)
api.include_router(questions_router)
api.include_router(answers_router)
api.include_router(results_router)
api.include_router(final_results_router)
api.include_router(users_router)
api.include_router(login_router)


