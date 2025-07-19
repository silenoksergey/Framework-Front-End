from pages.basic_auth_page import BasicAuthPage


def test_basic_auth_page(browser):
    basic_auth_page = BasicAuthPage(browser)
    basic_auth_page.open()
    basic_auth_page.get_success_message()
