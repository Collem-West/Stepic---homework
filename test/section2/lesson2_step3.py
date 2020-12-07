from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    num_1 = browser.find_element_by_css_selector('h2 > #num1').text
    num_2 = browser.find_element_by_css_selector('h2 > #num2').text
    summ = int(num_1) + int(num_2)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(summ))
    browser.find_element_by_css_selector('button.btn').click()
    print(browser.switch_to_alert().text)