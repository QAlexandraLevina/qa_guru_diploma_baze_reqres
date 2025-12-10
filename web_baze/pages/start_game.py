from selene import browser, be, have


class StartGame:
    def __init__(self):
        self.button_play_game = browser.element(".about-buttons__button")
        self.start_game_title = browser.element(".start-game__header-title")
        self.start_game_tabs = browser.all(".start-game__step")
        self.subtitle_tabs = browser.element(".start-game-slide__title")
        self.description_tabs = browser.element(".start-game-slide__description")
        self.steam_link = browser.element("a[href='https://store.steampowered.com/']")
        self.epic_games_link = browser.element("a[href='https://store.epicgames.com/")
        self.rockstar_games_link = browser.element("a[href='https://www.rockstargames.com/")
        self.rage_mp_link = browser.element("a[href='https://rage.mp/ru")
        self.copy_ip = browser.all(".ui-button__inner")


    """Нажатие на кнопку 'Начать игру'"""
    def click_button_play_game(self):
        self.button_play_game.click()
        return self


    """Нажатие на вкладки в разделе 'Как начать играть'"""
    def click_start_game_tabs(self, text):
        self.start_game_tabs.element_by(have.text(text)).click()
        return self


    def click_pay_game_tab(self):
        self.click_start_game_tabs("ПОКУПКА ИГРЫ")
        return self


    def click_launcher_installation_tab(self):
        self.click_start_game_tabs("УСТАНОВКА ЛАУНЧЕРА")
        return self


    def click_connection_tab(self):
        self.click_start_game_tabs("ПОДКЛЮЧЕНИЕ")
        return self


    """Проверка ссылок на сторонние сайты"""
    def should_link_to_steam(self):
        self.steam_link.should(be.visible).should(be.clickable)
        return self


    def should_link_to_epic_games(self):
        self.epic_games_link.should(be.visible).should(be.clickable)
        return self


    def should_link_to_rockstar_games(self):
        self.rockstar_games_link.should(be.visible).should(be.clickable)
        return self


    def should_link_to_rage_mp(self):
        self.rage_mp_link.should(be.visible).should(be.clickable)
        return self


    """Проверка отображения заголовка 'Как начать играть' и названий всех вкладок в разделе"""
    def should_display_heading_and_name_tabs_in_how_start_game(self, *tabs):
        self.start_game_title.should(have.text("КАК НАЧАТЬ"))
        self.start_game_title.should(have.text("ИГРАТЬ"))
        for tab in tabs:
            self.start_game_tabs.element_by(have.text(tab)).should(be.visible)
        return self


    """Проверка отображения подзаголовков, описания и названий ссылок во вкладках"""
    def should_display_subtitle_and_description_pay_game_tab(self):
        self.subtitle_tabs.should(be.visible)
        self.description_tabs.should(be.visible)
        self.subtitle_tabs.should(have.text("Купите и установите лицензионную GTA 5"))
        self.description_tabs.should(have.text("Лицензионную GTA 5 можно купить в Steam, Epic Games или на других площадках цифровой дистрибуции"))
        self.steam_link.should(be.visible).should(have.text("STEAM")).should(be.clickable)
        self.epic_games_link.should(be.visible).should(have.text("EPIC GAMES")).should(be.clickable)
        self.rockstar_games_link.should(be.visible).should(have.text("ROCKSTAR GAMES")).should(be.clickable)
        return self


    def should_display_subtitle_and_description_launcher_installation_tab(self):
        self.subtitle_tabs.should(be.visible)
        self.description_tabs.should(be.visible)
        self.subtitle_tabs.should(have.text("Установите Rage Multiplayer"))
        self.description_tabs.should(have.text("Загрузите официальный лаунчер Rage. По окончании загрузки произведите установку лаунчера в место, не включающее файлы игры"))
        self.rage_mp_link.should(be.visible).should(have.text("СКАЧАТЬ ЛАУНЧЕР")).should(be.clickable)
        return self


    def should_display_subtitle_and_description_connection_tab(self):
        self.subtitle_tabs.should(be.visible)
        self.description_tabs.should(be.visible)
        self.subtitle_tabs.should(have.text("Запустите лаунчер и подключайтесь"))
        self.description_tabs.should(have.text("Запустите лаунчер и в открывшемся окне введите IP адрес выбранного сервера"))
        self.copy_ip.element_by(have.text("СКОПИРОВАТЬ IP")).should(be.clickable)
        return self