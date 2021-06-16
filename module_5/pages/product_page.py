import pytest
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators




class ProductPage(BasePage):
    def press_buy_button(self):
        buy_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        buy_button.click()
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def should_be_correct_succes_msg (self):
        succes_msg = self.browser.find_element(*ProductPageLocators.SUCCES_MSG).text
        basket_msg = self.browser.find_element(*ProductPageLocators.BASKET_MSG).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_name_ex = self.browser.find_element(*ProductPageLocators.BOOK_NAME_EX).text
        book_price_ex = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_EX).text
        assert book_name_ex in succes_msg, "Incorrect succes message"
        assert book_price_ex in basket_msg, "Incorrect price value in succes message"

    def should_be_correct_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert book_price_ex in basket_total, "Incorrect value of basket"





