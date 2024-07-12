from driver import Driver
from pages.login_page import LoginPage
from pages.carturesti_search_page import CarturestiSearchPage
from pages.emag_search_page import EmagSearchPage
from pages.carturesti_login_page import CarturestiLoginPage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.carturesti_search = CarturestiSearchPage()
    context.emag_search = EmagSearchPage()
    context.carturesti_login = CarturestiLoginPage()

def after_all(context):
    context.browser.close()

