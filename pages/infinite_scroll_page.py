from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'scroll')]"
    INFINITE_SCROLL_PAGE_URL = "https://the-internet.herokuapp.com/infinite_scroll"
    PARAGRAPHS = "(//*[contains(@class, 'jscroll-added')])[{}]"
    MAX_VIEW_PARAGRAPHS = 27

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

    def open(self) -> None:
        self.browser.get(self.INFINITE_SCROLL_PAGE_URL)

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def count_paragraphs(self) -> int:
        count = 0
        for element in self.paragraphs:
            count += 1

        Logger.info(f"Найдено элементов с классом 'jscroll-added': {count}")
        return count

    def get_paragraphs_count(self) -> int:
        return self.count_paragraphs()

