from selenium.webdriver.common.by import By
from behave import *

use_step_matcher('re')


@when("I input '(.*)' as '(.*)'")
def step_impl(context, field_id, value):
    field = context.driver.find_element(By.ID, field_id)
    field.send_keys(value)


@when("I click '(.*)'")
def step_impl(context, button_id):
    button = context.driver.find_element(By.ID, button_id)
    button.click()
