class HomePage:
    load_delay_link_selector = 'a[href="/loaddelay"]'
    dynamic_id_link_selector ='a[href="/dynamicid"]'
    hidden_layer_link_selector = 'a[href="/hiddenlayers"]'
    ajax_link_selector = 'a[href="/ajax"]'
    classattr_selector = 'a[href="/classattr"]'
    AJAX_DATA_LINK = 'text="AJAX Data"'
    url = 'http://uitestingplayground.com'
    def __init__(self, page):
        self.page = page
    def navigate(self):
        self.page.goto(self.url)

    def click_load_delay_link(self):
        self.page.click(self.load_delay_link_selector)

    def click_dynamic_id_link(self):
            self.page.click(self.dynamic_id_link_selector)

    def click_hidden_layer_link(self):
            self.page.click(self.hidden_layer_link_selector)

    def click_ajax_link(self):
            self.page.click(self.ajax_link_selector)

    def click_ajax_data_link(self):
        self.page.click(self.AJAX_DATA_LINK)

    def click_classattr_link(self):
            self.page.click(self.classattr_selector)