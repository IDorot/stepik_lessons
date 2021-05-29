
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_reg():
    try:
        #Data
        login_mail_name = "registration-email"
        login_pass_name = "registration-password1"
        login_repeat_pass_name = "registration-password2"
        button_name = "registration_submit"
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        succes_link = "http://selenium1py.pythonanywhere.com/ru/"
        login_mail = "samplebamble643@yandex.ru"
        password = "WoobWeebBeep11"

        #Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        mail = browser.find_element_by_name(login_mail_name)
        mail.clear()
        password_one = browser.find_element_by_name(login_pass_name)
        password_one.clear()
        password_two = browser.find_element_by_name(login_repeat_pass_name)
        password_two.clear()

        #Act
        mail.send_keys(login_mail)
        password_one.send_keys(password)
        password_two.send_keys(password)
        button = browser.find_element_by_name(button_name)
        button.click()

        #Assert
        assert  succes_link == browser.current_url, \
        "We've failed the registration"

    finally:
        browser.quit()
test_reg()


