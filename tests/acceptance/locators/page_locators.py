from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'
    CONTAINER = By.ID, 'content'


class HomePageLocators(BasePageLocators):
    pass

class InputPageLocators(BasePageLocators):
    TRANSACTION_FORM = By.ID, "transaction-form"
    SUBMIT_BUTTON = By.ID, "submit"