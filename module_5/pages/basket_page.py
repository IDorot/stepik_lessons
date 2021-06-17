import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "There is some items but it should be empty"

    def should_be_no_items_msg(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_NO_ITEMS_MSG).text == "Your basket is empty. Continue shopping", \
        "There is incorrect emptinesses message"



