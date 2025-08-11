from pathlib import Path
from config.urls import internet, demoqa, InternetEP, DemoqaEP, internet_auth
from pages.actions_page import ActionsPage
from pages.alert_page import AlertPage, ClickMode
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
    user = "admin"
    pwd = "admin"

    basic_auth_page = BasicAuthPage(browser)
    browser.get(internet_auth(InternetEP.BASIC_AUTH, user, pwd))
    basic_auth_page.wait_for_open()
    success_message = basic_auth_page.get_success_message()
    assert success_message == "Congratulations! You must have the proper credentials.", \
        f"Ожидался текст 'Congratulations! You must have the proper credentials.', получен {success_message}"


def test_alerts_page(browser):
    browser.get(internet(InternetEP.JAVASCRIPT_ALERTS))
    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    _test_alert_workflow(alert_page, mode=ClickMode.NATIVE)

    _test_alert_workflow(alert_page, mode=ClickMode.JS)


def _test_alert_workflow(alert_page: AlertPage, mode: ClickMode):
    alert_page.click_js_alert_button(mode)
    alert_text = alert_page.get_alert_text()
    expected_alert = "I am a JS Alert"
    assert alert_text == expected_alert, f"Ожидалось: '{expected_alert}', получено: '{alert_text}'"
    alert_page.accept_alert()
    if mode is ClickMode.NATIVE:
        alert_page.wait_for_alert_closed()
    result_text = alert_page.get_alert_result_text()
    expected_result = "You successfully clicked an alert"
    assert result_text == expected_result, f"Ожидалось: '{expected_result}', получено: '{result_text}'"

    alert_page.click_js_confirm_button(mode)
    confirm_text = alert_page.get_alert_text()
    expected_confirm = "I am a JS Confirm"
    assert confirm_text == expected_confirm, f"Ожидалось: '{expected_confirm}', получено: '{confirm_text}'"
    alert_page.accept_alert()
    if mode is ClickMode.NATIVE:
        alert_page.wait_for_alert_closed()
    confirm_result = alert_page.get_alert_result_text()
    expected_confirm_result = "You clicked: Ok"
    assert confirm_result == expected_confirm_result, f"Ожидалось: '{expected_confirm_result}', получено: '{confirm_result}'"

    alert_page.click_js_prompt_button(mode)
    prompt_text = alert_page.get_alert_text()
    expected_prompt = "I am a JS prompt"
    assert prompt_text == expected_prompt, f"Ожидалось: '{expected_prompt}', получено: '{prompt_text}'"
    value = random_prompt()
    alert_page.send_keys_to_alert(value)
    alert_page.accept_alert()
    alert_page.wait_for_alert_closed()
    prompt_result = alert_page.get_alert_result_text()
    expected_prompt_result = f"You entered: {value}"
    assert prompt_result == expected_prompt_result, f"Ожидалось: '{expected_prompt_result}', получено: '{prompt_result}'"


def test_context_menu_page(browser):
    browser.get(internet(InternetEP.CONTEXT_MENU))
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.wait_for_open()

    context_menu_page.right_click_context_menu_area()
    context_menu_text = context_menu_page.get_alert_text()
    assert context_menu_text == "You selected a context menu", \
        f"Ожидался текст: 'You selected a context menu', получен: {context_menu_text}"
    context_menu_page.accept_alert()
    context_menu_page.wait_for_alert_closed()


def test_actions_page(browser):
    actions_page = ActionsPage(browser)
    browser.get(internet(InternetEP.HORIZONTAL_SLIDER))
    actions_page.wait_for_open()
    slider_button = actions_page.slider_input
    actions_page.set_random_slider_value()
    slider_value = actions_page.get_slider_value()
    displayed_slider_value = actions_page.get_displayed_value()
    assert slider_value == displayed_slider_value, (f"Установлено значение слайдера: '{slider_button}',"
                                                    f"отображается: '{displayed_slider_value}'")


def test_hovers_page(browser):
    hovers_page = HoversPage(browser)
    browser.get(internet(InternetEP.HOVERS))
    hovers_page.wait_for_open()

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

        browser.back()


