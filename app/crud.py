from tinydb import TinyDB, Query

db = TinyDB('./db_templates.json')

Template = Query()


def get_templates(form_field_type: dict):
    """ получаем шаблоны из бд по словарю """
    return db.search(Template.fragment(form_field_type))


def get_templates2(template_name: list):
    """ получаем шаблоны из бд по списку имен """
    return db.search(Template['templ_name'].one_of(template_name))
