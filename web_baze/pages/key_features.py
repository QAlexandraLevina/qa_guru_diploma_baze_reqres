from selene import browser, have, be


class KeyFeatures:
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
        self.click_feature_tabs("ПЕРСОНАЖ")
        return self


    def click_interactions_with_other_players_tab(self):
        self.click_feature_tabs("ВЗАИМОДЕЙСТВИЯ С ДРУГИМИ ИГРОКАМИ")
        return self


    def click_3d_and_graphics_tab(self):
        self.click_feature_tabs("3D И ГРАФИКА")
        return self


    def click_interfaces_and_server_mechanics_tab(self):
        self.click_feature_tabs("ИНТЕРФЕЙСЫ И СЕРВЕРНЫЕ МЕХАНИКИ")
        return self


    def click_lore_and_plot_tab(self):
        self.click_feature_tabs("ЛОР И СЮЖЕТ")
        return self


    """Проверка отображения заголовка раздела 'Ключевые особенности'"""
    def should_display_title_section(self):
        self.key_feature_title.should(be.visible).should(have.text("КЛЮЧЕВЫЕ ОСОБЕННОСТИ"))
        return self


    """Проверка отображения прогресс-баров под вкладками раздела 'Ключевые особенности'"""
    def should_display_key_feature_progress_bar(self):
        self.key_features_progress_bar.should(have.size(5))
        for i in range(5):
            self.key_features_progress_bar[i].should(be.visible)
        return self


    """Проверка отображения и кликабельности вкладок в разделе 'Ключевые особенности'"""
    def should_display_key_feature_tabs(self):
        tabs_names = ["ПЕРСОНАЖ", "ВЗАИМОДЕЙСТВИЯ С ДРУГИМИ ИГРОКАМИ", "3D И ГРАФИКА", "ИНТЕРФЕЙСЫ И СЕРВЕРНЫЕ МЕХАНИКИ", "ЛОР И СЮЖЕТ"]
        for tab_name in tabs_names:
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