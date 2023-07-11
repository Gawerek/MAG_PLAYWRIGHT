import playwright.sync_api
from playwright.sync_api import expect


class HiddenLayersPage:
    button_selector = '#greenButton'
    url = 'http://uitestingplayground.com/hiddenlayers'

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.url)

    def click_button(self):
        self.page.click(self.button_selector)

    def is_button_clickable(self):
        button = self.page.locator(self.button_selector)

        is_button_clickable = expect(button).not_to_be_visible()
        return is_button_clickable
