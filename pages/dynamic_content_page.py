import time
from collections import Counter

from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
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

    def check_duplicates_avatars(self, max_attempts=MAX_DUPLICATE_SEARCH_ATTEMPTS) -> bool:
        for i in range(max_attempts):
            avatars_list = []
            for avatar in self.avatars:
                avatar_src = avatar.get_attribute('src')
                if avatar_src in avatars_list:
                    return True
                avatars_list.append(avatar_src)
            if i < max_attempts - 1:
                self.browser.driver.refresh()
                self.wait_for_open()

        return False





