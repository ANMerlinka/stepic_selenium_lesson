import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="None",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(30)
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser, request):
    language = request.config.getoption("language")
    #print(language)
    if language != "None":   
        link = "http://selenium1py.pythonanywhere.com/" + language + "/"
        #print(link)
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
    
    else:
        raise pytest.UsageError("--language should be")
    