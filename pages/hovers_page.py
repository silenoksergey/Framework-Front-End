from selenium.webdriver import ActionChains

from browser.browser import Browser
from elements.button import Button
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'figure')]"
    HOVERS_PAGE_URL = "http://the-internet.herokuapp.com/hovers"
    USER_BLOCKS = "//*[contains(@class, 'figure')][{}]"
    USER_NAME = "//*[contains(@class, 'figure')][{}]//*[contains(@class, 'figcaption')]/h5"
    PROFILE_LINK = "//*[contains(@class, 'figure')][{}]//*[contains(@class, 'figcaption')]/a"

    def __init__(self, browser: Browser):
        super().__init__(browser)

        self.unique_element = Button(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Hovers Page -> User1 Block"
        )

        self.users_blocks = MultiWebElement(
            self.browser,
            self.USER_BLOCKS,
            description="Hovers Page -> Users Blocks"
        )

        self.users_name = MultiWebElement(
            self.browser,
            self.USER_NAME,
            description="Hovers Page -> Users Name"
        )

        self.profile_link = MultiWebElement(
            self.browser,
            self.PROFILE_LINK,
            description="Hovers Page -> Profile Links"
        )

    def open(self) -> None:
        self.browser.get(self.HOVERS_PAGE_URL)

    def hover_user(self, user_block) -> None:
        selenium_element = user_block.wait_for_presence()
        ActionChains(self.browser.driver).move_to_element(selenium_element).perform()

    def get_user_name(self, user_block) -> str:
        self.hover_user(user_block)
        user_name_element = self.users_name.__iter__()
        return user_name_element.get_text()

    def click_profile_link(self, user_block) -> None:
        self.hover_user(user_block)
        profile_link_element = self.profile_link.__iter__()
        profile_link_element.wait_for_clickable()
        profile_link_element.click()

    def process_all_users(self) -> None:
        user_count = 0

        while True:
            try:
                user_block = self.users_blocks.__iter__()
                user_count += 1

                user_name = self.get_user_name(user_block)
                assert user_name == f"name: user{user_count}"

                self.click_profile_link(user_block)

                assert f"users/{user_count}" in self.browser.driver.current_url, \
                    f"Не удалось перейти на профиль пользователя {user_name}"

                self.browser.driver.back()

            except StopIteration:
                break
