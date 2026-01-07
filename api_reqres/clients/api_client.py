import allure
from api_reqres.utils.logger import send_request_logger
from api_reqres.utils.config import API_KEY


class ApiClient:
    @staticmethod
    @allure.step("Отправка API запроса")
    def send_request(method, url, data=None, headers=None):
        if headers is None:
            headers = API_KEY
        response = send_request_logger(method=method.upper(), url=url, json=data, headers=headers)
        return response


api_client = ApiClient()
