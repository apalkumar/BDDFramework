from features.Pages.BasePage import BasePage
from features.Pages.LoginPage import LoginPage
from features.Pages.RegisterPage import RegisterPage
from features.Pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"
    Register_option_link_text = "Register"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def click_on_register(self):
        self.click_on_element("Register_option_link_text", self.Register_option_link_text)
        return RegisterPage(self.driver)

    def check_home_page_title(self, expected_title_text):
        return self.verify_page_title(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        self.type_into_element("search_box_field_name", self.search_box_field_name, product_text)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)




