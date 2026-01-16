import allure
from selene import browser, be
from selene.core.exceptions import TimeoutException


@allure.step("Проверка отображения и закрытие модального окна 'Колесо фортуны'")
def close_fortune_modal():
    modal = browser.element(".about-lucky-circle__lucky-circle")
    try:
        modal.should(be.visible, timeout=10)
        browser.element(".about-lucky-circle__close").click()
    except TimeoutException:
        pass