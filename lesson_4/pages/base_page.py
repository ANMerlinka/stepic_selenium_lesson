class BasePage():
    #добавим конструктор — метод, который вызывается, когда мы создаем объект.
    #В него в качестве параметров мы передаем экземпляр драйвера и url адрес. 
    def __init__(self, browser, url):       
        self.browser = browser
        self.url = url
    
    #Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)