from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class CarturestiLoginPage(BasePage):

    LOGIN_PAGE_URL = "https://carturesti.ro/"

    EMAIL_INPUT = (By.ID, "loginform-email")
    PASSWORD_INPUT = (By.ID, "loginform-password")
    LOGIN_BUTTON = (By.XPATH,"/html/body/div[4]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[3]/button")
    AUTENTIFICARE_BUTTON = (By.CSS_SELECTOR, 'form[id="modalLoginForm"] button[type="submit"]')
    # FLASH_CONTAINER = (By.CLASS_NAME, "help-block")
    COOKIES_BUTTON = (By.XPATH, '//a[contains(text(),"Permite toate")]')
    UTILIZATOR_EXISTENT = (By.ID, "loginTrigger")


    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)
        # self.driver.find_element(*self.COOKIES_BUTTON).click()

    def click_allow_cookies(self):
        self.wait_for_element(self.COOKIES_BUTTON, 10).is_displayed()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.COOKIES_BUTTON))
        self.click(self.COOKIES_BUTTON)

    def click_login(self):
        #self.wait_for_element(self.LOGIN_BUTTON, 10).is_displayed()
        self.wait_for_element(self.LOGIN_BUTTON, 10).is_displayed()
        self.click(self.LOGIN_BUTTON)

    def click_autentificare(self):
        sleep(10)
        self.wait_for_element(self.AUTENTIFICARE_BUTTON, 10).is_displayed()
        self.click(self.AUTENTIFICARE_BUTTON)

    def click_utilizator(self):
        self.wait_for_element(self.UTILIZATOR_EXISTENT, 10).is_displayed()
        self.click(self.UTILIZATOR_EXISTENT)

    # this method puts the email
    def set_email(self, email):
        #self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.EMAIL_INPUT, 10).is_displayed()
        self.type(self.EMAIL_INPUT, email)

    # this method puts the password
    def set_password(self, password):
        #self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.PASSWORD_INPUT, 10).is_displayed()
        self.type(self.PASSWORD_INPUT, password)

    def check_url(self, url):
        print(self.driver.current_url)
        assert url==self.driver.current_url

    # this method checks if the banner is displayed
    # same element is used for both scenarios positive and negative
    # def is_message_displayed(self):
    #     #return self.driver.find_element(*self.FLASH_CONTAINER).is_displayed()
    #     return self.wait_for_element(self.FLASH_CONTAINER, 6).is_displayed()

    # def get_message_text(self):
    #     #return self.driver.find_element(self.FLASH_CONTAINER).text
    #     return self.get_element_text(self.FLASH_CONTAINER)
