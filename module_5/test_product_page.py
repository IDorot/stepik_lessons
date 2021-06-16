import pytest
import math
from selenium import webdriver
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="

class TestProductPage:
    @pytest.mark.parametrize('promo_offer',["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("Bugged offer", marks = pytest.mark.xfail),"offer8","offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        page = ProductPage(browser, link+promo_offer)
        page.open()
        page.press_buy_button()
        page.solve_quiz_and_get_code()
        page.should_be_correct_succes_msg()









