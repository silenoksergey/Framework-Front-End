from selenium.webdriver import ActionChains
from browser.browser import Browser
from elements.button import Button
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'figure')]"
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

    def hover_user(self, user_block) -> None:
        selenium_element = user_block.wait_for_presence()
        ActionChains(self.browser.driver).move_to_element(selenium_element).perform()

    def get_user_name(self, user_block, user_name_element) -> str:
        self.hover_user(user_block)
        return user_name_element.get_text()

    def click_profile_link(self, user_block, profile_link_element) -> None:
        self.hover_user(user_block)
        profile_link_element.wait_for_clickable()
        profile_link_element.click()

    def get_current_url(self) -> str:
        return self.browser.driver.current_url

    def get_all_users_data(self) -> list:
        users_data = []

        for user_block, user_name_el, profile_link_el in zip(self.users_blocks, self.users_name, self.profile_link):
            self.hover_user(user_block)
            user_name = self.get_user_name(user_block, user_name_el)
            users_data.append({
                "block": user_block,
                "name": user_name,
                "profile_link": profile_link_el
            })

        return users_data
