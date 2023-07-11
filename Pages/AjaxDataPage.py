class AjaxDataPage:
    AJAX_BUTTON = '#ajaxButton'
    DATA_LOADED = 'text="Data loaded with AJAX get request."'

    def __init__(self, page):
        self.page = page

    def click_ajax_button(self):
        self.page.click(self.AJAX_BUTTON)

    def wait_for_data_loaded(self):
        self.page.wait_for_selector(self.DATA_LOADED, timeout=20000)