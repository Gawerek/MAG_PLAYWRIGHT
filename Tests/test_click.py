from Pages.HomePage import HomePage
from Pages.ClickPage import ClickButtonPage

def test_click_button_playwright(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_click_link()
    click_button_page = ClickButtonPage(page)
    click_button_page.click_button()
    click_button_page.is_button_green()