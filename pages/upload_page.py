from browser.browser import Browser
from elements.button import Button
from elements.input import Input
from elements.label import Label
from pages.base_page import BasePage


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='file-upload']"
    IMAGE_FILE_PATH = "C:/Users/skill/PycharmProjects/Framework-Front-End/tests/test_files/images/bober.png"
    UPLOAD_PAGE_URL = "https://the-internet.herokuapp.com/upload"
    SELECT_FILE_BUTTON = "//*[@id='file-upload']"
    UPLOAD_SUBMIT_BUTTON = "//*[@id='file-submit']"
    SUCCESSFUL_MESSAGE = "//*[contains(@class, 'example')]//h3"
    UPLOAD_FILE_NAME = "//*[@id='uploaded-files']"

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = Input(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Upload Page -> Select File Input"
        )

        self.select_file = Input(
            self.browser,
            self.SELECT_FILE_BUTTON,
            description="Upload Page -> Select File Input"
        )

        self.upload_submit_button = Button(
            self.browser,
            self.UPLOAD_SUBMIT_BUTTON,
            description="Upload Page -> Upload Submit Button"
        )

        self.successful_message = Label(
            self.browser,
            self.SUCCESSFUL_MESSAGE,
            description="Upload Page -> Successful Upload Message"
        )

        self.upload_file_name = Label(
            self.browser,
            self.UPLOAD_FILE_NAME,
            description="Upload Page -> Upload File Name Label"
        )

    def open(self) -> None:
        self.browser.get(self.UPLOAD_PAGE_URL)

    def upload_image(self, image_path=IMAGE_FILE_PATH) -> None:
        self.select_file.send_keys(image_path)

    def get_upload_file_name(self) -> str:
        full_path = self.select_file.get_attribute("value")
        return full_path.split('\\')[-1]
