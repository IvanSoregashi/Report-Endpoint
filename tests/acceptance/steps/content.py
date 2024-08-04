from behave import *
from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@step("Title '(.*)' is shown on the page")
def step_impl(context, title):
    page = BasePage(context.driver)
    assert page.title.is_displayed()
    assert page.title.text == title

@step('Transactions are shown on the page')
def step_impl(context):
    pass