# conftest.py

import pytest as pytest
from selenium import webdriver



from selenium.webdriver.chrome.service import Service

from pageobject.search_page_Google import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


#fixture for Login Functionality

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser_name")
    S = Service("D:\\chromedriver.exe")
    driver = webdriver.Chrome(service=S)
    yield driver
    driver.quit()

#code for the google page  search Functionality

@pytest.fixture
def google_search(driver):
    page = LoginPage(driver)
    page.open()
    return page



#screenshot cature code as below

@pytest.hookimpl(hookwrapper=True)
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
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(item.funcargs['driver'], file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)
