from behave import *

@given('EMAG I am on the main page')
def step_impl(context):
    context.emag_search.navigate_to_page()

@when('EMAG I click on the search button')
def step_impl(context):
    context.emag_search.click_on_search_button()

@when('EMAG I enter the keyword "{keyword}"')
def step_impl(context, keyword):
    context.emag_search.type_anything_on_search(keyword)

@when('EMAG I click the magnifier')
def step_impl(context):
    context.emag_search.click_on_magnifier_button()

@then('EMAG "{keyword}" keyword is in title phrasing element')
def step_impl(context, keyword):
    assert keyword in context.emag_search.get_title_text(), f"{keyword} is not found in title phrasing after search"

@then('EMAG "{keyword}" keyword is in negative title phrasing element')
def step_impl(context, keyword):
    assert keyword in context.emag_search.get_title_negative_text(), f"{keyword} is not found in title phrasing after search"

@then('EMAG "{keyword}" is in negative title phrasing number element')
def step_impl(context, keyword):
    assert keyword in context.emag_search.get_number_of_products_negative_text(), f"{keyword} is not found in title phrasing number after search"