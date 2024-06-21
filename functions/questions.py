from sqlalchemy.orm import joinedload
from models.categories import Categories
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.questions import Questions


def get_questions(ident, search, page, limit, db):
    if ident > 0:
        ident_filter = Questions.id == ident
    else:
        ident_filter = Questions.id > 0

    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Questions.question.like(search_formatted))
    else:
        search_filter = Questions.id > 0

    items = (db.query(Questions).options(joinedload(Questions.category))
             .filter(ident_filter, search_filter).order_by(Questions.id.desc()))

    return pagination(items, page, limit)


def create_question(forms, db):
    for form in forms:
        get_in_db(db, Categories, form.category_id)
        new_item_db = Questions(
            question=form.question,
            category_id=form.category_id
        )
        save_in_db(db, new_item_db)


def update_question(form, db):
    get_in_db(db, Categories, form.category_id), get_in_db(db, Questions, form.id)
    db.query(Questions).filter(Questions.id == form.id).update({
        Questions.question: form.question,
        Questions.category_id: form.category_id
    })
    db.commit()


def delete_question(ident, db):
    get_in_db(db, Questions, ident)
    db.query(Questions).filter(Questions.id == ident).delete()
    db.commit()
