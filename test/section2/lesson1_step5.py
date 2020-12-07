from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/math.html')
    x = int(browser.find_element_by_id('input_value').text)
    ans_input = browser.find_element_by_id('answer')
    ans_input.send_keys(calc(x))

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(10)



