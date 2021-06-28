import pytest
from selenium import webdriver
from .pages.product_page import ProductPage

# DATA
link = "http://selenium1py.pythonanywhere.com/catalogue/the-age-of-the-pussyfoot_89/"


class TestProductPage:
   def test_guest_can_open_review_form(self, browser):
      # Arrange
      page = ProductPage(browser, link)
      page.open()
      # Act
      page.press_review_button()
      # Assert
      page.should_be_review_form()

   @pytest.mark.xfail
   def test_guest_can_use_rating_bar(self, browser):
      # Arrange
      page = ProductPage(browser, link)
      page.open()
      # Act
      page.press_review_button()
      page.press_first_star_rating_bar()
      # Assert
      page.first_star_rating_bar_should_be_selected()
