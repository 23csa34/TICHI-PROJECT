from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    # Email
    email_textbox = (By.ID, "email")
    continue_button = (By.XPATH, "//button[text()='Continue']")
    email_error = (By.XPATH, "//p[text()='Email is required']")

    # First Name
    first_name = (By.ID, "firstName")
    first_name_error = (By.XPATH, "//p[text()='First name is required']")

    # Last Name
    last_name = (By.ID, "lastName")
    
    #Mobile Number
    phone_number = (By.ID, "phoneNumber")

    # Password
    password = (By.ID, "password")
    password_error = (By.XPATH, "//p[text()='Password is required']")

    # Confirm Password
    confirm_password = (By.ID, "confirmPassword")
    password_mismatch_error = (
        By.XPATH,
        "//p[text()='Passwords do not match']" )

    # Sign Up Button
    signup_button = (By.XPATH, "//button[text()='Sign Up']")

    
    # Terms & Conditions Checkbox
    terms_checkbox = (By.ID, "remember")

    
    # Methods

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).clear()
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.email_error).text

    def get_email_validation_message(self):
        return self.driver.find_element(
            *self.email_textbox
        ).get_attribute("validationMessage")

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name).clear()
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name):
     self.driver.find_element(*self.last_name).clear()
     self.driver.find_element(*self.last_name).send_keys(name)    

    def get_first_name_error_message(self):
        return self.driver.find_element(*self.first_name_error).text

    def enter_password(self, password):
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)

    def get_password_error_message(self):
        return self.driver.find_element(*self.password_error).text

    def enter_confirm_password(self, password):
        self.driver.find_element(*self.confirm_password).clear()
        self.driver.find_element(*self.confirm_password).send_keys(password)

    def get_password_mismatch_error(self):
        return self.driver.find_element(
            *self.password_mismatch_error
        ).text

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()

    def enter_phone_number(self, number):
     self.driver.find_element(*self.phone_number).clear()
     self.driver.find_element(*self.phone_number).send_keys(number) 

    def click_terms_checkbox(self):
     self.driver.find_element(*self.terms_checkbox).click()