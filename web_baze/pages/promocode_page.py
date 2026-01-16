import allure
from selene import browser, have, be


class PromocodePage:
    CONFIRMATION_BUTTON_TEXT = "Подтвердить"
    DISPLAY_ERROR_MESSAGE_TEXT = "Неизвестная ошибка"
    INVALID_PROMOCODE_TEXT = "INVALID"

    def __init__(self):
        self.field_promocode = browser.element(".text-field__input")
        self.confirmation_button = browser.all(".ui-button__text")
        self.error_message = browser.element(".notification__message")

    @allure.step("Заполнение поля 'Введите код'")
    def fill_field_promocode(self):
        self.field_promocode.type(self.INVALID_PROMOCODE_TEXT)
        return self

    @allure.step("Нажатие на кнопку 'Подтвердить'")
    def click_confirmation_button(self):
        self.confirmation_button.element_by(have.text(self.CONFIRMATION_BUTTON_TEXT)).click()
        return self

    @allure.step("Проверка отображения уведомления о невалидном промокоде")
    def should_display_error_message(self):
        self.error_message.should(have.text(self.DISPLAY_ERROR_MESSAGE_TEXT)).should(be.visible)
        return self