from enum import StrEnum

from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class ClickMode(StrEnum):
    NATIVE = "click"
    JS = "js_click"


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

    @staticmethod
    def _click_with_mode(button: Button, mode: ClickMode = ClickMode.NATIVE) -> None:
        if mode is ClickMode.NATIVE:
            button.click()
        elif mode is ClickMode.JS:
            button.js_click()

    def click_js_alert_button(self, mode: ClickMode = ClickMode.NATIVE) -> None:
        self._click_with_mode(self.js_alert_button, mode)

    def click_js_confirm_button(self, mode: ClickMode = ClickMode.NATIVE) -> None:
        self._click_with_mode(self.js_confirm_button, mode)

    def click_js_prompt_button(self, mode: ClickMode = ClickMode.NATIVE) -> None:
        self._click_with_mode(self.js_prompt_button, mode)

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
