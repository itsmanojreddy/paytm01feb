import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.amazonHomePage import amazonHomePage


@pytest.mark.test123
def test_verify_sigIn_button(setup):
    setup.get("https://www.amazon.in/")
    amazon = amazonHomePage(setup)
    amazon.select_All_dropdown("Alexa Skills")
    amazon.enter_search_value("Bags")
    amazon.click_suggested_Search(1)
    # time.sleep(10)


@pytest.mark.test123
def test_verify_select_all_dropdown(setup):
    setup.get("https://www.amazon.in/")
    amazon = amazonHomePage(setup)
    amazon.select_All_dropdown("All Categories")
    amazon.enter_search_value("Bags")
    amazon.click_suggested_Search(1)
