
from Pages.HomePage import HomePage
from Pages.ProgressBarPage import ProgressBarPage
def test_class_attribute(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_progress_bar_link()
    progress_bar_page = ProgressBarPage(page)
    progress_bar_page.click_start_button()
    progress_bar_page.wait_for_value_on_bar()
    progress_bar_page.click_stop_button()

