from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    FLASH_CONTAINER = (By.ID, "flash-messages")

    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

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

