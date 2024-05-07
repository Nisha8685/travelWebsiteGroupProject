from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class LoginPage(BasePage):


    def login_user(self,user_name,password):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.USER_NAME_TXTBX)
        self.find_element(IndexPageLocators.USER_NAME_TXTBX).send_keys(user_name)
        self.find_element(IndexPageLocators.PASSWORD_TXTBX).send_keys(password)
        self.find_element(IndexPageLocators.LOGIN_SUBMIT_BTN).click()

