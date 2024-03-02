import time

import pytest
from pages.homePage import homePage
from pages.termInsurancePage import termInsurancePage


@pytest.mark.healthpolicy
def test_click_term_life_insurance(setup):
    home = homePage(setup)
    home.click_term_insurance()


@pytest.mark.healthpolicy
def test_click_term_life_insurance_enter_details_initial(setup):
    home = homePage(setup)
    home.click_term_insurance()
    time.sleep(5)
    term = termInsurancePage(setup)
    term.enter_initial_details('Jay', '07/07/1993', '9398816485')
    time.sleep(10)
