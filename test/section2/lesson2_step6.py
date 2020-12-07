import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    x_elem = browser.find_element_by_id('input_value').text
    x = calc(int(x_elem))
    ans_input = browser.find_element_by_id('answer')
    ans_input.send_keys(x)
    button = browser.find_element_by_css_selector('button.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    button.click()
    print(browser.switch_to_alert().text)
