import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def setup(request):
    global Web_driver
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080")
    # chrome_options.add_argument("disable-popup-blocking")
    chrome_options.add_argument(
        "--disable-notifications")  # disable notifications like allow location/Show notifications
    # chrome_options.add_argument('--headless')
    Web_driver = webdriver.Chrome(service=s, options=chrome_options)
    Web_driver.maximize_window()
    # Web_driver.get("https://paytm.com/")
    Web_driver.get("https://www.policybazaar.com/")
    yield Web_driver
    Web_driver.close()


@pytest.fixture(autouse=True)
def eachTest():
    Web_driver.get("https://www.policybazaar.com/")
    yield

