from selenium import webdriver
import time
import math
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys("name")
    browser.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys("last name")
    browser.find_element_by_css_selector('[placeholder="Enter email"]').send_keys("Email")
    browser.find_element_by_css_selector('#file').send_keys(file_path)
    button = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
browser.quit()