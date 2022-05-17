import pytest
from selenium import  webdriver

@pytest.fixture
def setup(request,browser,url):
    print("in setup function")
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="edge":
        driver = webdriver.Edge()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="ie":
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()


    driver.implicitly_wait(10)
    driver.get(url)
    request.module.driver=driver
    print("login")
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def url(request):
    return request.config.getoption("--url")
