from selenium import webdriver
import time
import math
import os

def result(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[class="btn btn-primary"]').click()
    alert = browser.switch_to.alert
    alert.accept()
    element = browser.find_element_by_css_selector("#input_value")
    x = int(element.text)
    x = result(x)
    browser.find_element_by_css_selector('#answer').send_keys(x)
    browser.find_element_by_css_selector('[class="btn btn-primary"]').click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
browser.quit()