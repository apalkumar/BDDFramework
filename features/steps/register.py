import time
from datetime import datetime
from behave import *

from features.Pages.HomePage import HomePage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigate to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.click_on_register()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # Valid_email = "anil" + time_stamp + "@gmail.com"
        # f_Name = "First Name"
        # l_Name = "Last Name"
        # telehone_number = "2588"
        # pwd = "123456"
        Valid_email = EmailWithTimeStampGenerator.get_new_email_with_time_stamp()
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_email(Valid_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password1(row["password"])
        context.register_page.enter_confirm_password(row["password"])
        context.register_page.select_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    expected_message = "Your Account Has Been Created!"
    assert context.register_page.account_creation_confirmation_message(expected_message)


@when(u'I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # Valid_email = "anil" + time_stamp + "@gmail.com"
        # f_Name = "First Name"
        # l_Name = "Last Name"
        # telehone_number = "2588"
        # pwd = "123456"
        Valid_email = EmailWithTimeStampGenerator.get_new_email_with_time_stamp()
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_email(Valid_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password1(row["password"])
        context.register_page.enter_confirm_password(row["password"])
        context.register_page.select_privacy_policy()
        context.register_page.select_subscribe_button()


@when(u'I enter below details into all fields except email field')
def step_impl(context):
    for row in context.table:
        # f_Name = "First Name"
        # l_Name = "Last Name"
        # telehone_number = "2588"
        # pwd = "123456"
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password1(row["password"])
        context.register_page.enter_confirm_password(row["password"])
        context.register_page.select_privacy_policy()


@when(u'I enter existing into the email "{existing_email}" field')
def step_impl(context, existing_email):
    # context.register_page.enter_email("abcd1234#@gmail.com")
    context.register_page.enter_email(existing_email)

@when(u'I enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password1("")
    context.register_page.enter_confirm_password("")


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    time.sleep(5)
    expected_privacy_policy_warning = 'Warning: You must agree to the Privacy Policy!'
    expected_First_Name_warning = 'First Name must be between 1 and 32 characters!'
    expected_Last_Name_warning = 'Last Name must be between 1 and 32 characters!'
    expected_Email_warning = 'E-Mail Address does not appear to be valid!'
    expected_Telephone_warning = 'Telephone must be between 3 and 32 characters!'
    expected_Password_warning = 'Password must be between 4 and 20 characters!'
    assert context.register_page.verify_privacy_policy_warning_message(expected_privacy_policy_warning)
    assert context.register_page.verify_first_name_warning_message(expected_First_Name_warning)
    assert context.register_page.verify_last_name_warning_message(expected_Last_Name_warning)
    assert context.register_page.verify_email_warning_message(expected_Email_warning)
    assert context.register_page.verify_telephone_warning_message(expected_Telephone_warning)
    assert context.register_page.verify_password_warning_message(expected_Password_warning)


@then(u'Proper warning message information about duplicate account should be displayed')
def step_impl(context):
    assert context.register_page.duplicate_email_warning_message()