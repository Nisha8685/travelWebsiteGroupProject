from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def explicitly_wait_and_find_element(self, interval, locator):
        return WebDriverWait(self.driver, interval).until(
            expected_conditions.presence_of_element_located(locator))

    def navigate_to(self,url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)