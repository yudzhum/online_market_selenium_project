from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class SmartphonesPage(Base):
    URL = 'https://best-magazin.com/smartfoni/'
    BRAND = 'samsung'
    RAM = '12'
    COLOR = 'синий'

    # Locators
    samsung_button = '//a[@href="smartfoni/smartfony-samsung/"]'
    left_slider = '//div[@class="ocf-noUi-touch-area"]'
    blue_color_checkbox = '//button[@id="ocf-v-16-4-102-1"]'
    memory_12_checkbox = '//button[@id="ocf-v-264-2-2222398550-1"]'
    filter_button = '//button[@class="ocf-btn ocf-btn-block ocf-search-btn-static"]'
    first_phone_on_page = '//div[@class="cart"]'
    products_on_page = '//div[@class="row products_category"]'
    info_first_phone_on_page = '//span[@itemprop="name"]'
    price_first_phone_on_page = '//span[@class="price_no_format143853"]'
    cart_button = '//span[@id="cart-total"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.description = ''
        self.price = ''

    # Getters
    def get_first_item_description(self):
        all_products_on_page = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.products_on_page)))
        first_item_desc = all_products_on_page.find_element(By.XPATH, f'.{self.info_first_phone_on_page}').text
        print(f'product_info: {first_item_desc}')
        return first_item_desc

    # Actions
    def click_samsung_button(self):
        self.get_clickable(self.samsung_button).click()
        print('Click on samsung button')

    def move_left_slider_to_the_right(self):
        action = ActionChains(self.driver)
        action.click_and_hold(
            self.get_clickable(self.left_slider)).move_by_offset(50, 0).release().perform()
        print('Moved left slider to the right')

    def scroll_page_down(self):
        self.driver.execute_script('window.scrollTo(0, 400);')

    def click_blue_color_checkbox(self):
        black_checkbox = self.driver.find_element(By.XPATH, self.blue_color_checkbox)
        black_checkbox.click()
        print('Click black color checkbox')

    def click_memory_12_checkbox(self):
        memory_checkbox = self.driver.find_element(By.XPATH, self.memory_12_checkbox)
        memory_checkbox.click()
        print('Click memory 12 GB checkbox')

    def click_filter_button(self):
        self.get_clickable(self.filter_button).click()
        print('Click show filter result')

    def select_first_phone_on_page(self):
        self.get_clickable(self.first_phone_on_page).click()
        print('Select first phone on the page')

    def enter_cart(self):
        self.get_clickable(self.cart_button).click()
        print('enter cart')

    # Methods

    def select_smartphone_with_parameters(self):
        """
        Select smartphone:
        samsung
        black color
        12 GB RAM memory
        """
        self.get_current_url()

        self.click_samsung_button()
        self.move_left_slider_to_the_right()
        self.scroll_page_down()
        self.click_blue_color_checkbox()
        self.click_memory_12_checkbox()
        self.click_filter_button()

        self.description = self.get_first_item_description()
        self.is_word_in_description(self.BRAND, self.description)
        self.is_word_in_description(f'{self.RAM}/', self.description)
        self.is_word_in_description(self.COLOR, self.description)

        self.price = self.get_product_price(self.price_first_phone_on_page)

        self.select_first_phone_on_page()
        self.enter_cart()





