from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class termInsurancePage():
    def __init__(self, driver):
        self.driver = driver

    @property
    def Name(self):
        return self.driver.find_element(By.ID, "nameAdd")

    @property
    def DOB(self):
        return self.driver.find_element(By.ID, "dob")

    @property
    def MobileNumber(self):
        return self.driver.find_element(By.ID, "mobileNo")

    def enter_initial_details(self, nameVal, dobVal, MobVal):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.Name))
        self.Name.click()
        self.Name.send_keys(nameVal)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DOB))
        self.DOB.click()
        self.DOB.send_keys(dobVal)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MobileNumber))
        self.MobileNumber.click()
        self.MobileNumber.send_keys(MobVal)
