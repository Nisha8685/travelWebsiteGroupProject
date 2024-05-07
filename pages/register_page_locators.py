from selenium.webdriver.common.by import By


class RegisterPageLocators:
    EMAIL_TEXT_BX = (By.ID,"email")
    PASSWORD_TEXT_BX = (By.NAME, "password")
    CONFIRM_PW_TXT_BX = (By.NAME, "confirmPassword")
    REGISTER_SUBMIT_BTN = (By.NAME, "submit")