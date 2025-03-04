from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver

    """ 
    Method explicitly wait until object became clickable and get locator
    Wait time is 30
    """

    def get_clickable(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, locator)))

    """Method get current url"""

    def get_current_url(self):
        url = self.driver.current_url
        print(f'Current url: {url}')

    """Method assert url"""

    def assert_url(self, expected_url):
        url = self.driver.current_url
        assert expected_url == url
        print('url is GOOD')

    """Method assert word"""

    def assert_word(self, word_from_page, expected_word):
        assert word_from_page.text == expected_word
        print('value word is GOOD')

    """Method make screenshot"""

    def get_screenshot(self):
        now_date = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = f'screenshot-{now_date}.png'
        self.driver.save_screenshot(
            f"C:\\Users\\julia\\PycharmProjects\\online_market_selenium_project\\screen\\{name_screenshot}")

    """Method get product description"""

    def get_product_info(self, locator):
        product_info = self.driver.find_element(By.XPATH, locator).text
        print(f'product info: {product_info}')
        return product_info

    """ Method get product price"""

    def get_product_price(self, locator):
        price = self.driver.find_element(By.XPATH, locator).text
        print(f'price: {price}')
        return price

    """Method check if word in description"""
    def is_word_in_description(self, word, description):
        if word.lower() in description.lower():
            print(f'The {word} in description')
            return True
        print(f'ERROR: {word} not in description')
        return False

