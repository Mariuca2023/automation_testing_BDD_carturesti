from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CarturestiLoginPage(BasePage):

    LOGIN_PAGE_URL = "https://carturesti.ro/"

    EMAIL_INPUT = (By.ID, "loginform-email")
    PASSWORD_INPUT = (By.ID, "loginform-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'form[id="modalLoginForm"] button[type="submit"]')
    FLASH_CONTAINER = (By.CLASS_NAME, "help-block")
    COOKIES_BUTTON = (By.XPATH, '//a[contains(text(),"Permite toate")]')

    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)
        self.driver.find_element(*self.COOKIES_BUTTON).click()

    # this method puts the email
    def set_email(self, email):
        #self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.type(self.EMAIL_INPUT, email)

    # this method puts the password
    def set_password(self, password):
        #self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    # this method checks if the banner is displayed
    # same element is used for both scenarios positive and negative
    def is_message_displayed(self):
        #return self.driver.find_element(*self.FLASH_CONTAINER).is_displayed()
        return self.wait_for_element(self.FLASH_CONTAINER, 6).is_displayed()

    def get_message_text(self):
        #return self.driver.find_element(self.FLASH_CONTAINER).text
        return self.get_element_text(self.FLASH_CONTAINER)
