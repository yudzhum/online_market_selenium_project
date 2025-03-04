import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver():
    """Set up webdriver"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service('/Users/julia/PycharmProjects/resource/chromedriver.exe')
    config_driver = webdriver.Chrome(options=options, service=service)

    yield config_driver

    config_driver.quit()
