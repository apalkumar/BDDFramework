from features.Pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "HP LP3065"
    message_xpath = "//input[@id='button-search']//following-sibling::p"

    def display_status_of_product(self):
        return self.element_is_displayed("valid_product_link_text",
                                         self.valid_product_link_text)

    def display_stauts_of_message(self, expected_message_text):
        return self.retrieved_element_text_should_equals("message_xpath", self.message_xpath, expected_message_text)