from tests.acceptance.locators.page_locators import BasePageLocators, HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return "http://127.0.0.1:5000"

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)


class HomePage(BasePage):
    @property
    def url(self):
        return super().url + "/"

    @property
    def content(self):
        return self.driver.find_element(*HomePageLocators.CONTAINER)


class InputPage(BasePage):
    @property
    def url(self):
        return super().url + "/input"
