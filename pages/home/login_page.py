from base.base_page import BasePage
import time


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _login_button = ".btn.btn-default.btn-block.btn-md.dynamic-button"
    _my_profile_button = "dropdownMenu1"
    _logout_link = "Logout"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='link')

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type='css')

    def click_my_profile_button(self):
        self.element_click(self._my_profile_button, "id")

    def click_logout_link(self):
        self.element_click(self._logout_link, "link")

    def login(self, username="", password=""):
        self.click_login_link()
        self.clear_fields()
        self.enter_email(username)
        self.enter_password(password)
        time.sleep(1)
        self.click_login_button()

    def logout(self):
        self.click_my_profile_button()
        self.click_logout_link()

    def verify_login_successful(self):
        result = self.is_element_present(
            "dropdownMenu1", "id")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(".dynamic-text.help-block", "css")
        return result

    def clear_fields(self):
        email_field = self.get_element(self._email_field)
        email_field.clear()
        password_field = self.get_element(self._password_field)
        password_field.clear()

    def verify_login_title(self):
        return self.verify_page_title("All Courses")
