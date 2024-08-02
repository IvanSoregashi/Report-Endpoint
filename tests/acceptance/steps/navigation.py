from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from behave import *

use_step_matcher('re')


@given("I am on 'input' page")
def step_impl(context):
    chrome_service = Service(
        executable_path=r'C:\Users\Shyryaev\PycharmProjects\FlaskEndpointAutotesting\tests\acceptance\steps\chromedriver.exe')
    chrome_options = Options()
    context.browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    context.browser.get("http://127.0.0.1:5000/input")


@then("I am on 'home' page")
def step_impl(context):
    expected_url = "http://127.0.0.1:5000/"
    print(context.browser.current_url)
    assert context.browser.current_url == expected_url
