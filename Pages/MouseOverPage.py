from playwright.sync_api import expect

class MouseOverPage:

    btn_locator ="text=Click me"
    result_locator = ".badge-light"

    def __init__(self, page):
        self.page = page

    def click_link_twice(self):
        link = self.page.locator(self.btn_locator)
        link.dblclick()

    def get_click_count(self):
        count = self.page.locator(self.result_locator)
        print(count.all_text_contents())
        expect(count).to_have_text("2")