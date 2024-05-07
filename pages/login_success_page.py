from pages.base_page import BasePage
from pages.login_success_page_locator import LoginSuccessPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class LoginSuccessPage(BasePage):

    def get_login_success_label(self):
        return self.find_element(LoginSuccessPageLocators.LOGIN_SUCCESS_LBL).text