import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.regression
def test_verify_sigIn_button(setup):
    print("In Launch    Test")
    wait = WebDriverWait(setup, 10)
    email = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Sign In']")))
    setup.find_element(By.XPATH , "//span[text()='Sign In']").click()
