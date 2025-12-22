import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from mobile_baze.generators_name_guest import generate_guest_name


@pytest.mark.mobile
@allure.title("Проверка навигации по главному меню приложения")
def test_starting_menu(mobile_management):
        with allure.step("Тап на кнопку 'Гость' на странице авторизации"):
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/btn_guest")).should(be.visible).click()

        with allure.step("Ввод имени 'Гостя' на странице авторизации"):
            input_field = browser.element((AppiumBy.ID, "com.bazemobile.main:id/editTextText"))
            input_field.type(generate_guest_name())

        with allure.step("Тап на кнопку 'Подтвердить' на странице авторизации"):
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/button15")).should(be.visible).click()

        try:
            with allure.step("Тап на кнопку 'Нет' для отказа от фоновой загрузки"):
                browser.element((AppiumBy.ID, "com.bazemobile.main:id/button2")).should(be.visible).click()
        except:
            pass

        with allure.step("Тап на кнопку технической поддержки"):
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/imageButton13")).should(be.visible).click()

        with allure.step("Тап по первому вопросу в разделе 'Помощь'"):
            browser.element((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.bazemobile.main:id/faq_item_caption' and @text='Как придумать никнейм?']")).click()

        with allure.step("Тап на кнопку возврата в 'Главное меню'"):
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/button2")).should(be.visible).click()
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/textView69")).should(have.text("VICTORIA #1"))

        with allure.step("Тап на шестерёнку для перехода в настройки"):
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/imageButton11")).should(be.visible).click()

        with allure.step("Перемещение переключателей управления в игре в активное положение"):
            browser.element((AppiumBy.ID, 'com.bazemobile.main:id/sticky_switch1')).should(be.visible).click()
            browser.element((AppiumBy.ID, 'com.bazemobile.main:id/sticky_switch2')).should(be.visible).click()

        with allure.step("Переход на вкладку 'Графика'"):
            browser.element((AppiumBy.ID, 'com.bazemobile.main:id/menu_2')).should(be.visible).click()

        with allure.step("Тап на 'Оптимальное' качество графики"):
            browser.element((AppiumBy.ID, 'com.bazemobile.main:id/imageView197')).should(be.visible).click()

        with allure.step("Тап на кнопку возврата в 'Главное меню'"):
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/button2")).should(be.visible).click()
            browser.element((AppiumBy.ID, "com.bazemobile.main:id/textView69")).should(have.text("VICTORIA #1"))