import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def press_review_button(self):
        review_button = self.browser.find_element(*ProductPageLocators.REVIEW_BUTTON)
        review_button.click()

    def should_be_review_form(self):
        assert self.is_element_present(*ProductPageLocators.REVIEW_FORM), \
        "There is no review form"

    def press_buy_button(self):
        buy_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        buy_button.click()

    def take_title_name(self):
        title_name = self.browser.find_element(*ProductPageLocators.TITLE_NAME).text
        return title_name

    def press_first_star_rating_bar(self):
        star = self.browser.find_element(*ProductPageLocators.RATING_BAR_SELECT_1ST_OPTION)
        star.click()

    def first_star_rating_bar_should_be_selected(self):
        assert self.is_element_selected(*ProductPageLocators.RATING_BAR_SELECT_1ST_OPTION), \
        "Star isn't selected!"













