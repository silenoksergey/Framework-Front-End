from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'scroll')]"
    PARAGRAPHS = "(//*[contains(@class, 'jscroll-added')])[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Infinite Scroll Page -> Unique Element"
        )

        self.paragraphs = MultiWebElement(
            self.browser,
            self.PARAGRAPHS,
            description="Infinite Scroll Page -> Paragraphs"
        )

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_paragraphs_count(self) -> int:
        count = 0
        for element in self.paragraphs:
            count += 1

        Logger.info(f"Найдено элементов с классом 'jscroll-added': {count}")
        return count
