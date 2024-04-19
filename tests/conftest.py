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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # if (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.replace("::", "_") + ".png"
        _capture_screenshot(file_name)
        if file_name:
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    Web_driver.get_screenshot_as_file(name)
