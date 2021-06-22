import pytest
import math
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import random
import string



class TestProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    @pytest.mark.parametrize('promo_offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                             pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):

        page = ProductPage(browser, self.link + promo_offer)
        page.open()
        page.press_buy_button()
        page.solve_quiz_and_get_code()
        page.should_be_correct_succes_msg()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.press_buy_button()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.press_buy_button()
        page.should_be_dissapeared_succes_message()

    @pytest.mark.login
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.login
    def test_guest_can_go_to_login_page_from_product_page(self, browser):

        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.basket
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):

        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items()
        basket_page.should_be_no_items_msg()

@pytest.mark.user_test
class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        mail = page.mail_generator(9) + "@gmail.com"
        password = "aksdjkajdkajkjdkajkdjajk11"
        page.register_new_user(mail, password)
        page.should_be_authorized_user()



    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.press_buy_button()
        page.should_be_correct_succes_msg()






















