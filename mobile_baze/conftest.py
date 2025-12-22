import os
import sys
import allure
import pytest
from dotenv import load_dotenv
from selene import browser, be
from appium import webdriver
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
from mobile_baze.config import context_manager
from attachments import add_screenshot, add_xml, add_video
from appium.webdriver.common.appiumby import AppiumBy


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local_emulator",
        help="Выбор окружения для запуска теста: local emulator (локальный эмулятор) или bstack (BrowserStack)"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"
    load_dotenv(dotenv_path=env_file_path)
    load_dotenv('.env.credentials')


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = context_manager(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = float(os.getenv('timeout', '15.0'))

    session_id = browser.driver.session_id

    import time
    time.sleep(3)

    try:
        browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")).should(be.visible).click()
        browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")).should(be.visible).click()
        time.sleep(1)
    except:
        pass

    yield

    add_screenshot(browser)
    add_xml(browser)

    with allure.step("Закрытие браузера"):
        browser.quit()

    if context == 'bstack':
        add_video(session_id, os.getenv('BS_USER_NAME'), os.getenv('BS_ACCESS_KEY'))