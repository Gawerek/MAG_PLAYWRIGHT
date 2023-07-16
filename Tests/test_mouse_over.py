from Pages.HomePage import HomePage
from Pages.MouseOverPage import MouseOverPage


def test_mouse_over(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_mouse_over_link()
    mouse_over_page = MouseOverPage(page)
    mouse_over_page.click_link_twice()
    mouse_over_page.get_click_count()
