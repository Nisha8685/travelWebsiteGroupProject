from pages.base_page import BasePage
from pages.signoff_success_page_locator import SignoffSuccessPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class SignoffSuccessPage(BasePage):

    def get_signoff_success_btn(self):
        return self.find_element(SignoffSuccessPageLocators.SIGNOFF_SUCCESS_BTN).text
