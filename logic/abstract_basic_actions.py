from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AbstractBasicActions(ABC):
    def __init__(self, driver: webdriver):
        self._driver = driver

    @abstractmethod
    def wait_for_element_present(self, by: By, error_message: str, timeout: int) -> WebElement:
       raise NotImplementedError