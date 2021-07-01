import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators
from decimal import Decimal


class BasketPage(BasePage):

    def set_quantity(self, N):
        quantity_field = self.browser.find_element(*BasketPageLocators.BASKET_QUANTITY)
        print("Found Quantity field")
        quantity_field.clear()
        print("Quantity field cleared")
        print(f"PCS =  {N}")
        quantity_field.send_keys(N)
        print("Sent input")
        quantity_update_button = self.browser.find_element(*BasketPageLocators.BASKET_QUANTITY_UPDATE)
        quantity_update_button.click()

    def total_should_be_correct(self, N):
        price = self.browser.find_element(*BasketPageLocators.BASKET_ITEM_PRICE).text

        print("Got Price's value")
        total = self.browser.find_element(*BasketPageLocators.BASKET_TOTAL).text
        print("Got Total's value")
        price_decimal = Decimal(price.strip("£"))
        discount_offer = [price_decimal, price_decimal * 2, price_decimal * 3]  # Массив с переменной содержащей скидку.
        total_er = Decimal(price.strip("£")) * N
        total_ar = Decimal(total.strip("£"))

        if N > 2:
            total_er = total_er - Decimal(discount_offer[
                                              int(N / 3 - 1)])  # Каждая третья книжка  - бесплатна, поэтому вычитается из общего чека. 6 книжек - 2 бесплатных и т.д.

        print(f"+Total EXPECTED {total_er}")
        print(f"+Total ACTUAL {total_ar}")

        assert '{0:.3g}'.format(total_er) == '{0:.3g}'.format(total_ar), "Total or price is not correct!"

    def press_remove_button(self):
        remove_button  = self.browser.find_element(*BasketPageLocators.BASKET_QUANTITY_REMOVE)
        remove_button.click()

    def press_have_code_button(self):
        vaucher_button  = self.browser.find_element(*BasketPageLocators.BASKET_I_HAVE_A_VOUCHER_BUTTON)
        vaucher_button.click()

    def should_not_be_basket_items(self):
       assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
       "There are some basket's items, but  they shouldn't be!"


    def should_be_vaucher_form(self):
        assert self.is_usable(*BasketPageLocators.BASKET_VAUCHER_FORM), \
        "Vaucher form is not found, but it should be here"





