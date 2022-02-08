from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(x + y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_css_selector("#num1")
    first = int(first.text)
    second = browser.find_element_by_css_selector("#num2")
    second = int(second.text)
    y = calc(first, second)

    select = Select(browser.find_element_by_tag_name("#dropdown"))
    select.select_by_visible_text(y)

    element = browser.find_element_by_css_selector('[class="btn btn-default"]')
    element.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
browser.quit()

