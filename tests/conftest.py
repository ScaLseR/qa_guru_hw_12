"""фикстуры используемые для тестирования формы
https://demoqa.com/automation-practice-form"""
# import pytest
# from selene.support.shared import browser


# @pytest.fixture(scope='function', autouse=True)
# def browser_setup():
#     """Фикстура настройки браузера"""
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     browser.config.timeout = 2.0
#     browser.config.base_url = 'https://demoqa.com'

# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selene import Browser, Config
#
# from utils import attach


# @pytest.fixture(scope='function', autouse=True)
# def browser_setup():
#     """Фикстура настройки браузера"""
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     browser.config.timeout = 2.0
#     # browser.config.base_url = 'https://demoqa.com'
#
#     yield browser
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#
#     browser.quit()

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
