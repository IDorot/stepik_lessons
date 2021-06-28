import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

#DATA
link = "http://selenium1py.pythonanywhere.com/"
item_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
global title #Знаю, что плохо так делать, но и писать отдельную фикстуру в conftest не хотелось.


# DATA
@pytest.fixture(scope="function", autouse="True")
def setup( browser):
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_basket_items()
    product_page = ProductPage(browser, item_link)
    product_page.open()
    product_page.press_buy_button() # Покупаем книжку чтобы в ожидаемом выпадающем списке было что-то. Вдруг он без этого не активируется
    global title
    title = product_page.take_title_name() # Вытягиваем название книги прямо из её странички

@pytest.mark.personal_tests
class TestMainPageBasketDropdownList:

    @pytest.mark.xfail
    def test_guest_can_see_basket_dropdown_list(self, browser):
        #Arrange
        page = MainPage(browser, link)
        page.open()
        #Act
        page.open_drop_list()
        #Assert
        page.should_be_basket_drop_list()

class TestMainPageSearch:

    def test_guest_can_search_full_valid_title_name(self, browser):
        #Arrange
        page = MainPage(browser, link)
        page.open()
        #Act
        page.search_something(title)
        #Assert
        page.search_result_should_be() # Чисто для логгирования, что поиск прошел и что-то нашел.
        page.search_result_should_be_correct(title)
