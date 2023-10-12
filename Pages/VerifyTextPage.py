from playwright.sync_api import expect

class VerifyTextPage:
    def __init__(self, page):
        self.page = page

    def is_welcome_text_present(self):
        locator = self.page.get_by_text("Welcome UserName!", exact=True)
        print(locator.text_content())
        expect(locator).to_contain_text("Welcome UserName!")