def test_handlers_page(browser):
    handlers_page = HandlersPage(browser)
    browser.get(internet(InternetEP.WINDOWS))
    handlers_page.wait_for_open()

    handlers_page.click_new_window_link()
    browser.switch_to_window(HandlersPage.NEW_WINDOW_TITLE)
    window_text = handlers_page.get_new_window_text()
    assert window_text == HandlersPage.NEW_WINDOW_PAGE_TEXT, \
        f"Ожидался текст: '{HandlersPage.NEW_WINDOW_PAGE_TEXT}', получен: '{window_text}'"
    window_title = browser.get_title()
    assert window_title == HandlersPage.NEW_WINDOW_TITLE, \
        f"Ожидался заголовок окна: '{HandlersPage.NEW_WINDOW_TITLE}', получен: '{window_title}'"
    browser.switch_to_default_window()

    first_new_handle = browser.get_last_window_handle()

    handlers_page.click_new_window_link()
    browser.switch_to_window(HandlersPage.NEW_WINDOW_TITLE)
    window_text = handlers_page.get_new_window_text()
    assert window_text == HandlersPage.NEW_WINDOW_PAGE_TEXT, \
        f"Ожидался текст: '{HandlersPage.NEW_WINDOW_PAGE_TEXT}', получен: '{window_text}'"
    window_title = browser.get_title()
    assert window_title == HandlersPage.NEW_WINDOW_TITLE, \
        f"Ожидался заголовок окна: '{HandlersPage.NEW_WINDOW_TITLE}', получен: '{window_title}'"
    browser.switch_to_default_window()

    second_new_handle = browser.get_last_window_handle()

    browser.switch_to_window_by_handle(first_new_handle)
    browser.close()
    browser.switch_to_window_by_handle(second_new_handle)
    browser.close()


def test_frames_pages(browser):
    frames_main_page = FramesMainPage(browser)
    frames_page = FramesPage(browser)
    nested_frames_page = NestedFramesPage(browser)
    browser.get(demoqa(DemoqaEP.FRAMES))
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
    browser.get(internet(InternetEP.DYNAMIC_CONTENT))
    dynamic_content_page.wait_for_open()

    max_attempts = 10
    has_duplicates = False

    for attempt in range(max_attempts):
        avatars_sources = dynamic_content_page.get_avatars_sources()

        if len(avatars_sources) != len(set(avatars_sources)):
            has_duplicates = True
            break

        if attempt < max_attempts - 1:
            browser.refresh_page()
            dynamic_content_page.wait_for_open()

    assert has_duplicates, f"Не найдены дубликаты аватаров после {max_attempts} попыток"


def test_infinite_scroll_page(browser):
    infinite_scroll_page = InfiniteScrollPage(browser)
    browser.get(internet(InternetEP.INFINITE_SCROLL))
    infinite_scroll_page.wait_for_open()

    max_attempts = 50
    target_paragraphs = 27

    for attempt in range(max_attempts):
        current_count = infinite_scroll_page.get_paragraphs_count()

        if current_count >= target_paragraphs:
            break

        infinite_scroll_page.scroll_to_bottom()
        infinite_scroll_page.wait_for_open()

    final_count = infinite_scroll_page.get_paragraphs_count()
    assert final_count >= target_paragraphs, \
        f"Не удалось достичь {target_paragraphs} параграфов. Получено: {final_count}"


def test_upload_page(browser):
    upload_page = UploadPage(browser)
    file_path = (Path(__file__).parent / "test_files" / "images" / "bober.png").resolve()
    browser.get(internet(InternetEP.UPLOAD))
    upload_page.wait_for_open()
    upload_page.upload_image(str(file_path))
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
    browser.get(internet(InternetEP.UPLOAD))
    upload_page.wait_for_open()

    upload_page.upload_area.click()

    file_path = (Path(__file__).parent / "test_files" / "images" / "bober.png").resolve()
    PyAutoGUIUtilities.upload_file(str(file_path))

    expected_filename = file_path.name
    display_file_name = upload_page.upload_area_file_display.get_text()
    assert expected_filename == display_file_name, (
        f"Отображается неверное имя файла. Ожидалось: '{expected_filename}', "
        f"отображается: '{display_file_name}'"
    )
    assert upload_page.upload_success_mark.is_exist(), "Галочка об успешной загрузке файла отсутствует"
