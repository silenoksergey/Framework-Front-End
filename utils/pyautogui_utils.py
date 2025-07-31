import logging
import os
import time

import pyautogui

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info(f"Handle File Dialog for uploading file")
        time.sleep(3)  # timeout after opening File Dialog

        directory = os.path.dirname(file_path)
        filename = os.path.basename(file_path)

        Logger.info(f"Directory: {directory}")
        Logger.info(f"Filename: {filename}")

        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        for i in range(5):
            Logger.debug("Press tab")
            pyautogui.hotkey("tab")
        time.sleep(1)

        Logger.debug("Press enter")
        pyautogui.press('enter')
        time.sleep(0.5)

        logging.debug(f"Writing directory: '{directory}'")
        pyautogui.typewrite(directory, interval=0.1)
        time.sleep(0.5)

        Logger.debug("Press enter")
        pyautogui.press('enter')
        time.sleep(2)

        for i in range(6):
            Logger.debug("Press tab")
            pyautogui.hotkey("tab")
        time.sleep(1)

        logging.debug(f"Writing filename: '{filename}'")
        pyautogui.typewrite(filename, interval=0.1)
        time.sleep(0.5)

        Logger.debug("Press enter")

        pyautogui.press('enter')

        time.sleep(3)  # timeout befor closing File Dialog
