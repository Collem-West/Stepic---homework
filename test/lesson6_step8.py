from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/find_xpath_form')
    browser.find_element_by_tag_name('input').send_keys('Ivan')
    browser.find_element_by_name('last_name').send_keys('Petrov')
    browser.find_element_by_class_name('city').send_keys('Smolensk')
    browser.find_element_by_id('country').send_keys('Russia')
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    print(browser.switch_to_alert().text)
    browser.quit()