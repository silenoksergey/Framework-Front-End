import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName


@pytest.fixture
def browser():
    driver = BrowserFactory.get_driver(AvailableDriverName.CHROME, ["--headless=new", "--window-size=1920,1080", "--no-sandbox"])
    browser = Browser(driver)
    yield browser
    browser.quit()
