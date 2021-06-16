from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), "Login nickname is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD), "Register Email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_REPASSWORD_FIELD), "Register second password is not presented"
