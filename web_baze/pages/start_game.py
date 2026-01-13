from selene import browser, be, have


class StartGame:
    PAY_GAME_TEXT = "ПОКУПКА ИГРЫ"
    LAUNCHER_INSTALLATION_TEXT = "УСТАНОВКА ЛАУНЧЕРА"
    CONNECTION_TAB_TEXT = "ПОДКЛЮЧЕНИЕ"
    HOW_START_GAME_TEXT_1 = "КАК НАЧАТЬ"
    HOW_START_GAME_TEXT_2 = "ИГРАТЬ"
    SUBTITLE_PAY_GAME_TAB_TEXT = "Купите и установите лицензионную GTA 5"
    DESCRIPTION_PAY_GAME_TAB_TEXT = "Лицензионную GTA 5 можно купить в Steam, Epic Games или на других площадках цифровой дистрибуции"
    STEAM_LINK_TEXT = "STEAM"
    EPIC_GAMES_LINK_TEXT = "EPIC GAMES"
    ROCKSTAR_GAMES_LINK_TEXT = "ROCKSTAR GAMES"
    SUBTITLE_LAUNCHER_INSTALLATION_TAB_TEXT = "Установите Rage Multiplayer"
    DESCRIPTION_LAUNCHER_INSTALLATION_TAB_TEXT = "Загрузите официальный лаунчер Rage. По окончании загрузки произведите установку лаунчера в место, не включающее файлы игры"
    RAGE_MP_LINK_TEXT = "СКАЧАТЬ ЛАУНЧЕР"
    SUBTITLE_CONNECTION_TAB_TEXT = "Запустите лаунчер и подключайтесь"
    DESCRIPTION_CONNECTION_TAB_TEXT = "Запустите лаунчер и в открывшемся окне введите IP адрес выбранного сервера"
    COPY_IP_TEXT = "СКОПИРОВАТЬ IP"


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
        self.click_start_game_tabs(self.PAY_GAME_TEXT)
        return self


    def click_launcher_installation_tab(self):
        self.click_start_game_tabs(self.LAUNCHER_INSTALLATION_TEXT)
        return self


    def click_connection_tab(self):
        self.click_start_game_tabs(self.CONNECTION_TAB_TEXT)
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
        self.start_game_title.should(have.text(self.HOW_START_GAME_TEXT_1))
        self.start_game_title.should(have.text(self.HOW_START_GAME_TEXT_2))
        for tab in tabs:
            self.start_game_tabs.element_by(have.text(tab)).should(be.visible)
        return self


    """Проверка отображения подзаголовков, описания и названий ссылок во вкладках"""
    def should_display_subtitle_and_description_pay_game_tab(self):
        self.subtitle_tabs.should(be.visible)
        self.description_tabs.should(be.visible)
        self.subtitle_tabs.should(have.text(self.SUBTITLE_PAY_GAME_TAB_TEXT))
        self.description_tabs.should(have.text(self.DESCRIPTION_PAY_GAME_TAB_TEXT))
        self.steam_link.should(be.visible).should(have.text(self.STEAM_LINK_TEXT)).should(be.clickable)
        self.epic_games_link.should(be.visible).should(have.text(self.EPIC_GAMES_LINK_TEXT)).should(be.clickable)
        self.rockstar_games_link.should(be.visible).should(have.text(self.ROCKSTAR_GAMES_LINK_TEXT)).should(be.clickable)
        return self


    def should_display_subtitle_and_description_launcher_installation_tab(self):
        self.subtitle_tabs.should(be.visible)
        self.description_tabs.should(be.visible)
        self.subtitle_tabs.should(have.text(self.SUBTITLE_LAUNCHER_INSTALLATION_TAB_TEXT))
        self.description_tabs.should(have.text(self.DESCRIPTION_LAUNCHER_INSTALLATION_TAB_TEXT))
        self.rage_mp_link.should(be.visible).should(have.text(self.RAGE_MP_LINK_TEXT)).should(be.clickable)
        return self


    def should_display_subtitle_and_description_connection_tab(self):
        self.subtitle_tabs.should(be.visible)
        self.description_tabs.should(be.visible)
        self.subtitle_tabs.should(have.text(self.SUBTITLE_CONNECTION_TAB_TEXT))
        self.description_tabs.should(have.text(self.DESCRIPTION_CONNECTION_TAB_TEXT))
        self.copy_ip.element_by(have.text(self.COPY_IP_TEXT)).should(be.clickable)
        return self