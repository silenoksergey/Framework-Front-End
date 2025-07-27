from browser.browser import Browser
from elements.button import Button
from logger.logger import Logger
from pages.base_page import BasePage


class FramesMainPage(BasePage):
    ENSURE_MENU = "(//*[contains(@class, 'header-text')])[3]"
    NESTED_FRAMES_BUTTON = "//*[contains(@class, 'element-list collapse show')]//*[@id='item-3']"
    FRAMES_BUTTON = "//*[contains(@class, 'btn btn-light active')]"

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.ensure_menu = Button(
            self.browser,
            self.ENSURE_MENU,
            description="Frame Main Page -> Alerts, Frame & Windows Button"
        )

        self.nested_frames_button = Button(
            self.browser,
            self.NESTED_FRAMES_BUTTON,
            description="Frame Main Page -> Nested Frames Button"
        )

        self.frames_button = Button(
            self.browser,
            self.FRAMES_BUTTON,
            description="Frame Main Page -> Frames Button"
        )

    def is_menu_expanded(self) -> bool:
        return self.frames_button.is_exist()

    def click_ensure_menu(self) -> None:
        if self.is_menu_expanded():
            Logger.info(f"{self}: menu already expanded")
            return
        else:
            Logger.info(f"{self}: expanding menu")
            self.ensure_menu.click()
