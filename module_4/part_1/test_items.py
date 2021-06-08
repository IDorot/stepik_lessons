import pytest
from selenium import webdriver

#Data
link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
correct_button_text = {
    'ru': 'Добавить в корзину',
    'en-GB': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier',
}

def test_ui_language(browser, language):
    #Arrange
    browser.get(link)

    #Act
    buy_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    page_lang = browser.find_element_by_class_name("no-js").get_attribute("lang")

    #Assert
    #lower() используется т.к. в en-GB версии страницы аттрибут lang равен "en-gb", из-за чего тест может упасть
    assert buy_button.text == correct_button_text[language]
    assert page_lang == language.lower()
