from selene import browser, be, have


class Footer:
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
        self.vkontakte_link.should(have.text("VKONTAKTE"))
        self.telegram_link.should(have.text("TELEGRAM"))
        self.discord_link.should(have.text("DISCORD"))
        self.youtube_link.should(have.text("YOUTUBE"))
        self.user_agreement_link.should(have.text("ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"))
        self.privacy_policy_link.should(have.text("ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ"))
        self.project_rules_link.should(have.text("ПРАВИЛА ПРОЕКТА"))
        return self


    """Проверка отображения текстовой части футера"""
    def should_display_texts_footer(self):
        self.top_footer_logo.should(be.visible)
        self.top_footer_small_logo.should(be.visible).should(have.text("BAZE © 2025"))
        ex_text = ("BAZE RP НЕ СВЯЗАНА, НЕ СПОНСИРУЕТСЯ И НЕ ПОДДЕРЖИВАЕТСЯ КОМПАНИЕЙ TAKE-TWO INTERACTIVE SOFTWARE, INC. (ROCKSTAR GAMES). "
                   "ВСЕ ИСПОЛЬЗУЕМЫЕ ТОРГОВЫЕ МАРКИ И ДРУГИЕ ПРЕДМЕТЫ ИНТЕЛЛЕКТУАЛЬНОЙ СОБСТВЕННОСТИ ЯВЛЯЮТСЯ СОБСТВЕННОСТЬЮ СООТВЕТСТВУЮЩИХ ВЛАДЕЛЬЦЕВ.")
        self.disclaimer.should(be.visible).should(have.exact_text(ex_text))
        self.bottom_footer_info.should(be.visible).should(have.text('ООО "EDUCATION STUDIO'))
        self.bottom_footer_info.should(be.visible).should(have.text('ИНН 311 619 091'))
        self.bottom_footer_info.should(be.visible).should(have.text('BARHAYOT MFY, 12 MAVZESI , 20А-UY'))
        self.bottom_footer_payments.should(be.visible)
        return self