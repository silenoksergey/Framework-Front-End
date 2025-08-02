from enum import StrEnum

from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class WindowTitles(StrEnum):
    NEW_WINDOW = "New Window"


class PageTexts(StrEnum):
    NEW_WINDOW_TEXT = "New Window"


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'example')]//*[contains(@target, '_blank')]"
    HANDLERS_PAGE_URL = "https://the-internet.herokuapp.com/windows"
    NEW_WINDOW_TITLE = WindowTitles.NEW_WINDOW
    NEW_WINDOW_TEXT_LOC = "//*[contains(@class, 'example')]//h3"
    LINK_BUTTON = "//*[contains(@class, 'example')]//*[contains(@target, '_blank')]"
    NEW_WINDOW_PAGE_TEXT = PageTexts.NEW_WINDOW_TEXT

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

        self.new_window_page_text = Label(
            self.browser,
            self.NEW_WINDOW_TEXT_LOC,
            description="Handlers Page -> New Window Page Text"
        )

    def open(self) -> None:
        self.browser.get(self.HANDLERS_PAGE_URL)

    def click_new_window_link(self) -> None:
        self.link_button.click()

    def get_new_window_text(self) -> str:
        return self.new_window_page_text.get_text()

    def get_last_window_handle(self) -> str:
        return self.browser.get_last_window_handle()

    def switch_to_window_by_handle(self, handle: str) -> None:
        self.browser.switch_to_window_by_handle(handle)

    def close_current_window(self) -> None:
        self.browser.close()

    def get_current_window_title(self) -> str:
        return self.browser.get_title()

    def open_new_window(self) -> None:
        self.click_new_window_link()
        self.browser.switch_to_window(self.NEW_WINDOW_TITLE)

    def return_to_main_window(self) -> None:
        self.browser.switch_to_default_window()
