from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('I insert an username "{username}"')
def step_impl(context, username):
    #context.home_page....
    context.login_page.set_email(username)

@when('I insert a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login()

@then('The banner is displayed')
def step_impl(context):
    assert context.login_page.is_message_displayed(), 'Banner is not displayed'

@then('The message is "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_message_text(), "Message is not the same"
