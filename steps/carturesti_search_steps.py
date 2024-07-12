from behave import *

@given('I am on the main page')
def step_impl(context):
    context.carturesti_search.navigate_to_page()

@given('I am on the main page with "{keyword}" keyword and page parameter "{page_parameter}"')
def step_impl(context, keyword, page_parameter):
    context.carturesti_search.navigate_to_page_with_key_word(keyword,page_parameter)

@when('I click on the search button')
def step_impl(context):
    context.carturesti_search.click_on_search_button()

@when('I enter this ISBN code "{isbn}"')
def step_impl(context, isbn):
    context.carturesti_search.type_anything_on_search(isbn)

@when('I click the magnifier')
def step_impl(context):
    context.carturesti_search.click_on_magnifier_button()

@then('The book with the title "{bookTitle}" should be visible')
def step_impl(context, bookTitle):
    assert bookTitle in context.carturesti_search.get_title_text(), f"error:expected title:{bookTitle},actual title:{context.carturesti_search.get_title_text()}"