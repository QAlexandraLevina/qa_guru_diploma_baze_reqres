import time
import allure
import pytest
from selene import be
from web_baze.pages.authorization_form import AuthorizationForm


authorization_form = AuthorizationForm()

@pytest.mark.web
@allure.title("Авторизация и проверка авторизации пользователя")
def test_authorization_form(setup_browser, user_authorized):
    browser = setup_browser

    browser.open("/")

    """Закрытие модального окна 'Колесо фортуны'"""
    try:
        time.sleep(2)
        browser.element(".about-lucky-circle__lucky-circle").should(be.visible)
        browser.element(".about-lucky-circle__close").click()
    except:
        pass

    with allure.step("Авторизация пользователя"):
        authorization_form.authorization_user(user_authorized)

    with allure.step("Проверка авторизованного пользователя"):
        authorization_form.should_authorized_profile()