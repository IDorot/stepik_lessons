from selenium.webdriver.common.by import By



class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")
    TITLE_NAME = (By.CSS_SELECTOR,".col-sm-6.product_main h1")


class BasePageLocators():
    DROPDOWN_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.dropdown-toggle")
    DROPDOWN_BASKET_LIST = (By.CSS_SELECTOR, ".dropdown-menu.pull-right .basket-mini-item.list-unstyled")
    SEARCH_BUTTON = (By.CSS_SELECTOR,".navbar-form.navbar-right [value='Search']")
    SEARCH_FIELD = (By.CSS_SELECTOR,"[type='search']")
    SEARCH_RESULT_TITLE = (By.CSS_SELECTOR,".col-xs-6.col-sm-4.col-md-3.col-lg-3 h3 a")
    SEARCH_RESULT_BODY = (By.CSS_SELECTOR,".col-xs-6.col-sm-4.col-md-3.col-lg-3")







class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_QUANTITY = (By.CSS_SELECTOR, "[name='form-0-quantity']")
    BASKET_QUANTITY_UPDATE = (By.CSS_SELECTOR, ".input-group-btn > .btn.btn-default")
    BASKET_QUANTITY_REMOVE = (By.CSS_SELECTOR,"[data-behaviours='remove']")
    BASKET_ITEM_PRICE = (By.CSS_SELECTOR,".basket-items .col-sm-1 .price_color.align-right")
    BASKET_TOTAL = (By.CSS_SELECTOR,".total.align-right :nth-child(1)")
    BASKET_I_HAVE_A_VOUCHER_BUTTON = (By.CSS_SELECTOR,"#voucher_form_link .btn.btn-default.btn-full")
    BASKET_VAUCHER_FORM = (By.CSS_SELECTOR,"#voucher_form [name = code]")












