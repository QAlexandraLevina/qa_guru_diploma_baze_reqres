from selene import browser, have, be


class KeyFeatures:
    PERSONAGE_TAB_TEXT = "ПЕРСОНАЖ"
    INTERACTIONS_WITH_OTHER_PLAYERS_TAB_TEXT = "ВЗАИМОДЕЙСТВИЯ С ДРУГИМИ ИГРОКАМИ"
    TAB_3D_AND_GRAPHICS_TEXT = "3D И ГРАФИКА"
    INTERFACES_AND_SERVER_MECHANICS_TAB_TEXT = "ИНТЕРФЕЙСЫ И СЕРВЕРНЫЕ МЕХАНИКИ"
    LORE_AND_PLOT_TAB_TEXT = "ЛОР И СЮЖЕТ"
    KEY_FEATURE_TITLE_TEXT = "КЛЮЧЕВЫЕ ОСОБЕННОСТИ"
    KEY_FEATURE_TABS_TEXT = ["ПЕРСОНАЖ", "ВЗАИМОДЕЙСТВИЯ С ДРУГИМИ ИГРОКАМИ", "3D И ГРАФИКА", "ИНТЕРФЕЙСЫ И СЕРВЕРНЫЕ МЕХАНИКИ", "ЛОР И СЮЖЕТ"]


    def __init__(self):
        self.key_feature_title = browser.element(".key-features__title")
        self.key_feature_tabs = browser.all(".key-features__item")
        self.key_feature_description = browser.element(".key-features__description-value")
        self.key_feature_large_preview = browser.element(".key-features__full-img")
        self.key_features_thumbnails = browser.all(".key-features__thumbnails img")
        self.key_features_progress_bar = browser.all(".key-features__progress-bar")


    """Клик по каждой вкладке в разделе 'Ключевые особенности'"""
    def click_feature_tabs(self, tab_name):
        self.key_feature_tabs.element_by(have.text(tab_name)).click()
        return self


    def click_personage_tab(self):
        self.click_feature_tabs(self.PERSONAGE_TAB_TEXT)
        return self


    def click_interactions_with_other_players_tab(self):
        self.click_feature_tabs(self.INTERACTIONS_WITH_OTHER_PLAYERS_TAB_TEXT)
        return self


    def click_3d_and_graphics_tab(self):
        self.click_feature_tabs(self.TAB_3D_AND_GRAPHICS_TEXT)
        return self


    def click_interfaces_and_server_mechanics_tab(self):
        self.click_feature_tabs(self.INTERFACES_AND_SERVER_MECHANICS_TAB_TEXT)
        return self


    def click_lore_and_plot_tab(self):
        self.click_feature_tabs(self.LORE_AND_PLOT_TAB_TEXT)
        return self


    """Проверка отображения заголовка раздела 'Ключевые особенности'"""
    def should_display_title_section(self):
        self.key_feature_title.should(be.visible).should(have.text(self.KEY_FEATURE_TITLE_TEXT))
        return self


    """Проверка отображения прогресс-баров под вкладками раздела 'Ключевые особенности'"""
    def should_display_key_feature_progress_bar(self):
        self.key_features_progress_bar.should(have.size(5))
        for i in range(5):
            self.key_features_progress_bar[i].should(be.visible)
        return self


    """Проверка отображения и кликабельности вкладок в разделе 'Ключевые особенности'"""
    def should_display_key_feature_tabs(self):
        for tab_name in self.KEY_FEATURE_TABS_TEXT:
            self.key_feature_tabs.element_by(have.text(tab_name)).should(be.visible).should(be.clickable)
        return self


    """Проверка отображения крупного превью в разделе 'Ключевые особенности'"""
    def should_display_key_feature_large_preview(self):
        self.key_feature_large_preview.should(be.visible)
        return self


    """Проверка отображения миниатюр во вкладках раздела 'Ключевые особенности'"""
    def should_display_key_feature_thumbnails(self):
        self.key_features_thumbnails.should(have.size(3))
        for i in range(3):
            self.key_features_thumbnails[i].should(be.visible)
        return self