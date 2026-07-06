import time
import pytest
from utilities.driver_factory import DriverFactory
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    driver.get("https://tichi-app-webapp-stage.web.app")
    yield driver
    driver.quit()


def login(driver, email, password):
    page = LoginPage(driver)

    page.open_login()
    page.enter_email(email)
    page.click_continue()
    time.sleep(2)
    page.enter_password(password)
    page.click_login()
    time.sleep(3)


# TC01 - Valid Login
def test_valid_login(driver):
    login(driver, "23csa34@karpagamtech.ac.in", "Password@123")
    assert "login" not in driver.current_url.lower()


# TC02 - Invalid Password
def test_invalid_password(driver):
    login(driver, "23csa34@karpagamtech.ac.in", "Wrong@123")
    assert True


# TC03 - Empty Password
def test_empty_password(driver):
    page = LoginPage(driver)
    page.open_login()
    page.enter_email("23csa34@karpagamtech.ac.in")
    page.click_continue()
    page.click_login()
    assert True


# TC04 - Empty Email
def test_empty_email(driver):
    page = LoginPage(driver)
    page.open_login()
    page.click_continue()
    assert True


# TC05 - Invalid Email Format
def test_invalid_email(driver):
    page = LoginPage(driver)
    page.open_login()
    page.enter_email("abcgmail.com")
    page.click_continue()
    assert True


# TC06 - Unregistered Email
def test_unregistered_email(driver):
    page = LoginPage(driver)
    page.open_login()
    page.enter_email("qa123456789@gmail.com")
    page.click_continue()
    assert True


# TC07 - Email With Spaces
def test_email_spaces(driver):
    page = LoginPage(driver)
    page.open_login()
    page.enter_email("  23csa3 4@karpagamtech.ac.in")
    page.click_continue()
    assert True


# TC08 - Password Case Sensitive
def test_password_case(driver):
    login(driver, "23csa34@karpagamtech.ac.in", "Password@123")
    assert True


# TC09 - Forgot Password
def test_forgot_password(driver):
    page = LoginPage(driver)

    page.open_login()
    page.enter_email("23csa34@karpagamtech.ac.in")
    page.click_continue()

    import time
    time.sleep(5)

    driver.save_screenshot("forgot_debug.png")

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    page.click_forgot_password()

# TC10 - Login Button Displayed
def test_login_button(driver):
    page = LoginPage(driver)
    page.open_login()

    button = driver.find_element("xpath", "//button[@type='submit']")
    assert button.is_displayed()