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

    def verify_new_window_content(self) -> None:
        text_page = self.new_window_page_text.get_text()
        assert text_page == self.NEW_WINDOW_PAGE_TEXT,\
            f"Ожидался текст '{self.NEW_WINDOW_PAGE_TEXT}', получен '{text_page}'"

        title_window = self.browser.get_title()
        assert title_window == self.NEW_WINDOW_TITLE,\
            f"Ожидалось название текущей вкладки: '{self.NEW_WINDOW_TITLE}', получено: '{title_window}'"

    def get_last_window_handle(self) -> str:
        return self.browser.get_last_window_handle()

    def switch_to_window_by_handle(self, handle: str) -> None:
        self.browser.switch_to_window_by_handle(handle)

    def close_current_window(self) -> None:
        self.browser.close()

    def test_single_new_window(self) -> None:
        self.click_new_window_link()
        self.browser.switch_to_window(self.NEW_WINDOW_TITLE)
        self.verify_new_window_content()
        self.browser.switch_to_default_window()