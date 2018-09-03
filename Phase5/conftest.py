import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.rest_utils import RestFlow

rest = RestFlow()


@pytest.yield_fixture(scope='class')
def wd(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")
    if os.name == 'nt':
        driver = webdriver.Chrome(".\\chromedriver\\chromedriver.exe", chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver = item.instance.driver
    if rep.when == "call" and rep.failed or rep.skipped:
        try:
            allure.attach(driver.get_screenshot_as_png(), name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)


@pytest.fixture(scope='class')
def create_issues(request):
    rest.post_issues(5, "VM Search")
    yield
    rest.delete_issue()
