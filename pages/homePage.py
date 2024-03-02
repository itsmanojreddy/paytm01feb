import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class homePage():
    def __init__(self, driver):
        self.driver = driver

    @property
    def term_insurance_widget(self):
        return self.driver.find_element(By.XPATH, "//div[@class='shadowHandlerBox']/i[contains(@class,'term-life')]")

    @property
    def health_insurance_widget(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Cashless Anywhere']")

    def click_term_insurance(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.term_insurance_widget))
        self.term_insurance_widget.click()

    def click_health_insurance(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.health_insurance_widget))
        self.health_insurance_widget.click()
