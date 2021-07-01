import pytest

from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

#DATA
link = "http://selenium1py.pythonanywhere.com/basket/"
item_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
list = [3,6,9] #Список для параметризированного теста, содержащий количество книг(пограничные значения)
@pytest.mark.personal_tests
class TestBasketQuantity:

    #DATA
    @pytest.fixture(scope="function", autouse = "True")
    def setup(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.should_not_be_basket_items()
        product_page = ProductPage(browser, item_link)
        product_page.open()
        product_page.press_buy_button()

    @pytest.mark.parametrize('pcs',list) #Проверяется расчёт чека корзины с валидными значениями количества книг от 1 до 12 включительно
    def test_guest_basket_calculation(self, browser,pcs):
        #Arrange
        page = BasketPage(browser, link)
        page.open()
        #Act
        page.set_quantity(pcs)
        #Assert
        page.total_should_be_correct(pcs)

    @pytest.mark.xfail
    def test_guest_can_remove_item_with_remove_button(self, browser):
        #Arrange
        page = BasketPage(browser, link)
        page.open()
        #Act
        page.press_remove_button()
        #Assert
        page.should_not_be_basket_items()

    def test_guest_can_remove_item_with_zero_quantity_and_update(self, browser): #Негативный тест
        #Arrange
        page = BasketPage(browser,link)
        page.open()
        #Act
        page.set_quantity(0)
        #Assert
        page.should_not_be_basket_items()

    @pytest.mark.xfail
    def test_guest_can_use_vaucher_code(self, browser):
        # Arrange
        page = BasketPage(browser, link)
        page.open()
        # Act
        page.press_have_code_button()
        #Assert
        page.should_be_vaucher_form()











