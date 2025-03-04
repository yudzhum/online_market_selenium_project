from base.base_class import Base


class MainPage(Base):
    URL = 'https://best-magazin.com/'

    # Locators
    navbar_smartphones = '//a[@href="https://best-magazin.com/smartfoni/"]'

    def __init__(self, driver):
        super().__init__(driver)

    # Getters
    # method get_clickable from class Base

    # Actions
    def click_on_menu_smartphones(self):
        self.get_clickable(self.navbar_smartphones).click()
        print('Click on smartphones')

    # Methods
    def load(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def select_menu_smartphones(self):
        self.click_on_menu_smartphones()
        self.assert_url('https://best-magazin.com/smartfoni/')
