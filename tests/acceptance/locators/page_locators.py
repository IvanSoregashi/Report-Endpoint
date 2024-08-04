from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'
    CONTAINER = By.ID, 'content'


class HomePageLocators(BasePageLocators):
    pass
