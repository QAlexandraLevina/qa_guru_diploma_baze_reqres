import allure
import pytest
from web_baze.pages.promocode_page import PromocodePage


promocode_page = PromocodePage()

@pytest.mark.web
@allure.title("Ввод невалидного промокода")
def test_invalid_promocode_input(open_promocode_page):
    (promocode_page
     .fill_field_promocode("INVALID")
     .click_confirmation_button()
     .should_display_error_message())


### ДЛЯ ДОРАБОТКИ В БУДУЩЕМ ###
# @pytest.mark.web
# @allure.title("Ввод валидного промокода")
# @pytest.mark.parametrize('valid_promocode', [
#     'VALID1', 'VALID2',
# ])
# def test_valid_promocode_input(open_promocode_page, valid_promocode):
#     (promocode_page
#      .fill_field_promocode(valid_promocode)
#      .click_confirmation_button()
#      .should_display_error_message())