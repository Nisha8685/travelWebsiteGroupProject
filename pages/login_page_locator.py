from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_TEXT_BX = (By.NAME,"userName")
    PASSWORD_TEXT_BX = (By.NAME, "password")
    LOGIN_SUBMIT_BTN = (By.NAME, "submit")