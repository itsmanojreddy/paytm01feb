import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup(request):
    global Web_driver
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    Web_driver = webdriver.Chrome(service=s, options=chrome_options)
    Web_driver.maximize_window()
    Web_driver.get("https://paytm.com/")
    yield
    Web_driver.close()
