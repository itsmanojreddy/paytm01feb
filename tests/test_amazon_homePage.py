import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.amazonHomePage import amazonHomePage


@pytest.mark.amazon
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


@pytest.mark.test12
def test_click_first_result(setup):
    amazon = amazonHomePage(setup)
    amazon.select_All_dropdown("All Categories")
    amazon.enter_search_value("Bags")
    amazon.click_suggested_Search(1)
    amazon.click_first_item_from_results(1)
    windows = setup.window_handles
    print("size  :  " + str(windows))
    WebDriverWait(setup, 10).until(EC.number_of_windows_to_be(2))
    setup.switch_to.window(setup.window_handles[1])
    print(amazon.get_product_price())
