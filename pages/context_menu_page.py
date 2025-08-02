from browser.browser import Browser
from pages.base_page import BasePage
from elements.button import Button
from logger.logger import Logger


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='hot-spot']"

    CONTEXT_MENU_URL = "https://the-internet.herokuapp.com/context_menu"
    CONTEXT_MENU_AREA = "//*[@id='hot-spot']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Context Menu Page"

        self.unique_element = Button(self.browser, self.UNIQUE_ELEMENT_LOC,
                                     description="Context Menu Page -> Button Context Menu Area")
        self.context_menu_area = Button(self.browser, self.UNIQUE_ELEMENT_LOC,
                                        description="Context Menu Page -> Button Context Menu Area")

    def open(self) -> None:
        Logger.info(f"{self.page_name}: open")
        self.browser.get(self.CONTEXT_MENU_URL)
        self.wait_for_open()