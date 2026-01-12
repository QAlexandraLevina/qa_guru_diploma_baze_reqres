import allure
from selene import browser, have, be
from web_baze.data.users import UserData


class Header:
    TAB_TEXT_MAIN = "ГЛАВНАЯ"
    TAB_TEXT_COMMUNITY = "СООБЩЕСТВА"
    TAB_TEXT_RATING = "РЕЙТИНГ"
    TAB_TEXT_NEWS = "НОВОСТИ"
    TAB_TEXT_ROADMAP = "ДОРОЖНАЯ КАРТА"
    TAB_TEXT_REGISTRATION = "РЕГИСТРАЦИЯ"
    TAB_TEXT_REFILL = "ПОПОЛНЕНИЕ"
    TAB_TEXT_PROMOCODE = "ПРОМОКОД"
    EXPECTED_TAB_TEXT_UNAUTHORIZED = [TAB_TEXT_MAIN, TAB_TEXT_COMMUNITY, TAB_TEXT_RATING, TAB_TEXT_NEWS,
                                      TAB_TEXT_ROADMAP, TAB_TEXT_REGISTRATION]
    EXPECTED_TAB_TEXT_AUTHORIZED = [TAB_TEXT_MAIN, TAB_TEXT_COMMUNITY, TAB_TEXT_RATING, TAB_TEXT_NEWS, TAB_TEXT_ROADMAP,
                                    TAB_TEXT_REFILL, TAB_TEXT_PROMOCODE]

    def __init__(self):
        """Вкладки для неавторизованного пользователя"""
        self.logo_unauthorized = browser.element(".header__logo")
        self.tabs_header_unauthorized = browser.all(".header__menu-item")

        """Вкладки у авторизованного пользователя"""
        self.logo_authorized = browser.element(".header__logo")
        self.tabs_header_authorized = browser.all(".header__menu-item")
        self.mail_name_tab = browser.element(".header__menu-item--profile")
        self.notification_tab_open = browser.element("button.header__menu-link")
        self.notification_tab_close = browser.element("[data-v-b1c9d48e][data-v-d0da1ffa]")
        self.setting_tab = browser.element("a.header__menu-link")
        self.log_out_tab = browser.element(".ui-box--hoverable[style*='color-white-15']")

    """Шаги для неавторизованного пользователя"""

    def click_tabs_unauthorized(self, text):
        self.tabs_header_unauthorized.element_by(have.text(text)).click()
        return self

    def click_community_tab_unauthorized(self):
        self.click_tabs_unauthorized(self.TAB_TEXT_COMMUNITY)
        return self

    def click_rating_tab_unauthorized(self):
        self.click_tabs_unauthorized(self.TAB_TEXT_RATING)
        return self

    def click_news_tab_unauthorized(self):
        self.click_tabs_unauthorized(self.TAB_TEXT_NEWS)
        return self

    def click_roadmap_tab_unauthorized(self):
        self.click_tabs_unauthorized(self.TAB_TEXT_ROADMAP)
        return self

    def click_registration_tab_unauthorized(self):
        self.click_tabs_unauthorized(self.TAB_TEXT_REGISTRATION)
        return self

    @allure.step("Проверка отображения элементов хедера неавторизованным пользователем")
    def should_have_menu_items_unauthorized(self):
        self.logo_unauthorized.should(be.visible)
        for item in self.EXPECTED_TAB_TEXT_UNAUTHORIZED:
            self.tabs_header_unauthorized.element_by(have.text(item)).should(be.visible)
        return self

    @allure.step("Прокликивание элементов хедера неавторизованным пользователем")
    def click_all_tabs_header_unauthorized(self):
        self.click_community_tab_unauthorized()
        self.click_rating_tab_unauthorized()
        self.click_news_tab_unauthorized()
        self.click_news_tab_unauthorized()
        self.click_roadmap_tab_unauthorized()
        self.click_registration_tab_unauthorized()

    """Шаги для авторизованного пользователя"""

    def click_tabs_authorized(self, text):
        self.tabs_header_authorized.element_by(have.text(text)).click()
        return self

    def click_main_tab_authorized(self):
        self.click_tabs_authorized(self.TAB_TEXT_MAIN)
        return self

    def click_refill_tab_authorized(self):
        self.click_tabs_authorized(self.TAB_TEXT_REFILL)
        return self

    def click_promocode_tab_authorized(self):
        self.click_tabs_authorized(self.TAB_TEXT_PROMOCODE)
        return self

    def click_mail_name_tab_authorized(self):
        self.mail_name_tab.click()
        return self

    def click_notification_tabs_authorized(self):
        self.notification_tab_open.click()
        self.notification_tab_close.click()
        return self

    def click_setting_tab_authorized(self):
        self.setting_tab.click()
        return self

    @allure.step("Выход из аккаунта")
    def click_log_out_tab(self):
        self.log_out_tab.click()
        return self

    @allure.step("Проверка отображения элементов хедера авторизованным пользователем")
    def should_have_menu_items_authorized(self, user: UserData):
        self.logo_authorized.should(be.visible)
        for point in self.EXPECTED_TAB_TEXT_AUTHORIZED:
            self.tabs_header_authorized.element_by(have.text(point)).should(be.visible)
        masked_email = f"{user.mail[0].upper()}*******@{user.mail.split('@')[1].upper()}"
        self.mail_name_tab.should(be.visible).should(have.text(masked_email))
        self.notification_tab_open.should(be.visible)
        self.setting_tab.should(be.visible)
        self.log_out_tab.should(be.visible)
        return self

    @allure.step("Прокликивание элементов хедера авторизованным пользователем")
    def click_all_tabs_header_authorized(self):
        self.click_main_tab_authorized()
        self.click_refill_tab_authorized()
        self.click_promocode_tab_authorized()
        self.click_mail_name_tab_authorized()
        self.click_notification_tabs_authorized()
        self.click_setting_tab_authorized()
