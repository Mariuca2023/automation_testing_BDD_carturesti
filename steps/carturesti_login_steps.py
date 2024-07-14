from behave import *

@given('CARTURESTI I am on the login page')
def step_impl(context):
    context.carturesti_login.navigate_to_page()

@when('CARTURESTI I click on "COOKIES_BUTTON"')
def step_impl(context):
    context.carturesti_login.click_allow_cookies()

@when('CARTURESTI I click on the login button')
def step_impl(context):
    context.carturesti_login.click_login()
@when('CARTURESTI I click on UTILIZATOR EXISTENT')
def step_impl(context):
    context.carturesti_login.click_utilizator()

@when('CARTURESTI I insert an username "{username}"')
def step_impl(context, username):
    #context.home_page....
    context.carturesti_login.set_email(username)

@when('CARTURESTI I insert a password "{password}"')
def step_impl(context, password):
    context.carturesti_login.set_password(password)


@then('CARTURESTI The banner is displayed')
def step_impl(context):
    assert context.carturesti_login.is_message_displayed(), 'Banner is not displayed'

@then('CARTURESTI The message is "{message}"')
def step_impl(context, message):
    assert message in context.carturesti_login.get_message_text(), "Message is not the same"
