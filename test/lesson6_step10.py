from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/registration2.html")
    elements = browser.find_elements_by_tag_name('.first_block input')
    for elem in elements:
        elem.send_keys('gg')
    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(5)
    assert browser.find_element_by_tag_name('h1').text == "Congratulations! You have successfully registered!"
    time.sleep(5)
    browser.quit()
