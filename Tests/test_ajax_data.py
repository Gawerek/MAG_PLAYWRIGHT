from Pages.HomePage import HomePage
from Pages.AjaxDataPage import AjaxDataPage
import time
def test_ajax_data(page):
    start_time = time.time()
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_ajax_data_link()

    ajax_data_page = AjaxDataPage(page)
    ajax_data_page.click_ajax_button()
    ajax_data_page.wait_for_data_loaded()
    print(f"Selenium: {time.time() - start_time} seconds")


