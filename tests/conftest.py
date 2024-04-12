import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def setup(request):
    global Web_driver
    # s = Service(ChromeDriverManager(driver_version='100.0.4896.20').install())
    # chrome_options = Options()
    # chrome_options.add_argument("window-size=1920,1080")
    # chrome_options.add_argument("disable-popup-blocking")
    # chrome_options.add_argument(
    #     "--disable-notifications")  # disable notifications like allow location/Show notifications
    # chrome_options.add_argument('--headless')
    # Web_driver = webdriver.Chrome(service=s, options=chrome_options)
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    Web_driver = webdriver.Chrome(options=options)
    Web_driver.maximize_window()
    # Web_driver.get("https://paytm.com/")
    Web_driver.get("https://www.policybazaar.com/")
    yield Web_driver
    Web_driver.close()


def pytest_runtest_teardown(item):
    print(f"Tearing down test-----------------------------------------------------------------------: {item.name}")


# @pytest.fixture(scope='function', autouse=True)
# def setupFunction():
#     Web_driver.get("https://www.amazon.in/")


@pytest.fixture(autouse=True)
def eachTest():
    Web_driver.get("https://www.amazon.in/")
    yield
