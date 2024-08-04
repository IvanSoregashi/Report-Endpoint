from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from behave import *

from tests.acceptance.page_model.base_page import InputPage, HomePage

use_step_matcher('re')


def get_chromedriver():
    chrome_service = Service(
        executable_path=r'C:\Users\Shyryaev\PycharmProjects\FlaskEndpointAutotesting\tests\acceptance\steps\chromedriver.exe')
    chrome_options = Options()
    return webdriver.Chrome(service=chrome_service, options=chrome_options)


@given("I am on 'input' page")
def step_impl(context):
    context.driver = get_chromedriver()
    page = InputPage(context.driver)
    context.driver.get(page.url)


@given("I am on 'home' page")
def step_impl(context):
    context.driver = get_chromedriver()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@then("I am on 'home' page")
def step_impl(context):
    assert context.driver.current_url == HomePage(context.driver).url

@then("Transactions are shown on the page")
def step_impl(context):
    page = HomePage(context.driver)
    assert page.content.is_displayed()
