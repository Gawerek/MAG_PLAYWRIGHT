from Pages.HomePage import HomePage
from Pages.LoadDelaysPage import LoadDelaysPage


def test_load_delays(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_load_delay_link()
    load_delays_page = LoadDelaysPage(page)
    load_delays_page.click_button_after_delay()