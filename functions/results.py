from sqlalchemy.orm import joinedload
from models.finalresults import FinalResults
from models.users import Users
from utils.db_operations import save_in_db, get_in_db
from utils.pagination import pagination
from models.categories import Categories
from models.questions import Questions
from models.answers import Answers
from models.results import Results
from fastapi import HTTPException


def get_results(ident, search, page, limit, db, user):

    if ident > 0:
        ident_filter = Results.id == ident
    else:
        ident_filter = Results.id > 0

    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Categories.name.like(search_formatted) |
                         Answers.answer.like(search_formatted) |
                         Questions.question.like(search_formatted) |
                         Users.name.like(search_formatted) |
                         Users.username.like(search_formatted))
    else:
        search_filter = Results.id > 0

    items = (db.query(Results)
             .options(joinedload(Results.question),
                      joinedload(Results.answer),
                      joinedload(Results.category),
                      joinedload(Results.user)).filter(ident_filter, search_filter, Results.user_id == user.id)
             .order_by(Results.id.desc()))

    return pagination(items, page, limit)


def create_result(forms, db, user):
    common = 0
    found = 0
    for form in forms:
        question = get_in_db(db, Questions, form.question_id)
        category = get_in_db(db, Categories, form.category_id)
        if question.category_id != category.id:
            raise HTTPException(status_code=400, detail="Bu savol ushbu kategoriyaga tegishli emas!")
        this_answer = get_in_db(db, Answers, form.answer_id)
        if this_answer.question_id != question.id:
            raise HTTPException(status_code=400, detail="Bu javob ushbu savolga tegishli emas!")
        new_item_db = Results(
            question_id=form.question_id,
            answer_id=form.answer_id,
            user_id=user.id,
            category_id=form.category_id
        )
        save_in_db(db, new_item_db)
        common += 1
        if this_answer.status:
            found += 1
    if common != 0:
        percent = found / common * 100
    else:
        percent = 0
    new_final_result = FinalResults(
        common=common,
        found=found,
        percent=percent,
        user_id=user.id
    )
    save_in_db(db, new_final_result)
    return f"Umumiy: {common}, Topildi: {found}, Foizda: {percent}"


def get_final_results(ident, page, limit, db, user):

    if ident > 0:
        ident_filter = FinalResults.id == ident
    else:
        ident_filter = FinalResults.id > 0

    items = (db.query(FinalResults).filter(ident_filter, FinalResults.user_id == user.id)
             .order_by(FinalResults.id.desc()))

    return pagination(items, page, limit)


def get_final_final_results(db, user):

    final_results = db.query(FinalResults).filter(FinalResults.user_id == user.id).all()
    count = 0
    final_common = 0
    final_found = 0
    percent = 0
    for final_result in final_results:
        count += 1
        final_common += final_result.common
        final_found += final_result.found
        percent += final_result.percent
    if count != 0:
        final_percent = percent / count
    else:
        final_percent = 0

    return f"Jami ishlanganlar soni: {final_common}, Jami to'gri topilganlar: {final_found}, Oxirgi natija foizi: {final_percent}"



