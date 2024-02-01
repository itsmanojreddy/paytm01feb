import time

import pytest

from tests.conftest import setup


@pytest.mark.regression
def test_paytm_launch(setup):
    print("In Launch Test")
    time.sleep(10)
