from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from logger.logger import Logger
from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@onclick, 'jsAlert()')]"
    JS_ALERT_BUTTON = "//*[contains(@onclick, 'jsAlert')]"
    JS_CONFIRM_BUTTON = "//*[contains(@onclick, 'jsConfirm')]"
    ALERT_RESULT_TEXT = "result"
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

    def click_js_alert_button(self, use_js: bool = False) -> None:
        click_method = "js_click" if use_js else "click"
        getattr(self.js_alert_button, click_method)()

    def click_js_confirm_button(self, use_js: bool = False) -> None:
        click_method = "js_click" if use_js else "click"
        getattr(self.js_confirm_button, click_method)()

    def click_js_prompt_button(self, use_js: bool = False) -> None:
        click_method = "js_click" if use_js else "click"
        getattr(self.js_prompt_button, click_method)()

    def get_alert_result_text(self) -> str:
        return self.alert_result_text.get_text()

    def get_alert_text(self) -> str:
        return self.browser.get_alert_text()

    def accept_alert(self) -> None:
        self.browser.accept_alert()

    def send_keys_to_alert(self, text: str) -> None:
        self.browser.send_keys_alert(text)

    def wait_for_alert_closed(self) -> None:
        self.browser.wait_alert_closed()

    def handle_js_alert(self, use_js: bool = False) -> str:
        self.click_js_alert_button(use_js)
        alert_text = self.get_alert_text()
        self.accept_alert()
        return alert_text

    def handle_js_confirm(self, use_js: bool = False) -> str:
        self.click_js_confirm_button(use_js)
        alert_text = self.get_alert_text()
        self.accept_alert()
        return alert_text

    def handle_js_prompt(self, use_js: bool = False, text: str = None) -> str:
        self.click_js_prompt_button(use_js)
        alert_text = self.get_alert_text()
        if text:
            self.send_keys_to_alert(text)
        self.accept_alert()
        return alert_text