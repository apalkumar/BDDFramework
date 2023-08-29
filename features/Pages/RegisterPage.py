import time

from selenium.webdriver.common.by import By

from features.Pages.AccountPage import AccountPage
from features.Pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_name = "firstname"
    last_name_id = "input-lastname"
    email_by_name = "email"
    telephone_name = "telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    privacy_policy_xpath = "//input[@type='checkbox']"
    continue_button_xpath = "//input[@type='submit']"
    account_creation_confirmation_xpath = "//div//h1[text()='Your Account Has Been Created!']"
    subscribe_radio_button = "//input[@name = 'newsletter' and @value=1]"
    duplicate_email_warning_message_xpath = "//div[@id='account-register']//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@name='firstname']//following-sibling::div"
    last_name_warning_message_xpath = "//input[@name='lastname']//following-sibling::div"
    email_warning_message_xpath = "//input[@name='email']//following-sibling::div"
    telephone_warning_message_xpath = "//input[@name='telephone']//following-sibling::div"
    password_warning_message_xpath = "//input[@name='password']//following-sibling::div"

    def enter_first_name(self, fname):
        self.type_into_element("first_name_name", self.first_name_name, fname)

    def enter_last_name(self, lname):
        self.type_into_element("last_name_id", self.last_name_id, lname)

    def enter_email(self, email):
        self.type_into_element("email_by_name", self.email_by_name, email)

    def enter_telephone(self, telephone):
        self.type_into_element("telephone_name", self.telephone_name, telephone)

    def enter_password1(self, pwd):
        self.type_into_element("password_id", self.password_id, pwd)
        # self.driver.find_eleent(By.NAME, self.telephone_name).send_keys(telephone)

    def enter_confirm_password(self, pwd):
        self.type_into_element("confirm_password_id", self.confirm_password_id, pwd)

    def select_privacy_policy(self):
        self.click_on_element("privacy_policy_xpath", self.privacy_policy_xpath)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return AccountPage(self.driver)

    def account_creation_confirmation_message(self, account_confirm_message):
        return self.retrieved_element_text_should_contain("account_creation_confirmation_xpath",
                                                          self.account_creation_confirmation_xpath,
                                                          account_confirm_message)

    def select_subscribe_button(self):
        self.driver.find_element(By.XPATH, self.subscribe_radio_button).click()

    def duplicate_email_warning_message(self):
        return self.element_is_displayed("duplicate_email_warning_message_xpath", self.duplicate_email_warning_message_xpath)

    def verify_privacy_policy_warning_message(self, privacy_policy_warning_message):
        return self.retrieved_element_text_should_contain("privacy_policy_warning_xpath", self.privacy_policy_warning_xpath,
                                                          privacy_policy_warning_message)

    def verify_first_name_warning_message(self, firstname_warning_message):
        return self.retrieved_element_text_should_contain("first_name_warning_message_xpath",
                                                          self.first_name_warning_message_xpath,
                                                          firstname_warning_message)

    def verify_last_name_warning_message(self, lastname_warning_message):
        return self.retrieved_element_text_should_contain("last_name_warning_message_xpath",
                                                          self.last_name_warning_message_xpath,
                                                          lastname_warning_message)

    def verify_email_warning_message(self, expected_Email_warning):
        return self.retrieved_element_text_should_contain("email_warning_message_xpath",
                                                          self.email_warning_message_xpath,
                                                          expected_Email_warning)

    def verify_telephone_warning_message(self, expected_telephone_warning):
        return self.retrieved_element_text_should_contain("telephone_warning_message_xpath",
                                                          self.telephone_warning_message_xpath,
                                                          expected_telephone_warning)

    def verify_password_warning_message(self, expected_password_warning):
        return self.retrieved_element_text_should_contain("password_warning_message_xpath",
                                                          self.password_warning_message_xpath,
                                                          expected_password_warning)