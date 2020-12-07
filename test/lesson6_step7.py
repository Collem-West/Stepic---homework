from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/huge_form.html')
    elems = browser.find_elements_by_tag_name('input')
    for elem in elems:
        elem.send_keys('GG')
    browser.find_element_by_css_selector('button.btn').click()
    print(browser.switch_to_alert().text)
    browser.quit()