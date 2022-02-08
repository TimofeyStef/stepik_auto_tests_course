from selenium import webdriver
import time
import math

def result(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value")
    x = int(x.text)
    y = result(x)

    button = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector('#robotsRule').click()
    # button = browser.find_element_by_css_selector('[class="btn btn-default"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
browser.quit()