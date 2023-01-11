from fastapi import FastAPI
import uvicorn

from app.schemas import Data
from app import functions as func

app = FastAPI(title="Web-приложение для определения заполненных форм")


@app.post("/get_form")
async def get_form(data: Data):
    # разделяем строку со списком полей на ключи-значения
    form_field_val_dict = func.separate_fields(data.fields_values)
    # определяем типы полей
    form_field_type_dict = func.get_field_type(form_field_val_dict)
    # находим подходящий шаблон в бд
    template_name = func.get_template_name(form_field_type_dict)
    if len(template_name) > 0:
        return template_name
    else:
        # если шаблона нет, отправляем поля-типы полученной формы
        form_field_type_str = func.compose_str(form_field_type_dict)
        return form_field_type_str


# для отладки
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8002)
