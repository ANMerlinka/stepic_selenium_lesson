import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language. Default language - en")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(language)
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser 
    time.sleep(15)
    print("\nquit browser..")
    browser.quit()
