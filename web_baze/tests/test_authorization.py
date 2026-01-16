import allure
import pytest
from web_baze.pages.authorization_form import AuthorizationForm
from web_baze.utils.modal_helper import close_fortune_modal


@pytest.mark.web
@allure.title("Авторизация и проверка авторизации пользователя")
def test_authorization_form(setup_browser, user_authorized):
    browser = setup_browser

    browser.open("/")

    close_fortune_modal()

    authorization_form = AuthorizationForm()

    with allure.step("Авторизация пользователя"):
        authorization_form.authorization_user(user_authorized)

    with allure.step("Проверка авторизованного пользователя"):
        authorization_form.should_authorized_profile()