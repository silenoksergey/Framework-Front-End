from browser.browser import Browser
from elements.label import Label
from .base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'example')]//p"
    SUCCESS_MESSAGE = "//*[contains(@class, 'example')]//p"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Basic Auth Page"

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC,
                                   description="Basic Auth Page -> success message")

        self.success_message = Label(self.browser, self.SUCCESS_MESSAGE,
                                     description="Basic Auth Page -> success message")


    def get_success_message(self) -> str:
        return self.success_message.get_text()
