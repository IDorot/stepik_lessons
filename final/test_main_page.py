import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

# DATA
link = "http://selenium1py.pythonanywhere.com/"
item_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
global title  # Знаю, что плохо так делать, но и писать отдельную фикстуру в conftest не хотелось.
global part_title
invalid_title = "Конституция Российской Федерации"


@pytest.fixture(scope="function", autouse="True")
def setup(browser):
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_basket_items()
    product_page = ProductPage(browser, item_link)
    product_page.open()
    product_page.press_buy_button()  # Покупаем книжку чтобы в ожидаемом выпадающем списке было что-то. Вдруг он без этого не активируется
    global title
    global part_title
    title = product_page.take_title_name()  # Вытягиваем название книги прямо из её странички
    part_title = title.strip("foot")  # А здесь удаляем часть названия книги


@pytest.mark.personal_tests
class TestMainPageBasketDropdownList:

    @pytest.mark.xfail
    def test_guest_can_see_basket_dropdown_list(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.open_drop_list()
        # Assert
        page.should_be_basket_drop_list()


@pytest.mark.personal_tests
class TestMainPageSearch:

    def test_guest_can_search_full_valid_title_name(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.search_something(title)
        # Assert
        page.search_result_should_be()  # Чисто для логгирования, что поиск прошел и что-то нашел.
        page.search_result_should_be_correct(title)

    @pytest.mark.xfail
    def test_guest_can_search_partial_valid_title_name(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.search_something(part_title)
        # Assert
        page.search_result_should_be()  # Поиск прошел и что-то нашел.
        page.search_result_should_be_correct(part_title)

    def test_guest_cannot_search_invalid_title_name(self, browser):  # Отрицательный тест
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.search_something(invalid_title)
        # Assert
        page.search_result_should_not_be()

