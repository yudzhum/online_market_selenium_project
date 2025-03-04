from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.simple_checkout_window import SimpleCheckoutWindow
from pages.smartphones_page import SmartphonesPage


BRAND = 'samsung'
RAM = '12'
COLOR = 'синий'


def test_buy_product(driver):
    """
    E2E test for ordering a smartphone with parameters:
    Samsung
    12 GB RAM
    Blue
    """

    print('Start test')

    mp = MainPage(driver)
    mp.load()
    mp.select_menu_smartphones()
    print('------------------------')

    sp = SmartphonesPage(driver)
    sp.select_smartphone_with_parameters()
    print('------------------------')

    scw = SimpleCheckoutWindow(driver)
    scw.confirm_product()
    assert sp.description == scw.description
    print('Description in pop up window is GOOD')
    assert sp.price == scw.price
    print('Price in pop uo window is GOOD')
    print('------------------------')

    cp = CheckoutPage(driver)
    cp.check_order_info()
    assert cp.description == sp.description
    print('Description in order is GOOD')
    assert cp.price == sp.price
    print('Price in order in GOOD')
    cp.place_order()

    print('Finish test')
