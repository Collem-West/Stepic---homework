import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as br:
    br.get(link)
    br.find_element_by_css_selector('button.trollface').click()
    new_window = br.window_handles[1]
    br.switch_to.window(new_window)
    value = br.find_element_by_id('input_value').text
    x = calc(value)
    br.find_element_by_id('answer').send_keys(x)
    br.find_element_by_css_selector('button.btn').click()
    print(br.switch_to.alert.text.split(': ')[1])
    