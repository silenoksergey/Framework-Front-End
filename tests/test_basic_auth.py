from pages.actions_page import ActionsPage
from pages.alert_page import AlertPage
from pages.basic_auth_page import BasicAuthPage
from pages.context_menu_page import ContextMenuPage
from pages.handlers_page import HandlersPage
from pages.hovers_page import HoversPage
from utils.random_data import random_prompt


def test_basic_auth_page(browser):
    basic_auth_page = BasicAuthPage(browser)
    basic_auth_page.open()
    success_message = basic_auth_page.get_success_message()
    assert success_message == "Congratulations! You must have the proper credentials.", \
        f"Ожидался текст 'Congratulations! You must have the proper credentials.', получен {success_message}"


def test_alerts_page(browser):
    alert_page = AlertPage(browser)
    alert_page.open()
    alert_page.js_alert_button.click()
    alert_text = browser.get_alert_text()
    assert alert_text == "I am a JS Alert", f"Ожидался текст: 'I am a JS Alert', получен {alert_text}"
    browser.accept_alert()
    browser.wait_alert_closed()
    alert_result_text = alert_page.alert_result_text.get_text()
    assert alert_result_text == "You successfully clicked an alert", \
        f"Ожидался текст: You successfully clicked an alert, получен {alert_result_text}"
    alert_page.js_confirm_button.click()
    confirm_alert_text = browser.get_alert_text()
    assert confirm_alert_text == "I am a JS Confirm", \
        f"Ожидался текст: 'I am a JS Confirm', получен: {confirm_alert_text}"
    browser.accept_alert()
    browser.wait_alert_closed()
    confirm_result_text = alert_page.alert_result_text.get_text()
    assert confirm_result_text == "You clicked: Ok", \
        f"Ожидался текст: 'You clicked: Ok', получен: {confirm_result_text}"
    alert_page.js_prompt_button.click()
    prompt_alert_text = browser.get_alert_text()
    assert prompt_alert_text == "I am a JS prompt", \
        f"Ожидался текст: 'I am a JS prompt', получен {prompt_alert_text}"
    random_value = random_prompt(12)
    browser.send_keys_alert(random_value)
    browser.accept_alert()
    browser.wait_alert_closed()
    prompt_result_text = alert_page.alert_result_text.get_text()
    assert prompt_result_text == f"You entered: {random_value}", \
        f"Ожидался текст: You entered: {random_value}, получен: {prompt_result_text}"


def test_alerts_js_page(browser):
    alert_page = AlertPage(browser)
    alert_page.open()
    alert_page.js_alert_button.js_click()
    alert_text = browser.get_alert_text()
    assert alert_text == "I am a JS Alert", f"Ожидался текст: 'I am a JS Alert', получен {alert_text}"
    browser.accept_alert()
    alert_result_text = alert_page.alert_result_text.get_text()
    assert alert_result_text == "You successfully clicked an alert", \
        f"Ожидался текст: You successfully clicked an alert, получен {alert_result_text}"
    alert_page.js_confirm_button.js_click()
    confirm_alert_text = browser.get_alert_text()
    assert confirm_alert_text == "I am a JS Confirm", \
        f"Ожидался текст: 'I am a JS Confirm', получен: {confirm_alert_text}"
    browser.accept_alert()
    confirm_result_text = alert_page.alert_result_text.get_text()
    assert confirm_result_text == "You clicked: Ok", \
        f"Ожидался текст: 'You clicked: Ok', получен: {confirm_result_text}"
    alert_page.js_prompt_button.js_click()
    prompt_alert_text = browser.get_alert_text()
    assert prompt_alert_text == "I am a JS prompt", \
        f"Ожидался текст: 'I am a JS prompt', получен {prompt_alert_text}"
    random_value = random_prompt(12)
    browser.send_keys_alert(random_value)
    browser.accept_alert()
    browser.wait_alert_closed()
    prompt_result_text = alert_page.alert_result_text.get_text()
    assert prompt_result_text == f"You entered: {random_value}", \
        f"Ожидался текст: You entered: {random_value}, получен: {prompt_result_text}"


def test_context_menu_page(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.open()
    context_menu_page.context_menu_area.right_click()
    context_menu_text = browser.get_alert_text()
    assert context_menu_text == "You selected a context menu", \
        f"Ожидался текст: 'You selected a context menu', получен: {context_menu_text}"
    browser.accept_alert()
    browser.wait_alert_closed()


def test_actions_page(browser):
    actions_page = ActionsPage(browser)
    actions_page.open()
    slider_button = actions_page.slider_input
    actions_page.set_random_slider_value()
    slider_value = actions_page.get_slider_value()
    displayed_slider_value = actions_page.get_displayed_value()
    assert slider_value == displayed_slider_value, (f"Установлено значение слайдера: '{slider_button}',"
                                                    f"отображается: '{displayed_slider_value}'")


def test_hovers_page(browser):
    hovers_page = HoversPage(browser)
    hovers_page.open()
    hovers_page.process_all_users()


def test_handlers_page(browser):
    handlers_page = HandlersPage(browser)
    handlers_page.open()
    handlers_page.wait_for_open()
    handlers_page.link_button.click()
    title_window = browser.get_title()
    assert title_window == handlers_page.NEW_WINDOW_TITLE, \
        (f"Ожидалось название текущей вкладки '{handlers_page.NEW_WINDOW_TITLE}', "
         f"получено: '{title_window}'")
