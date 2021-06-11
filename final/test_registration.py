from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random
import string
import pytest

# Data
def mail_generator(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))

login_mail = mail_generator(8) + "@gmail.com"
login_mail_name = "registration-email"
login_pass_name = "registration-password1"
login_repeat_pass_name = "registration-password2"
button_name = "registration_submit"
link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
succes_text = "Спасибо за регистрацию!"
password = "WoobWeebBeep11"

# Arrange
# Поставил здесь Arrange, поскольку уже с этого момента описываю все подготовки


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser...")
    browser.quit()

def test_reg(browser):
    login_mail = mail_generator(8) + "@gmail.com"
    browser.get(link)
    mail = browser.find_element_by_name(login_mail_name)
    mail.clear()
    password_one = browser.find_element_by_name(login_pass_name)
    password_one.clear()
    password_two = browser.find_element_by_name(login_repeat_pass_name)
    password_two.clear()

    # Act
    mail.send_keys(login_mail)
    password_one.send_keys(password)
    password_two.send_keys(password)
    button = browser.find_element_by_name(button_name)
    button.click()
    message = browser.find_element_by_css_selector(".alertinner.wicon")


    # Assert
    assert succes_text == message.text, \
        "We've failed the registration"

