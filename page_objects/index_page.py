from selenium.webdriver.common.by import By
from my_framework.utilities.web_ui.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __welcome_text = (By.XPATH, '//div[@class="topic-block-title"]/h2')

    def welcome_text(self):
        return self.wait_until_element_located(self.__welcome_text).text
