from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def _driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome('./Phase4/chromedriver/chromedriver', chrome_options=chrome_options)
    return driver

