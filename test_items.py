import pytest
from selenium import webdriver
import time


def test_availability_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    bs = browser.find_elements_by_css_selector("#add_to_basket_form button[type=submit]")
    c = len(bs)
    assert c == 1, "Button 'Add to basket' not found"
