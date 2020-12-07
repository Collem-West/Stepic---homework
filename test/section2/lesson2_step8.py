import os
from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
link = 'http://suninjuly.github.io/file_input.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    f_name = browser.find_element_by_name('firstname')
    f_name.send_keys('a')
    l_name = browser.find_element_by_name('lastname')
    l_name.send_keys('aa')
    email = browser.find_element_by_name('email')
    email.send_keys('aaa')
    file_input = browser.find_element_by_css_selector('input[type="file"]')
    file_input.send_keys(file_path)
    browser.find_element_by_css_selector('button.btn').click()
    print(browser.switch_to_alert().text)
