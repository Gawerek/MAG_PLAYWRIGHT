class ScrollbarsPage:

    button_selector = '#hidingButton'
    def __init__(self, page):
        self.page = page

    def scroll_to_button_and_click(self):
        button_click = self.page.click(self.button_selector)
        return button_click
