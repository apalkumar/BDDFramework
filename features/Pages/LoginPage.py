import time

from features.Pages.AccountPage import AccountPage
from features.Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_xpath = "//input[@name = 'email']"
    password_address_field_xpath = "//input[@name = 'password']"
    login_button_xpath = "//input[@type='submit']"
    warning_message_xpath = "//div[@id='account-login']//div[1]"

    def enter_email_address(self, email_text):
        self.type_into_element("email_address_field_xpath", self.email_address_field_xpath, email_text)

    def enter_password(self, pwd):
        # time.sleep(5)
        self.type_into_element("password_address_field_xpath", self.password_address_field_xpath, pwd)
        # time.sleep(5)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def display_status_of_warning_message(self,expected_warning_text):
        return self.retrieved_element_text_should_contain("warning_message_xpath", self.warning_message_xpath, expected_warning_text)