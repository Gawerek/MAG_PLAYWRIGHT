class ProgressBarPage:
    start_button_locator = "button:has-text(\"Start\")"
    stop_button_locator = "button:has-text(\"Stop\")"
    progress_bar_selector = "#progressBar[aria-valuenow='75']"


    def __init__(self, page):
        self.page = page


    def click_start_button(self):
        button = self.page.locator(self.start_button_locator)
        button.click()

    def wait_for_value_on_bar(self):
        self.page.wait_for_selector(self.progress_bar_selector)


    def click_stop_button(self):
        button = self.page.click(self.stop_button_locator)
        return button