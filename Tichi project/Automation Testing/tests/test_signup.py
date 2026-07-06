import time
from utilities.driver_factory import DriverFactory
from pages.signup_page import SignupPage


class TestSignup:

    def setup_method(self):
        factory = DriverFactory()
        self.driver = factory.get_driver()
        self.driver.get("https://tichi-app-webapp-stage.web.app/login")
        self.signup = SignupPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    # ---------------- EMAIL TEST CASES ----------------

    def test_empty_email(self):

        self.signup.enter_email("")
        self.signup.click_continue()

        expected = "Email is required"
        actual = self.signup.get_error_message()

        assert actual == expected

    def test_invalid_email(self):

        self.signup.enter_email("abc")
        self.signup.click_continue()

        expected = "Please include an '@' in the email address. 'abc' is missing an '@'."
        actual = self.signup.get_email_validation_message()

        assert actual == expected

    def test_valid_email(self):

        self.signup.enter_email("23csa34@karpagamtech.ac.in")
        self.signup.click_continue()

        time.sleep(2)

    # ---------------- COMMON METHOD ----------------

    def navigate_to_signup(self):

        self.signup.enter_email("ramesh@gmail.com")
        self.signup.click_continue()

        time.sleep(2)

    # ---------------- SIGNUP TEST CASES ----------------

    def test_empty_first_name(self):

        self.navigate_to_signup()

        self.signup.enter_first_name("")

        self.signup.click_signup()

        expected = "First name is required"
        actual = self.signup.get_first_name_error_message().strip()

        assert actual == expected

    def test_empty_password(self):

        self.navigate_to_signup()

        self.signup.enter_first_name("divya")

        self.signup.enter_password("")

        self.signup.click_signup()

        expected = "Password is required"
        actual = self.signup.get_password_error_message().strip()

        assert actual == expected

    def test_password_mismatch(self):

        self.navigate_to_signup()

        self.signup.enter_first_name("divya")

        self.signup.enter_password("Password@123")

        self.signup.enter_confirm_password("Password@12")

        self.signup.click_signup()

        expected = "Passwords do not match"
        actual = self.signup.get_password_mismatch_error().strip()

        assert actual == expected

    def test_invalid_mobile_number(self):

        self.navigate_to_signup()

        self.signup.enter_first_name("divya")

        self.signup.enter_phone_number("98765")

        self.signup.click_signup()

        expected = "Please lengthen this text to 10 characters or more (you are currently using 5 characters)."

        actual = self.driver.find_element(
            *self.signup.phone_number
        ).get_attribute("validationMessage")

        assert actual == expected

    def test_terms_checkbox_not_selected(self):

        self.navigate_to_signup()

        self.signup.enter_first_name("divya")
        self.signup.enter_last_name("D")
        self.signup.enter_phone_number("8015027848")
        self.signup.enter_password("Password@123")
        self.signup.enter_confirm_password("Password@123")

        # Checkbox NOT clicked

        self.signup.click_signup()

        # User should remain on Sign-Up page
        assert "sign-up" in self.driver.current_url.lower()