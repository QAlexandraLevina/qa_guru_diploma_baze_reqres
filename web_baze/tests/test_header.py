# import time
# import allure
# import pytest
# from selene import be
# from web_baze.pages.authorization_form import AuthorizationForm
# from web_baze.pages.header import Header
#
#
# header = Header()
# auth_form = AuthorizationForm()
#
# @pytest.mark.web
# @allure.title("Проверка элементов хедера и переход по каждой вкладке")
# @allure.feature('Test Case #1: Проверка хедера у неавторизованного пользователя')
# def test_header_unauthorized_user(setup_browser):
#     browser = setup_browser
#
#     browser.open("/")
#
#     """Закрытие модального окна 'Колесо фортуны'"""
#     try:
#         time.sleep(2)
#         browser.element(".about-lucky-circle__lucky-circle").should(be.visible)
#         browser.element(".about-lucky-circle__close").click()
#     except:
#         pass
#
#     header.should_have_menu_items_unauthorized()
#
#     header.click_all_tabs_header_unauthorized()
#
#
# @pytest.mark.web
# @allure.title("Проверка авторизованного пользователя")
# @allure.feature('Test Case #2: Проверка хедера у авторизованного пользователя')
# def test_header_authorized_user(authenticated_user):
#
#     auth_form.should_authorized_profile()
#
#     header.should_have_menu_items_authorized(authenticated_user)
#
#     header.click_all_tabs_header_authorized()
#
#
# @pytest.mark.web
# @allure.title("Проверка выхода из аккаунта")
# def test_log_out(authenticated_user):
#
#     header.click_log_out_tab()
#
#     header.should_have_menu_items_unauthorized()