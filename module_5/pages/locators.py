from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_USERNAME_FIELD = (By.NAME, "login-username")
    LOGIN_PASSWORD_FIELD = (By.NAME, "login-password")
    REGISTER_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTER_PASSWORD_FIELD = (By.NAME,"registration-password1")
    REGISTER_REPASSWORD_FIELD = (By.NAME,"registration-password2")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCES_MSG = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) .alertinner strong")
    BASKET_MSG = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs .btn-group > a.btn.btn-default")
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_NO_ITEMS_MSG = (By.CSS_SELECTOR,"#content_inner p")






