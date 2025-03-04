from base.base_class import Base


class CheckoutWindow(Base):

    # Locators
    make_order_button = '//a[@href="https://best-magazin.com/simplecheckout/"]'

    def __init__(self, driver):
        super().__init__(driver)

    # Getters

    # Actions
    def click_on_make_order_button(self):
        self.get_clickable(self.make_order_button).click()
        print('Click on make order button')

    # Methods

    def confirm_product(self):
        self.click_on_make_order_button()

