from playwright.sync_api import expect


class ClickButtonPage:
    BUTTON_SELECTOR = '#badButton'

    def __init__(self, page):
        self.page = page

    def click_button(self):
        self.page.click(self.BUTTON_SELECTOR)

    def is_button_green(self):
        button = self.page.locator(self.BUTTON_SELECTOR)
        print(button)
        if expect(button).to_have_class("btn btn-success"):
            return button
        else:
            False, "Button didn't change class"
