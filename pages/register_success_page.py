from pages.base_page import BasePage
from pages.register_success_page_locators import RegisterSuccessPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class RegisterSuccessPage(BasePage):

    def get_register_success_label(self):
        return self.find_element(RegisterSuccessPageLocators.RESIGSTER_SUCCESS_LBL).text
