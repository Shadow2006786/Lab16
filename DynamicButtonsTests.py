# AllTests.py
import pytest
from DynamicButtonsPages import SearchHelper
import time
from playwright.sync_api import Page


def test_click_all_buttons(page: Page):
    search = SearchHelper(page)
    search.go_to_site()

    search.click_start()
    time.sleep(1)
    search.click_one()
    time.sleep(1)
    search.click_two()
    time.sleep(1)
    search.click_three()
    time.sleep(1)

    assert search.is_all_buttons_clicked_displayed()

def test_mp3_player(page: Page):
    page.goto("https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20")
    page.click("text=MP3 Players (4)")
    page.click("text=iPod Classic")
    assert page.locator("//p[contains(text(),'songs')]").is_visible()

def test_basic_html_form(page: Page):
    page.goto("https://testpages.eviltester.com/styled/basic-html-form-test.html")
    page.fill("[name='username']", "testuser")
    page.fill("[name='password']", "password123")
    page.fill("[name='comments']", "This is a test comment.")
    page.click("input[type='submit']")

    result_username = page.text_content("#_valueusername")
    result_comments = page.text_content("#_valuecomments")

    assert result_username == "testuser"
    assert result_comments == "This is a test comment."

def test_login_auth(page: Page):
    page.goto("https://testpages.eviltester.com/styled/auth/basic-auth-test.html")

    username_text = page.text_content("xpath=//p[contains(text(), 'username:')]")
    password_text = page.text_content("xpath=//p[contains(text(), 'password:')]")

    real_username = username_text.split(": ")[1].strip()
    real_password = password_text.split(": ")[1].strip()

    assert page.locator("h1:has-text('Basic Auth Page Protection')").is_visible()


    page.goto(f"https://{real_username}:{real_password}@testpages.eviltester.com/styled/auth/basic-auth-results.html")
    assert page.locator("text=Authenticated").is_visible()

def test_file_upload(page: Page, tmp_path):
    page.goto("https://testpages.eviltester.com/styled/file-upload-test.html")
    file_path = tmp_path / "test_upload.txt"
    file_path.write_text("Test file content")

    page.set_input_files("input[name='filename']", str(file_path))
    page.click("input[name='upload']")

    body_text = page.text_content("body")
    assert "test_upload.txt" in body_text
    assert "You uploaded a file" in body_text

def test_alert(page: Page):
    page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

    def handle_dialog(dialog):
        assert dialog.message == "I am an alert box!"
        dialog.accept()

    page.on("dialog", handle_dialog)
    page.click("#alertexamples")

def test_fake_alerts(page: Page):
    page.goto("https://testpages.eviltester.com/styled/alerts/fake-alert-test.html")
    page.click("#fakealert")

    dialog_text = page.text_content("#dialog-text")
    assert "I am a fake alert box!" in dialog_text

    page.click("#dialog-ok")
    page.wait_for_selector(".dialog", state="hidden")

    explanation = page.text_content("xpath=//p[contains(text(), 'The buttons on this page create modal dialogs')]")
    assert "The buttons on this page create modal dialogs" in explanation
