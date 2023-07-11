from Pages.DynamicIdPage import DynamicIDPage
from Pages.HomePage import HomePage

def test_dynamic_button_click(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_dynamic_id_link()
    dynamic_id_page = DynamicIDPage(page)
    dynamic_id_page.click_button()