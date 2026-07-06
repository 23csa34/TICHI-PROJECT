from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ---------------- LOCATORS ---------------- #

    SIGN_IN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Sign In')]"
    )

    EMAIL = (
        By.ID,
        "email"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    PASSWORD = (
        By.ID,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and normalize-space()='Login']"
    )

    # ---------------- ACTIONS ---------------- #

    def open_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        ).click()

    def enter_email(self, email):
        email_box = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        email_box.clear()
        email_box.send_keys(email)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def enter_password(self, password):
        password_box = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        password_box.clear()
        password_box.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def click_forgot_password(self):
        forgot = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Forgot Password')]")
            )
        )

        print("Found:", forgot.text)

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", forgot
        )

        self.driver.execute_script(
            "arguments[0].click();", forgot
        )

    # ---------------- COMPLETE LOGIN ---------------- #

    def login(self, email, password):
        self.open_login()
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_login()