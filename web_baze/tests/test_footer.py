import allure
import pytest
from web_baze.pages.footer import Footer
from web_baze.utils.modal_helper import close_fortune_modal


@pytest.mark.web
@allure.title("Скролл до блока футера и проверка футера")
def test_footer(setup_browser):
    browser = setup_browser

    browser.open("/")

    close_fortune_modal()

    footer = Footer()

    with allure.step("Скролл до футера"):
        browser.execute_script("arguments[0].scrollIntoView();", footer.bottom_footer_info.locate())


    with allure.step("Проверка отображения названий ссылок"):
       footer.should_display_correct_names_links()


    with allure.step("Проверка отображения текстовой части футера"):
       footer.should_display_texts_footer()


    with allure.step("Проверка отображения и кликабельности ссылки на VKONTAKTE"):
       footer.should_link_to_vkontakte()


    with allure.step("Проверка отображения и кликабельности ссылки на TELEGRAM"):
       footer.should_link_to_telegram()


    with allure.step("Проверка отображения и кликабельности ссылки в DISCORD"):
       footer.should_link_to_discord()


    with allure.step("Проверка отображения и кликабельности ссылки на YOUTUBE"):
       footer.should_link_to_youtube()


    with allure.step("Проверка отображения и кликабельности ссылки на ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ"):
       footer.should_link_to_user_agreement_page()


    with allure.step("Проверка отображения и кликабельности ссылки на ПОЛИТИКУ КОНФИДЕНЦИЛЬНОСТИ"):
       footer.should_link_to_privacy_policy_page()