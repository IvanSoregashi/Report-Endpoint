from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.page_locators import BasePageLocators

use_step_matcher('re')


@given("I wait for 'container' to load")
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.CONTAINER)
    )
