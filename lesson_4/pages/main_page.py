#импорт базового класса BasePage
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 
    
    #def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    #def should_be_login_link(self):
        #assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
