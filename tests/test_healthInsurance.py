import time

import pytest
from pages.homePage import homePage

@pytest.mark.policy
def test_click_health_insurance(setup):
    home = homePage(setup)
    home.click_health_insurance()
    time.sleep(10)
