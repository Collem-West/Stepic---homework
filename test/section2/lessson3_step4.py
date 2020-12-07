import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element_by_css_selector('button.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    value = browser.find_element_by_id('input_value').text
    x = calc(value)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_css_selector('button.btn').click()
    print(browser.switch_to.alert.text.split(': ')[1])
