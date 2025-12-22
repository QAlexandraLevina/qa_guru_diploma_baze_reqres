import requests
import logging
import json
import allure
from curlify import to_curl
from allure_commons.types import AttachmentType


def send_request_logger(method, url, **kwargs):
    with allure.step(f'Отправка {method} запроса на {url}'):
        response = requests.request(method=method, url=url, **kwargs)

        # Логирование запроса
        curl = to_curl(response.request)
        logging.info(f"CURL: {curl}")
        logging.info(f"Status Code: {response.status_code}")
        allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')

        # Логирование ответа
        try:
            response_json = response.json()
            allure.attach(body=json.dumps(response_json, indent=4, ensure_ascii=False),
                        name='response', attachment_type=AttachmentType.JSON, extension='json')
            logging.info(f"Response: {response_json}")
        except json.JSONDecodeError:
            response_text = response.text if response.text else "Нет содержимого"
            allure.attach(body=response_text, name='response', attachment_type=AttachmentType.TEXT, extension='txt')
            logging.info(f"Response: {response_text}")
    return response