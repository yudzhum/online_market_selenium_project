from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class SimpleCheckoutWindow(Base):
    """Class for pop up checkout window"""

    # Locators
    window = '//div[@id="popup-okno-inner"]'
    item_description = '//td[@class="name"]'
    price_locator = '//div[@class="totals-right"]'
    make_order_button = '//a[@href="https://best-magazin.com/simplecheckout/"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.description = ''
        self.price = ''

    # Getters

    def get_item_description(self):
        full_window = WebDriverWait(self.driver, 30).until(
           EC.element_to_be_clickable((By.XPATH, self.window)))
        item_desc = full_window.find_element(By.XPATH, f'.{self.item_description}').text
        print(f'pop up window product info: {item_desc}')
        return item_desc

    # Actions

    def click_on_make_order_button(self):
        self.get_clickable(self.make_order_button).click()
        print('Click on make order button')

    # Methods

    def confirm_product(self):
        self.description = self.get_item_description()
        self.price = self.get_product_price(self.price_locator)
        self.click_on_make_order_button()

