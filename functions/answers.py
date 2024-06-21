from sqlalchemy.orm import joinedload
from models.answers import Answers
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.questions import Questions


def get_answers(ident, search, page, limit, db):

    if ident > 0:
        ident_filter = Answers.id == ident
    else:
        ident_filter = Answers.id > 0

    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Answers.answer.like(search_formatted))
    else:
        search_filter = Questions.id > 0

    items = (db.query(Answers).options(joinedload(Answers.question))
             .filter(ident_filter, search_filter).order_by(Answers.id.desc()))

    return pagination(items, page, limit)


def create_answer(forms, db):
    for form in forms:
        get_in_db(db, Questions, form.question_id)
        new_item_db = Answers(
            answer=form.answer,
            status=form.status,
            question_id=form.question_id
        )
        save_in_db(db, new_item_db)


def update_answer(form, db):
    get_in_db(db, Questions, form.question_id), get_in_db(db, Answers, form.id)
    db.query(Answers).filter(Answers.id == form.id).update({
        Answers.answer: form.answer,
        Answers.status: form.status,
        Answers.question_id: form.question_id
    })
    db.commit()


def delete_answer(ident, db):
    get_in_db(db, Answers, ident)
    db.query(Answers).filter(Answers.id == ident).delete()
    db.commit()


