from datetime import datetime

from behave import *
from features.Pages.HomePage import HomePage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigated to Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # invalid_email = "anil" + time_stamp + "@gmail.com"
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_time_stamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("123456")


@when(u'I dont enter anything into email and password the fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    for row in context.table:
        context.login_page.enter_email_address(row["email_id"])
        context.login_page.enter_password(row["invalid_password"])

        # context.login_page.enter_email_address("abcd1234#@gmail.com")
        # context.login_page.enter_password("2135")


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # invalid_email = "anil" + time_stamp + "@gmail.com"
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_time_stamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("@@#@@")


@then(u'I should get a proper warning message')
def step_impl(context):
    # expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    for row in context.table:
        # assert context.login_page.display_status_of_warning_message(expected_warning_message)
        assert context.login_page.display_status_of_warning_message(row["expected_warning_message"])