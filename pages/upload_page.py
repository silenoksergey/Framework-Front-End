from browser.browser import Browser
from elements.button import Button
from elements.input import Input
from elements.label import Label
from pages.base_page import BasePage


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "file-upload"
    SELECT_FILE_BUTTON = "file-upload"
    UPLOAD_SUBMIT_BUTTON = "file-submit"
    SUCCESSFUL_MESSAGE = "//*[contains(@class, 'example')]//h3"
    UPLOAD_FILE_NAME = "uploaded-files"
    UPLOAD_AREA = "drag-drop-upload"
    UPLOAD_AREA_FILE_DISPLAY = "//*[@id='drag-drop-upload']//*[contains(@class, 'dz-filename')]//span"
    UPLOAD_SUCCESS_MARK = "//*[@id='drag-drop-upload']//*[contains(@class, 'dz-success-mark')]//span"

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

        self.upload_area = Button(
            self.browser,
            self.UPLOAD_AREA,
            description="Upload Page -> Upload Area Button"
        )

        self.upload_area_file_display = Label(
            self.browser,
            self.UPLOAD_AREA_FILE_DISPLAY,
            description="Upload Page -> Upload Area File Display"
        )

        self.upload_success_mark = Label(
            self.browser,
            self.UPLOAD_SUCCESS_MARK,
            description="Upload Page -> Upload Success Mark"
        )

    def upload_image(self, image_path) -> None:
        self.select_file.send_keys(image_path)

    def get_upload_file_name(self) -> str:
        full_path = self.select_file.get_attribute("value")
        return full_path.split('\\')[-1]
