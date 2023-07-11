class LoadDelaysPage:
    def __init__(self, page):
        self.page = page
        self.button_selector = '.btn.btn-primary'

    def click_button_after_delay(self):
        self.page.wait_for_selector(self.button_selector, state="attached")
        self.page.click(self.button_selector)