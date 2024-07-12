from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# mostenim clasa BasePage
class CarturestiSearchPage(BasePage):

    MAIN_URL = "https://carturesti.ro/"
    SEARCH_WITH_PAGE_URL = "https://carturesti.ro/product/search/"

    SEARCH_INPUT_SELECTOR = (By.ID, "search-input")
    TITLE_SELECTOR = (By.CSS_SELECTOR, "h5.md-title")
    MAGNIFIER_SELECTOR = (By.CSS_SELECTOR, 'div.search-container[role="button"]')
    # when you are on the page 10, rest of the elements for page number have @class='ng-scope'
    # this is why, the current page element is the only one in DOM that has @class='ng-scope active'
    CURRENT_PAGE_SELECTOR = (By.XPATH, "//li[@data-ng-repeat='page in pager.pages' and @class='ng-scope active']")

    #9781449340377


    def navigate_to_page(self):
        self.driver.get(self.MAIN_URL)

    # construiesc URL
    # when you try to search a specific keyword from the main page,
    # the URL looks like this: https://carturesti.ro/product/search/vinyl?page=109
    # this is why when you try to navigate directly to a specific page
    # you can "hack" the steps and go directly to the URL:
    def navigate_to_page_with_key_word(self, keyword, page):
    # declar o variabila care se va numi
        URL = self.SEARCH_WITH_PAGE_URL + keyword + "?page=" + page
        self.driver.get(URL)

    def click_on_search_button(self):
        # I take click method from BasePage
        # click method accept a tuple (tuplu) -> see base_page.py
        self.click(self.SEARCH_INPUT_SELECTOR)

    def click_on_magnifier_button(self):
        # self.click(self.MAGNIFIER_SELECTOR)
        self.driver.find_element(*self.SEARCH_INPUT_SELECTOR).send_keys(Keys.ENTER)

    def type_anything_on_search(self, text_to_search):
        self.type(self.SEARCH_INPUT_SELECTOR, text_to_search)

    # get the title from the respective book
    def get_title_text(self):
        return self.get_element_text(self.TITLE_SELECTOR)

    def get_current_page_text(self):
        return self.get_element_text(self.CURRENT_PAGE_SELECTOR)