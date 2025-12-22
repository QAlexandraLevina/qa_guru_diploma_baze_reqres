import os
import time
import warnings
import pytest
from dotenv import load_dotenv
from selene import be
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from web_baze.data.users import UserData
from web_baze.pages.authorization_form import AuthorizationForm
from web_baze.utils import attachments

DEFAULT_BROWSER_VERSION = "128.0"

"""Настройка параметров для браузера"""
def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


"""Загрузка переменных сред из файла .env"""
@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


"""Получение информации о значении параметра browser из командной строки"""
@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION


    """Настройка драйвера"""
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)


    """Создание переменных, cсылающихся на секретные данные"""
    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')


    """Создание драйвера"""
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # """Драйвер для локального запуска тестов"""
    # options = Options()
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    """Передача драйвера в Selene"""
    browser.config.driver = driver


    """Настройка параметров браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 45
    browser.config.base_url = "https://bazerp.com"


    yield browser


    """Добавление аттачей после теста"""
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_html(browser)
    attachments.add_video(browser)


    """Закрытие браузера"""
    browser.quit()


"""Авторизация для проверки функционала у авторизованного пользователя"""
@pytest.fixture
def user_authorized():
    return UserData(
        os.getenv('TEST_USER_EMAIL_BAZE_AUTHORIZATION'),
        os.getenv('TEST_USER_PASSWORD_BAZE_AUTHORIZATION')
    )


@pytest.fixture(scope='function')
def authenticated_user(setup_browser, user_authorized):
    browser.open("/")

    """Закрытие модального окна 'Колесо фортуны'"""
    try:
        time.sleep(2)
        browser.element(".about-lucky-circle__lucky-circle").should(be.visible)
        browser.element(".about-lucky-circle__close").click()
    except:
        pass

    authenticated_form = AuthorizationForm()
    authenticated_form.authorization_user(user_authorized)

    authenticated_form.should_authorized_profile()

    yield user_authorized


@pytest.fixture(scope='function')
def open_refill_page(authenticated_user):
    browser.open("/top-up")

    """Закрытие модального окна 'Колесо фортуны'"""
    try:
        time.sleep(2)
        browser.element(".about-lucky-circle__lucky-circle").should(be.visible)
        browser.element(".about-lucky-circle__close").click()
    except:
        pass

    yield


@pytest.fixture(scope='function')
def open_promocode_page(authenticated_user):
    browser.open("/activate-promo")

    """Закрытие модального окна 'Колесо фортуны'"""
    try:
        time.sleep(2)
        browser.element(".about-lucky-circle__lucky-circle").should(be.visible)
        browser.element(".about-lucky-circle__close").click()
    except:
        pass

    yield

"""Игнорирование Warning(ов)"""
@pytest.fixture(scope='session', autouse=True)
def suppress_warnings():
    warnings.filterwarnings("ignore", message="Embedding username and password")
    warnings.filterwarnings("ignore", category=PendingDeprecationWarning)