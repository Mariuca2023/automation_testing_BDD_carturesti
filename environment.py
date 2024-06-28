from driver import Driver
from pages.login_page import LoginPage
from pages.carturesti_search_page import CarturestiSearchPage
from pages.emag_search_page import EmagSearchPage

def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.carturesti_search = CarturestiSearchPage()
    context.emag_search = EmagSearchPage()

def after_all(context):
    context.browser.close()

