# Plik: Tests/test_verify_text.py
from Pages.HomePage import HomePage
from Pages.VerifyTextPage import VerifyTextPage

def test_verify_text(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_verify_text_link()
    verify_text_page = VerifyTextPage(page)
    verify_text_page.is_welcome_text_present(), f"Welcome text not found in text: {verify_text_page.is_welcome_text_present()}"