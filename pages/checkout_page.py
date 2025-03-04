from selenium.webdriver import Keys

from base.base_class import Base


class CheckoutPage(Base):
    """Class for checkout page"""

    URL = 'https://best-magazin.com/simplecheckout/'
    FIRST_NAME = 'Иван'
    LAST_NAME = 'Иванов'
    CITY = 'Москва'
    ADDRESS = 'просп. Маршала Жукова, 1'

    # Locators
    item_description = '//td[@class="name"]'
    item_price = '//td[@class="total"]'

    email_input = '//input[@id="customer_email"]'
    phone_input = '//input[@id="customer_telephone"]'
    first_name_input = '//input[@id="customer_firstname"]'
    last_name_input = '//input[@id="customer_lastname"]'

    radio_button_delivery_moscow = '//input[@id="filterit0.filterit2"]'
    city_delivery_input = '//input[@id="shipping_address_city"]'
    city_option_moscow = '//ul[@class="dropdown-menu"]/li[1]'
    shipping_address_input = '//input[@id="shipping_address_address_1"]'
    create_order_button = '//a[@id="simplecheckout_button_confirm"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.description = ''
        self.price = ''

    # Getters
    # Use get_clickable method from Base class

    # Actions
    def input_email(self):
        self.get_clickable(self.email_input).send_keys('email@gmail.com')
        print('Input email')

    def input_phone_number(self):
        self.get_clickable(self.phone_input).click()
        self.get_clickable(self.phone_input).send_keys('1112223344')
        print('Input phone number')

    def input_first_name(self):
        self.get_clickable(self.first_name_input).send_keys(self.FIRST_NAME)
        print('Input first name')

    def input_last_name(self):
        self.get_clickable(self.last_name_input).send_keys(self.LAST_NAME)
        print('Input last name')

    def click_radio_button_delivery_moscow(self):
        self.get_clickable(self.radio_button_delivery_moscow).click()
        print('Click radio button delivery Доставка в пределах МКАД г. Москва - 0 руб.')

    def input_city_delivery(self):
        city = self.get_clickable(self.city_delivery_input)
        city.click()
        city.send_keys(Keys.CONTROL + 'a')
        city.send_keys(Keys.BACKSPACE)
        city.send_keys(self.CITY)
        self.get_clickable(self.city_option_moscow).click()
        print('Input City of delivery')

    def input_shipping_address(self):
        self.get_clickable(self.shipping_address_input).send_keys(self.ADDRESS)
        print('Input shipping address')

    def check_for_create_order_button(self):
        self.get_clickable(self.create_order_button)
        print('Create order button is clickable')

    # Methods

    def check_order_info(self):
        self.get_current_url()
        self.assert_url(self.URL)

        self.description = self.get_product_info(self.item_description)
        self.price = self.get_product_price(self.item_price)

    def place_order(self):
        self.input_email()
        self.input_phone_number()
        self.input_first_name()
        self.input_last_name()

        self.click_radio_button_delivery_moscow()
        self.input_city_delivery()
        self.input_shipping_address()
        self.check_for_create_order_button()

        self.get_screenshot()
