from pages.base_page import BasePage
from pages.Signoff_page_locator import SignoffPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class SignoffPage(BasePage):


    def signoff_user(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,SignoffPageLocators.SIGNOFF_BTN)
        self.find_element(SignoffPageLocators.SIGNOFF_BTN).click()

