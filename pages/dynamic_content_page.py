from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "flash-messages"
    AVATARS = "(//*[contains(@class, 'large-2') and contains(@class, 'columns')]//img)[{}]"

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

    def get_avatars_sources(self) -> list:
        avatars_sources = []
        for avatar in self.avatars:
            avatars_sources.append(avatar.get_attribute('src'))
        return avatars_sources
