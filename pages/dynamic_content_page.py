from collections import Counter

from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='flash-messages']"
    DYNAMIC_CONTENT_PAGE_URL = "https://the-internet.herokuapp.com/dynamic_content"
    AVATARS = "//img[contains(@src, 'Avatar-{}')]"

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

    def get_avatar(self) -> WebElement:
        return self.avatars.__iter__()

    def get_all_avatars(self) -> list:
        avatars = []
        index = 1
        while True:
            try:
                avatar = self.get_avatar()
                if not avatar.is_exist():
                    break

                avatars.append(avatar)
                index += 1

            except StopIteration:
                break
        return avatars

    def verify_avatars(self, max_count=2):
        avatars = self.get_all_avatars()
        counter = Counter(avatars)
        return any(count >= max_count for count in counter.values())

    def find_duplicate_avatars(self, max_attempts=10):
        has_duplicates = False
        attempt = 0
        while not has_duplicates and attempt < max_attempts:
            attempt += 1
            has_duplicates = self.verify_avatars()
            self.browser.driver.refresh()
            Logger.info(f"Attempt {attempt}/{max_attempts}")

        assert has_duplicates is True, f"Повторяющихся аватаров не найдено"





