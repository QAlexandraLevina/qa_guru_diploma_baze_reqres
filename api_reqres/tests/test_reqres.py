import pytest
import allure
from api_reqres.utils.api_client import api_client
from api_reqres.utils.schemas import post_user_create_schema, get_single_user_schema, put_update_user_schema, post_unsuccessful_login_schema
from jsonschema import validate


@pytest.mark.api
@allure.title("Создание пользователя")
def test_create_user(base_url):
    data = {"name": "morpheus", "job": "leader"}

    response = api_client.send_request('POST', f"{base_url}users", data)

    with allure.step("Проверка статус кода 201"):
        assert response.status_code == 201

    with allure.step("Проверка данных ответа"):
        assert response.json()["name"] == data["name"]
        assert response.json()["job"] == data["job"]

    with allure.step("Валидация схемы ответа"):
        validate(response.json(), post_user_create_schema)


@pytest.mark.api
@allure.title("Получение информации о пользователе")
def test_get_user(base_url):
    response = api_client.send_request('GET', f"{base_url}users/2")

    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200

    with allure.step("Валидация схемы ответа"):
        validate(response.json(), get_single_user_schema)


@pytest.mark.api
@allure.title("Обновление пользователя")
def test_update_user(base_url):
    data = {"name": "lawrence", "job": "actor"}

    response = api_client.send_request('PUT', f"{base_url}users/2", data)

    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200

    with allure.step("Проверка данных ответа"):
        assert response.json()["name"] == data["name"]
        assert response.json()["job"] == data["job"]

    with allure.step("Валидация схемы ответа"):
        validate(response.json(), put_update_user_schema)


@pytest.mark.api
@allure.title("Удаление пользователя")
def test_delete_user(base_url):
    response = api_client.send_request('DELETE', f"{base_url}users/2")

    with allure.step("Проверка статус кода 204"):
        assert response.status_code == 204

    with allure.step("Проверка пустого ответа"):
        assert response.text == ''


@pytest.mark.api
@allure.title("Неуспешная регистрация пользователя")
def test_unsuccessful_login(base_url):
    data = {"email": "peter@klaven"}

    response = api_client.send_request('POST', f"{base_url}login", data)

    with allure.step("Проверка статус кода 400"):
        assert response.status_code == 400

    with allure.step("Проверка сообщений об ошибке"):
        assert "error" in response.json()

    with allure.step("Валидация схемы ответа"):
        validate(response.json(), post_unsuccessful_login_schema)