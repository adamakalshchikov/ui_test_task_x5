from logic.abstract_basic_actions import AbstractBasicActions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasicActions(AbstractBasicActions):
    def __init__(self, driver, config: dict):
        super().__init__(driver)
        if config['browser'] == "chrome":
            self._init_chrome()
        if config['browser' ]== "firefox":
            self._init_firefox()

    def _init_chrome(self):
        raise NotImplementedError

    def _init_firefox(self):
        raise NotImplementedError

    def wait_for_element_present(self, by: By, error_message: str, timeout: int) -> WebElement:
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(
            EC.presence_of_element_located(by),
            message=error_message
        )

    def wait_for_element_present(self, by: By, error_message: str) -> WebElement:
        return self.wait_for_element_present(by, error_message, 5)
