from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasePageLocators



class MainPage(BasePage):

    def open_drop_list(self):
        drop_list_button = self.browser.find_element(*BasePageLocators.DROPDOWN_BASKET_BUTTON)
        drop_list_button.click()

    def should_be_basket_drop_list(self):
        assert self.is_usable(*BasePageLocators.DROPDOWN_BASKET_LIST), \
            "There is no dropdown list for using"

    def search_something(self, title):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(title)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_button.click()

    def search_result_should_be_correct(self, title):
        search_result = self.browser.find_element(*BasePageLocators.SEARCH_RESULT_TITLE)
        search_result = search_result.get_attribute("title")
        assert title in search_result, "Search result is not correct"

    def search_result_should_be(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_RESULT_BODY), \
            "There is no search result, but it should be!"

    def search_result_should_not_be(self):
        assert self.is_not_element_present(*BasePageLocators.SEARCH_RESULT_BODY), \
            "There is search result, but it shouldn't be!"
