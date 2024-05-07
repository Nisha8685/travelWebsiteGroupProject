from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from resources.constans import TEST_SITE_URL
from pages.login_page import LoginPage
from pages.login_success_page import LoginSuccessPage
from pages.Signoff_page import SignoffPage
from pages.signoff_success_page import SignoffSuccessPage


class TestLogin:

    # Test Case 1 - Registering the user
    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.click_on_register_btn()
        register_page = RegisterPage(driver)
        register_page.register_new_user(username_password[0], username_password[1])
        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert "Note: Your user name is dan25." == register_success_lbl, "Test Case 1 Failed due to username assertion error"

    # Test Case 2

    def test_login_user(self, driver, username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        login_page.login_user(username_password[0], username_password[1])
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert "Login Successfully" == login_success_lbl, "Test case 2 failed"

    # Test Case 3

    def test_signoff_user(self, driver):
        signoff_page = SignoffPage(driver)
        signoff_page.signoff_user()
        signoff_success_page = SignoffSuccessPage(driver)
        signoff_success_txt = signoff_success_page.get_signoff_success_btn()
        assert "SIGN-ON" == signoff_success_txt, "Test case 2 failed"
