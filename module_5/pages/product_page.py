import pytest
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_name == succes_msg, "Incorrect succes message"
        assert book_price == basket_msg, "Incorrect price value in succes message"
        print(f"\n{book_name} = {succes_msg} ")
        print(f"{book_price} = {basket_msg}")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MSG), \
            "Success message is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.BASKET_MSG), \
            "Success basket's message is presented, but should not be"

    def should_be_dissapeared_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MSG), \
            "Succes message doesn't dissappear"
        assert self.is_disappeared(*ProductPageLocators.BASKET_MSG), \
            "Succes basket's message doesn't dissappear"










