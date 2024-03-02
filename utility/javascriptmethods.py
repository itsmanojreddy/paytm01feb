from abc import abstractmethod

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class javascriptmethods():
    # @abstractmethod
    def clickjs(self, driver, element):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
        driver.execute_script("arguments[0].click();", element)
