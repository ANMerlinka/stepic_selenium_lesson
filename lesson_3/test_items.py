import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    
    #страница товара на сайте содержит кнопку добавления в корзину
    cl = (By.CSS_SELECTOR, 'button.btn.btn-lg')
    element = WebDriverWait(browser, 30).until(EC.visibility_of_element_located(cl), "No button on page")
    assert element
    