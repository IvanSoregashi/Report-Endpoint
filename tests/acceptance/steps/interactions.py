from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from behave import *

use_step_matcher('re')


@given('I am on input page')
def step_impl(context):
    chrome_service = Service(executable_path='chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get('http://127.0.0.1:5000/input')
