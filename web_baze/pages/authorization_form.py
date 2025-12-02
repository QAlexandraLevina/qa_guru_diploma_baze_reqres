from web_baze.data.users import UserData
from selene import browser, have


class AuthorizationForm:
    def __init__(self):
        self.personal_account_tab = browser.all(".header__menu-item")
        self.button_authorization = browser.all(".ui-button--overflow-hidden")
        self.field_mail = browser.element(".text-field__input[name='email']")
        self.field_password = browser.element("input[name='password']")
        self.check_box_remember_me = browser.element(".ui-checkbox__box")
        self.authorized_profile = browser.element(".header__menu-item--profile")
        self.text_user_points = browser.element("h4.account-data__user-points-title")


    def click_personal_account_tab(self):
        self.personal_account_tab.element_by(have.text("РЕГИСТРАЦИЯ")).click()


    def click_button_authorization(self):
        self.button_authorization.element_by(have.text('Вход в аккаунт')).click()
        return self


    def fill_field_mail(self, par_email):
        self.field_mail.type(par_email)
        return self


    def fill_field_password(self, par_password):
        self.field_password.type(par_password)
        return self


    def click_check_box_remember_me(self):
        self.check_box_remember_me.click()
        return self


    def click_button_log_in(self):
        self.button_authorization.element_by(have.text("войти в аккаунт")).click()
        return self


    """Проверка авторизации после заполнения полей"""
    def should_authorized_profile(self):
        self.text_user_points.should(have.text("ОЧКИ ПЕРСОНАЖА"))
        browser.should(have.url_containing("/account"))  # Проверка, что после авторизации происходит редирект на /account
        return self


    """Авторизация пользователя"""
    def authorization_user(self, user: UserData):
        self.click_personal_account_tab()
        self.click_button_authorization()
        self.fill_field_mail(user.mail)
        self.fill_field_password(user.password)
        self.click_check_box_remember_me()
        self.click_button_log_in()