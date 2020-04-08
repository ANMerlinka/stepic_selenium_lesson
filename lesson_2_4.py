# Task 2 - ждем нужный текст на странице и потом нажимаем кнопку
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
#

import math
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try: 
    link="http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollBy(0, 300);")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)

    print(y)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button1 = browser.find_element_by_id("solve")
    button1.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()