
from Pages.HomePage import HomePage
from Pages.ScrollBarPage import ScrollbarsPage

def test_class_attribute(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_scrollbarrs_link()
    scroll_bars_page = ScrollbarsPage(page)
    scroll_bars_page.scroll_to_button_and_click()