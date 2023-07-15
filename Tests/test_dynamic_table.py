from Pages.HomePage import HomePage
from Pages.DynamicTablePage import DynamicTablePage

def test_dynamic_table(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_dynamic_table_link()
    dynamic_table_page = DynamicTablePage(page)
    dynamic_table_page.get_chrome_cpu_load_and_assert()