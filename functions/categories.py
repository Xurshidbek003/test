from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.categories import Categories


def get_categories(ident, search, page, limit, db):

    if ident > 0:
        ident_filter = Categories.id == ident
    else:
        ident_filter = Categories.id > 0

    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Categories.name.like(search_formatted))
    else:
        search_filter = Categories.id > 0

    items = db.query(Categories).filter(ident_filter, search_filter).order_by(Categories.id.desc())

    return pagination(items, page, limit)


def create_category(form, db):
    new_item_db = Categories(
        name=form.name)
    save_in_db(db, new_item_db)


def update_category(form, db):
    get_in_db(db, Categories, form.id)
    db.query(Categories).filter(Categories.id == form.id).update({
        Categories.name: form.name
    })
    db.commit()


def delete_category(ident, db):
    get_in_db(db, Categories, ident)
    db.query(Categories).filter(Categories.id == ident).delete()
    db.commit()


