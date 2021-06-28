import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def press_buy_button(self):
        buy_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        buy_button.click()

    def take_title_name(self):
        title_name = self.browser.find_element(*ProductPageLocators.TITLE_NAME).text
        return title_name












