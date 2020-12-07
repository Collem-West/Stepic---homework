import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as br:
    br.get(link)
    check_price = WebDriverWait(br, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    br.find_element_by_css_selector('button#book').click()
    value = br.find_element_by_id('input_value').text
    x = calc(value)
    br.find_element_by_id('answer').send_keys(x)
    br.find_element_by_css_selector('button#solve').click()
    print(br.switch_to.alert.text.split(': ')[1])