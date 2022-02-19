import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1"
"https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    pole = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
    answer = math.log(int(time.time()))
    pole.send_keys(answer)
    button = browser.find_element_by_css_selector('[class="submit-submission"]')
    button.click()
    feedback = browser.find_element_by_css_selector('[class="smart-hints__hint"]')
    feedback = feedback.text
    assert feedback == "Correct!", feedback
    