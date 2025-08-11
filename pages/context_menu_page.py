from browser.browser import Browser
from pages.base_page import BasePage
from elements.button import Button


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='hot-spot']"
    CONTEXT_MENU_AREA = "hot-spot"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Context Menu Page"

        self.unique_element = Button(self.browser, self.UNIQUE_ELEMENT_LOC,
                                     description="Context Menu Page -> Button Context Menu Area")
        self.context_menu_area = Button(self.browser, self.UNIQUE_ELEMENT_LOC,
                                        description="Context Menu Page -> Button Context Menu Area")

    def right_click_context_menu_area(self) -> None:
        self.context_menu_area.right_click()

    def get_context_menu_area_text(self) -> str:
        return self.context_menu_area.get_text()

    def get_alert_text(self) -> str:
        return self.browser.get_alert_text()

    def accept_alert(self) -> None:
        self.browser.accept_alert()

    def wait_for_alert_closed(self) -> None:
        self.browser.wait_alert_closed()

    def handle_context_menu_alert(self) -> str:
        self.right_click_context_menu_area()
        alert_text = self.get_alert_text()
        self.accept_alert()
        return alert_text
