from enum import StrEnum

from browser.browser import Browser
from elements.button import Button
from pages.base_page import BasePage

class WindowTitles(StrEnum):
    NEW_WINDOW = "New Window"





class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'example')]//*[contains(@target, '_blank')]"
    HANDLERS_PAGE_URL = "https://the-internet.herokuapp.com/windows"
    NEW_WINDOW_TITLE = WindowTitles.NEW_WINDOW

    LINK_BUTTON = "//*[contains(@class, 'example')]//*[contains(@target, '_blank')]"


    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = Button(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Handlers Page -> Link Button"
        )

        self.link_button = Button(
            self.browser,
            self.LINK_BUTTON,
            description="Handlers Page -> Link Button"
        )

    def open(self) -> None:
        self.browser.get(self.HANDLERS_PAGE_URL)

