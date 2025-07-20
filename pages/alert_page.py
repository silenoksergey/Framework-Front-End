from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from logger.logger import Logger
from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@onclick, 'jsAlert()')]"

    ALERT_PAGE_URL = "https://the-internet.herokuapp.com/javascript_alerts"
    JS_ALERT_BUTTON = "//*[contains(@onclick, 'jsAlert')]"
    JS_CONFIRM_BUTTON = "//*[contains(@onclick, 'jsConfirm')]"
    ALERT_RESULT_TEXT = "//*[@id='result']"
    JS_PROMPT_BUTTON = "//*[contains(@onclick, 'jsPrompt')]"



    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Alert Page"

        self.unique_element = Button(self.browser, self.UNIQUE_ELEMENT_LOC,
                                     description="Alert Page -> JS Alert Button")
        self.js_alert_button = Button(self.browser, self.JS_ALERT_BUTTON,
                                      description="Alert Page -> JS Alert Button")
        self.alert_result_text = Label(self.browser, self.ALERT_RESULT_TEXT,
                                       description="Alert Page -> Alert Result Text")
        self.js_confirm_button = Button(self.browser, self.JS_CONFIRM_BUTTON,
                                        description="Alert Page -> JS Confirm Button")
        self.js_prompt_button = Button(self.browser, self.JS_PROMPT_BUTTON,
                                        description="Alert Page -> JS Prompt Button")


    def open(self) -> None:
        Logger.info(f"{self.page_name}: open")
        self.browser.get(self.ALERT_PAGE_URL)
        self.wait_for_open()