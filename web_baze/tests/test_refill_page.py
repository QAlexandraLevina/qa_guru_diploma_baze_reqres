import allure
import pytest
from web_baze.pages.refill_page import RefillPage


refill_page = RefillPage()

@pytest.mark.web
@allure.title("Пополнение без бонуса")
def test_refill_page_without_bonus(open_refill_page):
    """
    Проверка полного flow пополнения счёта без бонуса.
    Внешние платёжные системы не тестируем из-за ограничений анти-бот систем.
    """

    (refill_page
     .select_list_currency('RUS')
     .click_button_payment_method()
     .click_sbp_method()
     .click_check_boxes()
     .fill_field_amount_refill('100')
     .should_have_correct_conversion('33')
    .should_bonus_be_not_active()
     .should_link_to_button_top_up()
    )


@pytest.mark.web
@allure.title("Автоматическая активация бонуса при вводе суммы")
@pytest.mark.parametrize('input_amount, expected_bonus, expected_conversion', [
    ('300', '100\n+20', '100\n+20'),
    ('2250', '750\n+130', '750\n+130'),
])
def test_bonus_auto_activation(open_refill_page, input_amount, expected_bonus, expected_conversion):
    """Проверка автоматической активации бонуса при вводе определённой суммы"""

    (refill_page
     .select_list_currency('RUS')
     .click_button_payment_method()
     .click_sbp_method()
     .click_check_boxes()
     .fill_field_amount_refill(input_amount)
     .should_bonus_be_active(expected_bonus)
     .should_have_correct_conversion(expected_conversion)
     .should_link_to_button_top_up()
     )


@pytest.mark.web
@allure.title("Ручной выбор бонуса кликом на плитку")
@pytest.mark.parametrize('bonus_name, expected_amount, expected_conversion', [
    ('100\n+20', '300', '100\n+20'),
    ('750\n+130', '2250', '750\n+130'),
])
def test_bonus_manual_select(open_refill_page, bonus_name, expected_amount, expected_conversion):
    """Проверка активации плитки и заполнения суммы пополнения при клике на бонус"""

    (refill_page
     .select_list_currency('RUS')
     .click_button_payment_method()
     .click_sbp_method()
     .click_check_boxes()
     .select_bonus(bonus_name)
     .should_have_correct_amount(expected_amount)
     .should_bonus_be_active(bonus_name)
     .should_have_correct_conversion(expected_conversion)
     .should_link_to_button_top_up()
     )