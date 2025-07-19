import pytest
from browser.browser import Browser
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    browser = Browser(driver)
    yield browser
    driver.quit()