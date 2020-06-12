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

    @abstractmethod
    def wait_for_element_present_and_click(self, by: By, error_message: str) -> WebElement:
        raise NotImplementedError

    @abstractmethod
    def wait_for_element_and_send_keys(self, by: By, value: str, error_message: str) -> WebElement:
        raise NotImplementedError

    @abstractmethod
    def wait_for_element_not_present(self, by: By, error_message: str, timeout: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def wait_for_element_and_clear(self, by: By, error_message: str, timeout: int) -> WebElement:
        raise NotImplementedError

    @abstractmethod
    def wait_for_all_elements(self, by: By, error_message: str, timeout: int) -> list[WebElement]:
        raise NotImplemented

    @abstractmethod
    def wait_for_all_elements_are_not_presented(self, by: By, error_message: str, timeout: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_amount_of_elements(self, by: By) -> int:
       raise NotImplementedError 

    @abstractmethod
    def wait_for_element_and_get_attribute(self, by:by, attribue: str, error_message: str, timeout: int) -> str:
        raise NotImplementedError
