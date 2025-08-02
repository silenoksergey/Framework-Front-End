import os
import time

from pages.actions_page import ActionsPage
from pages.alert_page import AlertPage
from pages.basic_auth_page import BasicAuthPage
from pages.context_menu_page import ContextMenuPage
from pages.dynamic_content_page import DynamicContentPage
from pages.frames_main_page import FramesMainPage
from pages.frames_page import FramesPage
from pages.handlers_page import HandlersPage
from pages.hovers_page import HoversPage
from pages.infinite_scroll_page import InfiniteScrollPage
from pages.nested_frames_page import NestedFramesPage
from pages.upload_page import UploadPage
from utils.pyautogui_utils import PyAutoGUIUtilities
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
    random_value = random_prompt()
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

    users_data = hovers_page.get_all_users_data()

    for i, user_data in enumerate(users_data):
        hovers_page.wait_for_open()
        user_name = user_data['name']
        user_block = user_data['block']
        profile_link = user_data['profile_link']

        expected_user_name = f"name: user{i + 1}"
        assert user_name == expected_user_name, \
            f"Ожидалось имя пользователя: '{expected_user_name}', получено: '{user_name}'"

        hovers_page.click_profile_link(user_block, profile_link)

        current_url = hovers_page.get_current_url()
        expected_user_number = f"users/{i + 1}"
        assert expected_user_number in current_url, \
            (f"Ожидалось, что откроется страница с пользователем {expected_user_number},"
             f" фактически открылась: {current_url}")

        browser.driver.back()


def test_handlers_page(browser):
    handlers_page = HandlersPage(browser)
    handlers_page.open()
    handlers_page.wait_for_open()

    handlers_page.open_new_window()
    window_text = handlers_page.get_new_window_text()
    assert window_text == handlers_page.NEW_WINDOW_PAGE_TEXT, \
        f"Ожидался текст: '{handlers_page.NEW_WINDOW_PAGE_TEXT}', получен: '{window_text}'"
    window_title = handlers_page.get_current_window_title()
    assert window_title == handlers_page.NEW_WINDOW_TITLE, \
        f"Ожидался заголовок окна: '{handlers_page.NEW_WINDOW_TITLE}', получен: '{window_title}'"
    handlers_page.return_to_main_window()

    first_new_handle = handlers_page.get_last_window_handle()

    handlers_page.open_new_window()
    window_text = handlers_page.get_new_window_text()
    assert window_text == handlers_page.NEW_WINDOW_PAGE_TEXT, \
        f"Ожидался текст: '{handlers_page.NEW_WINDOW_PAGE_TEXT}', получен: '{window_text}'"
    window_title = handlers_page.get_current_window_title()
    assert window_title == handlers_page.NEW_WINDOW_TITLE, \
        f"Ожидался заголовок окна: '{handlers_page.NEW_WINDOW_TITLE}', получен: '{window_title}'"
    handlers_page.return_to_main_window()

    second_new_handle = handlers_page.get_last_window_handle()

    handlers_page.switch_to_window_by_handle(first_new_handle)
    handlers_page.close_current_window()
    handlers_page.switch_to_window_by_handle(second_new_handle)
    handlers_page.close_current_window()


def test_frames_pages(browser):
    frames_main_page = FramesMainPage(browser)
    frames_page = FramesPage(browser)
    nested_frames_page = NestedFramesPage(browser)
    frames_page.open()
    frames_page.wait_for_open()
    frames_main_page.click_ensure_menu()
    frames_main_page.nested_frames_button.click()
    nested_frames_page.wait_for_open()
    nested_parent_frame_text = nested_frames_page.get_parent_frame_text()
    assert nested_parent_frame_text == "Parent frame", \
        f"Ожидался текст: 'Parent frame', получен: '{nested_parent_frame_text}'"
    nested_child_frame_text = nested_frames_page.get_child_frame_text()
    assert nested_child_frame_text == "Child Iframe", \
        f"Ожидался текст: 'Child Iframe', получен: '{nested_child_frame_text}'"
    frames_main_page.click_ensure_menu()
    frames_button = frames_main_page.frames_button
    frames_button.click()
    frames_page.wait_for_open()
    first_frame_text = frames_page.get_frame_text(frames_page.first_frame)
    second_frame_text = frames_page.get_frame_text(frames_page.second_frame)
    assert first_frame_text == second_frame_text, \
        (f"Ожидалось, что текст первого фрейма будет равен тексту второго фрейма."
         f" Первый фрейм: '{first_frame_text}', второй фрейм: '{second_frame_text}'")


def test_dynamic_content_page(browser):
    dynamic_content_page = DynamicContentPage(browser)
    dynamic_content_page.open()
    dynamic_content_page.wait_for_open()
    has_duplicates_avatars = dynamic_content_page.check_duplicates_avatars()
    assert has_duplicates_avatars is True, f"Не найдены дубликаты аватаров"


def test_infinite_scroll_page(browser):
    infinite_scroll_page = InfiniteScrollPage(browser)
    infinite_scroll_page.open()
    infinite_scroll_page.wait_for_open()
    infinite_scroll_page.scroll_until_paragraphs()


def test_upload_page(browser):
    upload_page = UploadPage(browser)
    upload_page.open()
    upload_page.wait_for_open()
    upload_page.upload_image()
    upload_file_name = upload_page.get_upload_file_name()
    upload_page.upload_submit_button.click()
    successful_message = upload_page.successful_message.get_text()
    assert successful_message == "File Uploaded!", \
        f"Ожидался текст: 'File Uploaded!', получен: {successful_message}"
    displayed_upload_file_name = upload_page.upload_file_name.get_text()
    assert upload_file_name == displayed_upload_file_name, \
        (f"Неверное отображение имени файла. Ожидалось: '{upload_file_name}',"
         f" отображается: '{displayed_upload_file_name}'")


def test_upload_dialog_window(browser):
    upload_page = UploadPage(browser)
    upload_page.open()
    upload_page.wait_for_open()
    upload_page.upload_area.click()
    PyAutoGUIUtilities.upload_file(upload_page.IMAGE_FILE_PATH)
    expected_filename = os.path.basename(upload_page.IMAGE_FILE_PATH)
    display_file_name = upload_page.upload_area_file_display.get_text()
    assert expected_filename == display_file_name, \
        (f"Отображается неверное имя файла. Ожидалось: '{expected_filename}',"
         f" отображается: '{display_file_name}'")
    assert upload_page.upload_success_mark.is_exist(), f"Галочка об успешной загрузке файла отсутствует"
