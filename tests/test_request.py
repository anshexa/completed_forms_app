# выполнение тестовых запросов
import requests


def request_post(url, query):
    headers = {
        'accept': 'application/json, text/javascript, /; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'pragma': 'no-cache',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    data = {"fields_values": query}
    response = requests.request("POST", url, json=data, headers=headers)
    if response.status_code == 200:
        resp = response.text
        print(resp)
    else:
        print('error', response.status_code)


url = 'http://127.0.0.1:8000/get_form'
# url = 'http://127.0.0.1:8002/get_form'  # для отладки
query_list = [
    'user_name=Петр&field_date_1_1=07.01.2023&field_phone_1_2=+7 800 000 00 00&field_email_1_3=email@e.ru&field_text_1_4=Привет&доп_text_поле=Поле',
    'user_name=Иван&field_date_1_1=08.01.2023&field_phone_1_2=+7 800 123 00 00&field_email_1_3=email1@e.ru&field_text_1_4=Привет',
    'field_date_1_1=2023-01-07&field_phone_1_2=+7 800 111 11 11&field_email_1_3=email2@e.ru&field_text_1_4=Добрый день',
    'f_name1=value1&f_name2=value2',
]
for query in query_list:
    request_post(url, query)
