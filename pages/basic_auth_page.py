from elements.label import Label
from logger.logger import Logger
from .base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'example')]"

    BASIC_AUTH_URL = "http://{}:{}@the-internet.herokuapp.com/basic_auth"
    BASIC_AUTH_LOGIN = "admin"
    BASIC_AUTH_PASSWORD = "admin"
    SUCCESS_MESSAGE = "//*[contains(@class, 'example')]//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Basic Auth Page"

        self.success_message = Label(self.browser, self.SUCCESS_MESSAGE,
                                     description="Basic Auth Page -> success message")

    def open(self) -> None:
        Logger.info(f"{self.name}: open")
        basic_auth_url = self.BASIC_AUTH_URL.format(self.BASIC_AUTH_LOGIN, self.BASIC_AUTH_PASSWORD)
        self.browser.get(basic_auth_url)

    def get_success_message(self) -> str:
        return self.success_message.get_text()
