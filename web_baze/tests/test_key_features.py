import time
import pytest
from selene import be
from web_baze.pages.key_features import KeyFeatures
import allure


key_features = KeyFeatures()

@pytest.mark.web
@allure.title("Скролл до блока 'Ключевые особенности' и проверка блока")
def test_key_features(setup_browser):
    browser = setup_browser

    browser.open("/")

    """Закрытие модального окна 'Колесо фортуны'"""
    try:
        time.sleep(2)
        browser.element(".about-lucky-circle__lucky-circle").should(be.visible)
        browser.element(".about-lucky-circle__close").click()
    except:
        pass


    with allure.step("Скролл до раздела 'Ключевые особенности'"):
        browser.execute_script("arguments[0].scrollIntoView();", key_features.key_feature_title.locate())


    with allure.step("Проверка отображения заголовка раздела 'Ключевые особенности' и прогресс-баров под вкладками"):
        key_features.should_display_title_section().should_display_key_feature_progress_bar()


    with allure.step("Проверка отображения и кликабельности вкладок в разделе 'Ключевые особенности'"):
        key_features.should_display_key_feature_tabs()


    with allure.step("Клик по вкладке 'ИССЛЕДОВАНИЕ МИРА', проверка отображения крупного превью и миниатюр"):
        key_features.click_interfaces_and_server_mechanics_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()


    with allure.step("Клик по вкладке 'ПРОКАЧКА ПЕРСОНАЖА', проверка отображения крупного превью и миниатюр"):
        key_features.click_3d_and_graphics_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()


    with allure.step("Клик по вкладке 'PVP ИВЕНТЫ С МАТЧМЕЙКИНГОМ', проверка отображения крупного превью и миниатюр"):
        key_features.click_interactions_with_other_players_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()


    with allure.step("Клик по вкладке 'СПЕЦИАЛИЗАЦИИ', проверка отображения крупного превью и миниатюр"):
        key_features.click_personage_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()