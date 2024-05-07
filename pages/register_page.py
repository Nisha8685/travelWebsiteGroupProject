from pages.base_page import BasePage
from pages.register_page_locators import RegisterPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class RegisterPage(BasePage):

    def register_new_user(self,user_name,password):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,RegisterPageLocators.EMAIL_TEXT_BX)
        self.find_element(RegisterPageLocators.EMAIL_TEXT_BX).send_keys(user_name)
        self.find_element(RegisterPageLocators.PASSWORD_TEXT_BX).send_keys(password)
        self.find_element(RegisterPageLocators.CONFIRM_PW_TXT_BX).send_keys(password)
        self.find_element(RegisterPageLocators.REGISTER_SUBMIT_BTN).click()


