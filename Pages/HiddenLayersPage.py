import pytest


class HiddenLayersPage:
    button_selector = "button#greenButton"
    obstructing_button_selector = "button#blueButton"
    url = 'http://uitestingplayground.com/hiddenlayers'

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.url)

    def click_button(self):
        try:
            # First, wait for the obstructing button to be hidden
            self.page.wait_for_selector(self.obstructing_button_selector, state="hidden", timeout=2000)

            # Now, click the green button
            green_btn = self.page.locator(self.button_selector)
            green_btn.click()
        except TimeoutError:
            # If the blueButton is not hidden after waiting, force click the greenButton
            print("blueButton is obstructing. Attempting to force click greenButton...")
            self.page.evaluate('''() => {
                document.querySelector("button#greenButton").click();
            }''')