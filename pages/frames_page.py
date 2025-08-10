from browser.browser import Browser
from elements.label import Label
from pages.base_page import BasePage


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "frame2"
    FIRST_FRAME = "frame1"
    SECOND_FRAME = "frame2"
    BODY_FRAME = "//body"

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Frame Page -> First Frame")

        self.first_frame = Label(
            self.browser,
            self.FIRST_FRAME,
            description="Frame Page -> First Frame")

        self.second_frame = Label(
            self.browser,
            self.SECOND_FRAME,
            description="Frame Page -> Second Frame")

        self.body_frame = Label(
            self.browser,
            self.BODY_FRAME,
            description="Frame Page -> Body Frame")



    def get_frame_text(self, frame) -> str:
        self.browser.switch_to_frame(frame)
        body_element_text = self.body_frame.get_text()
        self.browser.switch_to_default_content()
        return body_element_text
