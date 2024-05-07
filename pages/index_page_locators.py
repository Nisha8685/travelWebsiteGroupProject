from selenium.webdriver.common.by import By


class IndexPageLocators:
    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='REGISTER']")
    USER_NAME_TXTBX = (By.NAME, "userName")
    PASSWORD_TXTBX = (By.NAME, "password")
    LOGIN_SUBMIT_BTN = (By.NAME, "submit")