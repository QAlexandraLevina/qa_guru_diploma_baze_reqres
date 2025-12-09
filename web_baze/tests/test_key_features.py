import pytest
from web_baze.pages.key_features import KeyFeatures
import allure


key_features = KeyFeatures()

@pytest.mark.web
@allure.title("Скролл до блока 'Ключевые особенности' и проверка блока")
def test_key_features(setup_browser, close_fortune_wheel):
    browser = setup_browser

    browser.open("/")

    with allure.step("Скролл до раздела 'Ключевые особенности'"):
        browser.execute_script("arguments[0].scrollIntoView();", key_features.key_feature_title.locate())


    with allure.step("Проверка отображения заголовка раздела 'Ключевые особенности' и прогресс-баров под вкладками"):
        key_features.should_display_title_section().should_display_key_feature_progress_bar()


    with allure.step("Проверка отображения и кликабельности вкладок в разделе 'Ключевые особенности'"):
        key_features.should_display_key_feature_tabs()


    with allure.step("Клик по вкладке 'ИССЛЕДОВАНИЕ МИРА', проверка отображения крупного превью и миниатюр"):
        key_features.click_exploring_the_world_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()


    with allure.step("Клик по вкладке 'ПРОКАЧКА ПЕРСОНАЖА', проверка отображения крупного превью и миниатюр"):
        key_features.click_leveling_up_character_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()


    with allure.step("Клик по вкладке 'PVP ИВЕНТЫ С МАТЧМЕЙКИНГОМ', проверка отображения крупного превью и миниатюр"):
        key_features.click_pvp_events_with_matchmaking_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()


    with allure.step("Клик по вкладке 'СПЕЦИАЛИЗАЦИИ', проверка отображения крупного превью и миниатюр"):
        key_features.click_specializations_tab().should_display_key_feature_large_preview().should_display_key_feature_thumbnails()