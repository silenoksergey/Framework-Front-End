from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class HandlersPage(BasePage):
    NEW_WINDOW_TITLE = "New Window"
    NEW_WINDOW_PAGE_TEXT = "New Window"
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'example')]//*[contains(@target, '_blank')]"
    NEW_WINDOW_TEXT_LOC = "//*[contains(@class, 'example')]//h3"
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

        self.new_window_page_text = Label(
            self.browser,
            self.NEW_WINDOW_TEXT_LOC,
            description="Handlers Page -> New Window Page Text"
        )

    def click_new_window_link(self) -> None:
        self.link_button.click()

    def get_new_window_text(self) -> str:
        return self.new_window_page_text.get_text()
