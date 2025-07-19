import logging
import time

import pyautogui

from logger.logger import Logger



class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info(f"Handle File Dialog for uploading file")
        time.sleep(3) # timeout after opening File Dialog

        logging.debug(f"Write '{file_path}' to search File Dialog field")
        pyautogui.typewrite(file_path)
        logging.debug("Press enter")
        pyautogui.hotkey("enter")

        time.sleep(3) # timeout befor closing File Dialog