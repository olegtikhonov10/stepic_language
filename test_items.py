from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(6)
    browser.find_element_by_css_selector(".btn-add-to-basket")







