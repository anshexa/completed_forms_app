import datetime
import re

from app import crud


def separate_fields(fields_values: str) -> dict:
    """ разделяем на ключи-значения """
    form_field_val = {}
    fields_lst = fields_values.split('&')
    for field in fields_lst:
        lst = field.split('=')
        field_name = lst[0]
        val = lst[1]
        form_field_val[field_name] = val
    return form_field_val


def get_field_type(form_field_val: dict) -> dict:
    """ определяем типы полей """
    form_field_type = {}
    for field_name, field_val in form_field_val.items():
        type = search_type(field_val)
        form_field_type[field_name] = type
    return form_field_type


def search_type(val: str, i=1):
    """
    проверяем на форматы дата, телефон, email, текст,
    возвращаем подходящий тип
    """
    type = 'text'
    try:
        if i == 1:
            search_date = datetime.datetime.strptime(val, "%d.%m.%Y")
            type = 'date'  # найдено
        if i == 2:
            search_date = datetime.datetime.strptime(val, "%Y-%m-%d")
            type = 'date'  # найдено
        if i == 3:
            search_phone = re.match("^\+7\s[0-9]{3}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}$", val)
            assert (search_phone is not None), (val, 'does not match format phone')
            type = 'phone'  # найдено
        if i == 4:
            search_email = re.match("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+", val)
            assert (search_email is not None), (val, 'does not match format email')
            type = 'email'  # найдено
        return type
    except Exception as _e:
        # если не соответствует формату, прерываем, вызываем исключение,
        # делаем следующую проверку
        return search_type(val, i + 1)


def compose_str(form_field_type: dict) -> str:
    """ собираем строку из словаря с типом полей """
    field_type_str = ''
    for field_name, field_type in form_field_type.items():
        if len(field_type_str) > 0:
            field_type_str = '{}, {}: {}'.format(field_type_str, field_name, field_type.upper())
        else:
            field_type_str = '{}: {}'.format(field_name, field_type.upper())
    field_type_str = '{{ {} }}'.format(field_type_str)
    return field_type_str


def get_template_name(form_field_type: dict):
    """ получаем имя шаблона, наиболее подходящего полям формы """
    # находим шаблоны, где встречаются поля формы
    template_lst = search_matching_templates(form_field_type)
    # отбираем подходящий шаблон
    template_name = find_best_template(template_lst, form_field_type)
    if len(template_name) > 0:
        return template_name
    else:
        return ''


def search_matching_templates(form_field_type: dict) -> list:
    """ находим список шаблонов, в которых встречаются поля формы """
    # ищем по всей форме
    templ_lst = crud.get_templates(form_field_type)
    if len(templ_lst) == 0:
        templ_name_lst = []
        # если в форме больше полей, чем в шаблоне, ищем по каждому полю
        for field_name, field_type in form_field_type.items():
            templ_lst = crud.get_templates({field_name: field_type})
            if len(templ_lst) > 0:
                for templ in templ_lst:
                    templ_name_lst.append(templ['templ_name'])
        templ_name_lst = list(set(templ_name_lst))
        templ_lst = crud.get_templates2(templ_name_lst)
    return templ_lst


def find_best_template(template_lst: list, form_field_type: dict) -> str:
    """ отбираем самый подходящий шаблон, возвращаем его имя """
    templ_names_dict = {}
    for templ_obj in template_lst:
        # вес, сколько полей шаблона совпадают с формой
        weight = 0
        for field_name, field_type in templ_obj.items():
            # оставляем шаблоны, все поля которых присутствуют в форме
            if field_name != 'templ_name':
                if field_name in form_field_type and \
                        field_type == form_field_type[field_name]:
                    weight += 1
                    templ_names_dict[templ_obj['templ_name']] = weight
                else:
                    if templ_obj['templ_name'] in templ_names_dict:
                        templ_names_dict.pop(templ_obj['templ_name'])
                    break
    # оставляем один с max весом
    if len(templ_names_dict) > 0:
        template_name = max(templ_names_dict, key=templ_names_dict.get)
        return template_name
    else:
        return ''
