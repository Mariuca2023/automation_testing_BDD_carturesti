from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import Driver

# BasePage -                        cea mai comuna
#    |                  |
# SamePage1            SamePage2
#   |     |
#  SM1.1 - SM1.2


class BasePage(Driver):

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element(locator, 6).text

    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))