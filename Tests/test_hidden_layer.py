import time
from Pages.HomePage import HomePage
from Pages.HiddenLayersPage import HiddenLayersPage
def test_hidden_layers(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_hidden_layer_link()
    hidden_layers_page = HiddenLayersPage(page)
    hidden_layers_page.click_button()
