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
        progress_bar_value_stop = self.page.wait_for_selector(self.progress_bar_selector)
        return progress_bar_value_stop

    def click_stop_button(self):
        button = self.page.locator().click(self.stop_button_locator)
        button.click()