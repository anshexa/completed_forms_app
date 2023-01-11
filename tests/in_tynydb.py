# создание тестовой бд
from tinydb import TinyDB

db = TinyDB('../db_templates.json')

# запись в бд
db.insert({
    "templ_name": "Form template1 name",
    "field_date_1_1": "date",
    "field_phone_1_2": "phone",
    "field_email_1_3": "email",
    "field_text_1_4": "text",
})
db.insert({
    "templ_name": "Form template2 name",
    "field_date_2_1": "date",
    "field_phone_2_2": "phone",
    "field_email_2_3": "email",
})
db.insert({
    "templ_name": "Form template3 name",
    "field_date_3_1": "date",
    "field_phone_3_2": "phone",
    "field_text_3_3": "text",
})
db.insert({
    "templ_name": "Form template4 name",
    "field_date_4_1": "date",
    "field_email_4_2": "email",
    "field_text_4_3": "text",
})
db.insert({
    "templ_name": "Form template5 name",
    "field_phone_5_1": "phone",
    "field_email_5_2": "email",
    "field_text_5_3": "text",
})
db.insert({
    "templ_name": "Form template6 name",
    "field_date_6_1": "date",
    "field_phone_6_2": "phone",
})
db.insert({
    "templ_name": "Form template7 name",
    "field_date_7_1": "date",
    "field_email_7_2": "email",
})
db.insert({
    "templ_name": "Form template8 name",
    "field_date_8_1": "date",
    "field_text_8_2": "text",
})
db.insert({
    "templ_name": "Form template9 name",
    "field_phone_9_1": "phone",
    "field_email_9_2": "email",
})
db.insert({
    "templ_name": "Form template10 name",
    "field_phone_10_1": "phone",
    "field_text_10_2": "text",
})
db.insert({
    "templ_name": "Form template11 name",
    "field_email_11_1": "email",
    "field_text_11_2": "text",
})
db.insert({
    "templ_name": "Form template12 name",
    "field_date_12_1": "date",
})
db.insert({
    "templ_name": "Form template13 name",
    "field_phone_13_1": "phone",
})
db.insert({
    "templ_name": "Form template14 name",
    "field_email_14_1": "email",
})
db.insert({
    "templ_name": "Form template15 name",
    "field_text_15_1": "text",
})
# /**********повторяются сочетания типов, но с другими названиями полей
db.insert({
    "templ_name": "Form template16 name",
    "field_date_16_1": "date",
    "field_phone_16_2": "phone",
    "field_email_16_3": "email",
    "field_text_16_4": "text",
})
db.insert({
    "templ_name": "Form template17 name",
    "field_date_17_1": "date",
    "field_phone_17_2": "phone",
    "field_email_17_3": "email",
})
db.insert({
    "templ_name": "Form template18 name",
    "field_date_18_1": "date",
    "field_phone_18_2": "phone",
    "field_text_18_3": "text",
})
db.insert({
    "templ_name": "Form template19 name",
    "field_date_19_1": "date",
    "field_email_19_2": "email",
    "field_text_19_3": "text",
})
db.insert({
    "templ_name": "Form template20 name",
    "field_phone_20_1": "phone",
    "field_email_20_2": "email",
    "field_text_20_3": "text",
})
db.insert({
    "templ_name": "Form template21 name",
    "field_date_21_1": "date",
    "field_phone_21_2": "phone",
})
db.insert({
    "templ_name": "Form template22 name",
    "field_date_22_1": "date",
    "field_email_22_2": "email",
})
db.insert({
    "templ_name": "Form template23 name",
    "field_date_23_1": "date",
    "field_text_23_2": "text",
})
db.insert({
    "templ_name": "Form template24 name",
    "field_phone_24_1": "phone",
    "field_email_24_2": "email",
})
db.insert({
    "templ_name": "Form template25 name",
    "field_phone_25_1": "phone",
    "field_text_25_2": "text",
})
db.insert({
    "templ_name": "Form template26 name",
    "field_email_26_1": "email",
    "field_text_26_2": "text",
})
db.insert({
    "templ_name": "Form template27 name",
    "field_date_27_1": "date",
})
db.insert({
    "templ_name": "Form template28 name",
    "field_phone_28_1": "phone",
})
db.insert({
    "templ_name": "Form template29 name",
    "field_email_29_1": "email",
})
db.insert({
    "templ_name": "Form template30 name",
    "field_text_30_1": "text",
})
# /**********повторяются сочетания типов с названиями полей
db.insert({
    "templ_name": "Form template31 name",
    "field_date_31_1": "date",
    "field_phone_1_2": "phone",  # это поле и тип повторяется
})
db.insert({
    "templ_name": "Form template32 name",
    "field_date_1_1": "date",  # это поле и тип повторяется
    "field_phone_1_2": "phone",  # это поле и тип повторяется
})
db.insert({
    "templ_name": "Form template33 name",
    "field_date_1_1": "date",  # это поле и тип повторяется
    "field_phone_1_2": "phone",  # это поле и тип повторяется
    "field_email_1_3": "email",  # это поле и тип повторяется
    "field_text_1_4": "text",  # это поле и тип повторяется
    "доп_text_поле": "text",
})
