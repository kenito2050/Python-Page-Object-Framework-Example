import pytest
from selenium import webdriver
from config_globals import *


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="ProdDemo5",
                     help="Environment to run test against")


@pytest.fixture
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='class')
def browser(request):
    print("creating a new webdriver")
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(executable_path=str(CONFIG_PATH / 'chromedriver.exe'),
                              chrome_options=options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             file_name_path = "reports/" + file_name
#             _capture_screenshot(file_name_path)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name, browser):
#     driver = browser

