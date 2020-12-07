import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')

    x_elem = browser.find_element_by_id('treasure')
    x = calc(int(x_elem.get_attribute('valuex')))
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()
    print(browser.switch_to_alert().text)


    