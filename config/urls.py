import os
from enum import StrEnum

THE_INTERNET_BASE = os.getenv("THE_INTERNET_BASE", "https://the-internet.herokuapp.com")
DEMOQA_BASE = os.getenv("DEMOQA_BASE", "https://demoqa.com")


class InternetEP(StrEnum):
    UPLOAD = "upload"
    JAVASCRIPT_ALERTS = "javascript_alerts"
    CONTEXT_MENU = "context_menu"
    HOVERS = "hovers"
    WINDOWS = "windows"
    DYNAMIC_CONTENT = "dynamic_content"
    INFINITE_SCROLL = "infinite_scroll"
    BASIC_AUTH = "basic_auth"
    HORIZONTAL_SLIDER = "horizontal_slider"


class DemoqaEP(StrEnum):
    FRAMES = "frames"


def internet(path: str | InternetEP = "") -> str:
    p = path.value if isinstance(path, InternetEP) else str(path)
    return f"{THE_INTERNET_BASE}/{p.lstrip('/')}"


def internet_auth(path: str | InternetEP, username: str, password: str) -> str:
    p = path.value if isinstance(path, InternetEP) else str(path)
    base_no_scheme = THE_INTERNET_BASE.replace("https://", "").replace("http://", "")
    scheme = "https" if THE_INTERNET_BASE.startswith("https") else "http"
    return f"{scheme}://{username}:{password}@{base_no_scheme}/{p.lstrip('/')}"


def demoqa(path: str | DemoqaEP = "") -> str:
    p = path.value if isinstance(path, DemoqaEP) else str(path)
    return f"{DEMOQA_BASE}/{p.lstrip('/')}"
