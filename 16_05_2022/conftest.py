import pytest
from selenium import  webdriver
@pytest.fixture(autouse=True,scope="module")
def setup(browser,request):
    print(f"invoke {browser}")
    d = webdriver.Chrome()
    d.get("https://www.google.com")
    request.module.driver=d
    print("login")
    yield
    print("log out")
    print("clean")
    d.close()

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")

