import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory


@pytest.fixture
def browser():
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    yield browser
    browser.quit()