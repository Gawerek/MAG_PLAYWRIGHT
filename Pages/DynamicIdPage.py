
class DynamicIDPage:
    dynamic_id_locator ='button:text("Button with Dynamic ID")'
    def __init__(self, page):
        self.page = page
    def navigate(self):
        self.page.goto('http://uitestingplayground.com/dynamicid')

    def click_button(self):
        self.page.click(self.dynamic_id_locator)
