import pytest
import math
from selenium import webdriver
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.press_buy_button()
        page.solve_quiz_and_get_code()
        page.should_be_correct_succes_msg()









