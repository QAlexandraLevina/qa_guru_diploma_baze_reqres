from selene import browser, be, have


class Footer:
    VKONTAKTE_TEXT_LINK = "VKONTAKTE"
    TELEGRAM_TEXT_LINK = "TELEGRAM"
    DISCORD_TEXT_LINK = "DISCORD"
    YOUTUBE_TEXT_LINK = "YOUTUBE"
    USER_AGREEMENT_TEXT_LINK = "ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"
    PRIVACY_POLICY_TEXT_LINK = "ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ"
    PROJECT_RULES_TEXT_LINK = "ПРАВИЛА ПРОЕКТА"
    DISCLAIMER_TEXT = ("BAZE RP НЕ СВЯЗАНА, НЕ СПОНСИРУЕТСЯ И НЕ ПОДДЕРЖИВАЕТСЯ КОМПАНИЕЙ TAKE-TWO INTERACTIVE SOFTWARE, INC. (ROCKSTAR GAMES). "
                   "ВСЕ ИСПОЛЬЗУЕМЫЕ ТОРГОВЫЕ МАРКИ И ДРУГИЕ ПРЕДМЕТЫ ИНТЕЛЛЕКТУАЛЬНОЙ СОБСТВЕННОСТИ ЯВЛЯЮТСЯ СОБСТВЕННОСТЬЮ СООТВЕТСТВУЮЩИХ ВЛАДЕЛЬЦЕВ.")
    COPYRIGHT_LOGO_TEXT = "BAZE © 2025"
    ORGANIZATION_NAME_TEXT = 'ООО "EDUCATION STUDIO"'
    INN_TEXT = "ИНН 311 619 091"
    ORGANIZATION_ADDRESS_TEXT = "BARHAYOT MFY, 12 MAVZESI , 20А-UY"

    def __init__(self):
        self.top_footer_logo = browser.element(".footer-top__logo")
        self.top_footer_small_logo = browser.element(".footer-top__small-logo")
        self.disclaimer = browser.element(".disclaimer")
        self.bottom_footer_info = browser.element(".info")
        self.bottom_footer_payments = browser.element(".payment-methods")
        self.vkontakte_link = browser.element("li a[href='https://vk.com/rpbaze']")
        self.telegram_link = browser.element("li a[href='https://t.me/bazerp")
        self.discord_link = browser.element("li a[href='https://discord.com/invite/baze")
        self.youtube_link = browser.element("li a[href='https://www.youtube.com/@Baze_RP")
        self.user_agreement_link = browser.element("a[href='/user-agreement']")
        self.privacy_policy_link = browser.element("a[href='/privacy-policy']")
        self.project_rules_link = browser.element(".links__list li:nth-child(3) .links__item") # НЕТ ССЫЛКИ В HTML


    """Проверка ссылок на сторонние сайты и страницы BAZE RP"""
    def should_link_to_vkontakte(self):
        self.vkontakte_link.should(be.visible).should(be.clickable)
        return self


    def should_link_to_telegram(self):
        self.telegram_link.should(be.visible).should(be.clickable)
        return self

    def should_link_to_discord(self):
        self.discord_link.should(be.visible).should(be.clickable)
        return self

    def should_link_to_youtube(self):
        self.youtube_link.should(be.visible).should(be.clickable)
        return self

    def should_link_to_user_agreement_page(self):
        self.user_agreement_link.should(be.visible).should(be.clickable)
        return self

    def should_link_to_privacy_policy_page(self):
        self.privacy_policy_link.should(be.visible).should(be.clickable)
        return self


    def should_link_to_project_rules_page(self):
        self.project_rules_link.should(be.visible).should(be.clickable)
        return self


    """Проверка отображения названий ссылок"""
    def should_display_correct_names_links(self):
        self.vkontakte_link.should(have.text(self.VKONTAKTE_TEXT_LINK))
        self.telegram_link.should(have.text(self.TELEGRAM_TEXT_LINK))
        self.discord_link.should(have.text(self.DISCORD_TEXT_LINK))
        self.youtube_link.should(have.text(self.YOUTUBE_TEXT_LINK))
        self.user_agreement_link.should(have.text(self.USER_AGREEMENT_TEXT_LINK))
        self.privacy_policy_link.should(have.text(self.PRIVACY_POLICY_TEXT_LINK))
        self.project_rules_link.should(have.text(self.PROJECT_RULES_TEXT_LINK))
        return self


    """Проверка отображения текстовой части футера"""
    def should_display_texts_footer(self):
        self.top_footer_logo.should(be.visible)
        self.top_footer_small_logo.should(be.visible).should(have.text(self.COPYRIGHT_LOGO_TEXT))
        self.disclaimer.should(be.visible).should(have.exact_text(self.DISCLAIMER_TEXT))
        self.bottom_footer_info.should(be.visible).should(have.text(self.ORGANIZATION_NAME_TEXT))
        self.bottom_footer_info.should(be.visible).should(have.text(self.INN_TEXT))
        self.bottom_footer_info.should(be.visible).should(have.text(self.ORGANIZATION_ADDRESS_TEXT))
        self.bottom_footer_payments.should(be.visible)
        return self