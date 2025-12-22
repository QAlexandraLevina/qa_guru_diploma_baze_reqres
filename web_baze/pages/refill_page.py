import allure
from selene import browser, have, be


class RefillPage:
    def __init__(self):
        self.button_payment_method = browser.element(".top-up__method-select")
        self.drop_down_list_currency = browser.element(".ui-select")
        self.list_currency = browser.all(".ui-select__option-item")
        self.list_payment_method = browser.all(".top-up-method-select__select-item")
        self.field_amount_refill = browser.element(".text-field__input")
        self.field_converter = browser.element(".top-up__converter-output")
        self.check_boxes = browser.all(".ui-checkbox__label")
        self.button_top_up = browser.element(".top-up__replenish")
        self.bonus_tiles = browser.all(".top-up-bonus-card")
        self.active_bonus_tile = browser.element(".top-up-bonus-card--active")

    @allure.step("Выбор валюты для пополнения")
    def select_list_currency(self, currency):
        self.drop_down_list_currency.click()
        self.list_currency.should(have.size_greater_than(0))
        if currency == "USD":
            self.list_currency.first.click()
        else:
            self.list_currency.second.click()
        return self

    @allure.step("Нажатие на кнопку 'Выберите способ оплаты'")
    def click_button_payment_method(self):
        self.button_payment_method.click()
        return self

    def click_payment_methods(self, text):
        self.list_payment_method.element_by(have.text(text)).click()
        return self

    @allure.step("Выбор 'СБП' для способа оплаты")
    def click_sbp_method(self):
        return self.click_payment_methods("СБП")

    @allure.step("Выбор 'Sberpay' для способа оплаты")
    def click_sberpay_method(self):
        return self.click_payment_methods("Sberpay")

    @allure.step("Выбор 'USDT TRC20' для способа оплаты")
    def click_usdt_method(self):
        return self.click_payment_methods("USDT TRC20")

    @allure.step("Проставление галочек в чек-боксах")
    def click_check_boxes(self):
        self.check_boxes.element_by(have.text("Я ознакомлен и согласен с условиями ")).click()
        self.check_boxes.element_by(have.text("Я понимаю и согласен, что после получения Игровой валюты")).click()
        return self

    @allure.step("Заполнение поля суммы пополнения")
    def fill_field_amount_refill(self, amount_ref):
        self.field_amount_refill.type(amount_ref)
        return self

    @allure.step("Выбор бонуса к пополнению")
    def select_bonus(self, bonus_name):
        self.bonus_tiles.element_by(have.text(bonus_name)).click()
        return self

    @allure.step("Проверка заполненного поля суммы пополнения")
    def should_have_correct_amount(self, expected_amount):
        self.field_amount_refill.should(have.value(expected_amount))
        return self

    @allure.step("Проверка конвертации валюты в WIN coin")
    def should_have_correct_conversion(self, expected_conversion):
        self.field_converter.should(have.text(expected_conversion))
        return self

    @allure.step("Проверка отображения и кликабельности кнопки 'Пополнить'")
    def should_link_to_button_top_up(self):
        self.button_top_up.should(be.visible).should(be.clickable)
        return self

    @allure.step("Проверка отсутствия активного бонуса")
    def should_bonus_be_not_active(self):
        self.active_bonus_tile.should(be.not_.present)
        return self

    @allure.step("Проверка наличия активного бонуса")
    def should_bonus_be_active(self, bonus_name):
        self.active_bonus_tile.should(have.text(bonus_name))
        return self