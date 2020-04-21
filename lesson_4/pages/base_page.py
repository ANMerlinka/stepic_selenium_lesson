from selenium.common.exceptions import NoSuchElementException

class BasePage():
    #добавим конструктор — метод, который вызывается, когда мы создаем объект.
    #В него в качестве параметров мы передаем экземпляр драйвера и url адрес. 
    def __init__(self, browser, url):       
        self.browser = browser
        self.url = url
    
    #Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)

    # неявного ожидания со значением по умолчанию в 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True