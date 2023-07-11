

class ClassAttributePage:
    def __init__(self, page):
        self.page = page
    def navigate(self):
        self.page.goto('http://uitestingplayground.com/classattr')

    def click_primary_button(self):
        self.page.click('.btn-primary')

    def handle_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())