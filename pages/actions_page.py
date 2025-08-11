import random
from selenium.webdriver import ActionChains
from browser.browser import Browser
from elements.input import Input
from elements.label import Label
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class ActionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@type, 'range')]"
    SLIDER = "//*[contains(@type, 'range')]"
    DISPLAYED_VALUE_SLIDER = "range"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Actions Page"

        self.unique_element = Input(self.browser, self.SLIDER,
                                    description="Actions Page -> Slider Button")

        self.slider_input = Input(self.browser, self.SLIDER,
                                  description="Actions Page -> Slider Button")
        self.displayed_value_slider = Label(self.browser, self.DISPLAYED_VALUE_SLIDER,
                                            description="Action Page -> Slider Displayed Value")

    def get_slider_value(self):
        Logger.info(f"{self} get slider value")
        return float(self.slider_input.get_attribute("value"))

    def get_displayed_value(self):
        Logger.info(f"{self} get displayed slider value")
        return float(self.displayed_value_slider.get_text())

    def get_slider_min_value(self) -> float:
        Logger.info(f"{self} get slider min value")
        return float(self.slider_input.get_attribute("min"))

    def get_slider_max_value(self) -> float:
        Logger.info(f"{self} get slider max value")
        return float(self.slider_input.get_attribute("max"))

    def set_random_slider_value(self) -> None:
        min_value = self.get_slider_min_value()
        max_value = self.get_slider_max_value()
        step = float(self.slider_input.get_attribute("step") or 1)
        current_value = float(self.slider_input.get_attribute("value"))

        total_steps = int(round((max_value - min_value) / step))
        if total_steps <= 1:
            msg = f"{self}: No valid non-boundary values for slider"
            Logger.error(msg)
            raise ValueError(msg)

        possible_steps = [i for i in range(1, total_steps)]
        random_step = random.choice(possible_steps)
        random_value = min_value + random_step * step

        Logger.info(f"{self}: set value {random_value} (step {random_step})")
        action = ActionChains(self.browser.driver)
        self.slider_input.click()

        steps_to_min = int(round((current_value - min_value) / step))
        Logger.info(f"{self}: moving to min value ({steps_to_min} steps)")
        arrow_left_string = Keys.ARROW_LEFT * steps_to_min
        action.send_keys(arrow_left_string)
        action.perform()

        Logger.info(f"{self}: moving to target value ({random_step} steps)")
        right_left_string = Keys.ARROW_RIGHT * random_step
        action.send_keys(right_left_string)
        action.perform()
