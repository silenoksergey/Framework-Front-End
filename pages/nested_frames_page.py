from browser.browser import Browser
from elements.label import Label
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='frame1']"

    PARENT_FRAME = "//*[@id='frame1']"
    CHILD_FRAME = "//*[contains(@srcdoc, 'Child Iframe')]"
    BODY_FRAME = "//body"

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Nested Frames Page -> Parent Frame"
        )

        self.parent_frame = Label(
            self.browser,
            self.PARENT_FRAME,
            description="Nested Frames Page -> Parent Frame"
        )

        self.child_frame = Label(
            self.browser,
            self.CHILD_FRAME,
            description="Nested Frames Page -> Child Frame"
        )

        self.body_frame = Label(
            self.browser,
            self.BODY_FRAME,
            description="Nested Frames Page -> Body Frame"
        )

    def get_parent_frame_text(self) -> str:
        self.browser.switch_to_frame(self.parent_frame)
        body_element_text = self.body_frame.get_text()
        self.browser.switch_to_default_content()
        return body_element_text

    def get_child_frame_text(self) -> str:
        self.browser.switch_to_frame(self.parent_frame)
        self.browser.switch_to_frame(self.child_frame)
        body_element_text = self.body_frame.get_text()
        self.browser.switch_to_default_content()
        return body_element_text


