import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_addition_book(browser):
    # browser.implicitly_wait(5)
    browser.get(link)
    add_button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    add_button.click()
    basket_view = browser.find_element_by_css_selector('.alert.alert-safe.alert-noicon.alert-info.fade.in div a:first-child')
    basket_view.click()
    book = browser.find_element_by_css_selector('.basket-items .col-sm-4 a')
    book = book.text
    assert book == "Coders at Work"
    print(book)

