from behave import *
from selenium.webdriver.common.by import By
from features.Pages.HomePage import HomePage


@given(u'I got navigate to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title("Your Store")


@when(u'I entered valid product "{product}" into the search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@when(u'I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.search_page.display_status_of_product()


@when(u'I entered Invalid product "{product}" into the search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@then(u'Proper message should be displayed in Search Results')
def step_impl(context):
    for row in context.table:
        assert context.search_page.display_stauts_of_message(row["warning_message"])


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
