from pathlib import Path
from logger.logger import Logger
from pywinauto import Desktop, timings


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file (pywinauto)")
        path = str(Path(file_path).resolve())
        if not Path(path).exists():
            raise FileNotFoundError(f"File not found: {path}")

        timings.Timings.window_find_timeout = 8.0
        timings.Timings.after_clickinput_wait = 0.2

        dlg = Desktop(backend="win32").window(class_name="#32770", active_only=True)
        dlg.wait("exists enabled visible ready", timeout=8)
        dlg.set_focus()

        edit = dlg.child_window(class_name="Edit")
        edit.wait("exists enabled visible ready", timeout=2)
        edit.set_edit_text(path)

        open_btn = dlg.child_window(title_re=r"^(Open|Открыть)$", class_name="Button")
        if open_btn.exists(timeout=1.0):
            open_btn.click_input()
        else:
            dlg.type_keys("{ENTER}")
