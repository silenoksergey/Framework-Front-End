from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='flash-messages']"
    DYNAMIC_CONTENT_PAGE_URL = "https://the-internet.herokuapp.com/dynamic_content"
    AVATARS = "(//*[contains(@class, 'large-2 columns')]//img)[{}]"
    MAX_DUPLICATE_SEARCH_ATTEMPTS = 10

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Dynamic Content Page -> Unique Element"
        )

        self.avatars = MultiWebElement(
            self.browser,
            self.AVATARS,
            description="Dynamic Content Page -> Avatars"
        )

    def open(self) -> None:
        self.browser.get(self.DYNAMIC_CONTENT_PAGE_URL)

    def get_avatars_sources(self) -> list:
        avatars_sources = []
        for avatar in self.avatars:
            avatars_sources.append(avatar.get_attribute('src'))
        return avatars_sources

    def refresh_page(self) -> None:
        self.browser.driver.refresh()
        self.wait_for_open()
        return False







