class HomePage:
    load_delay_link_selector = 'a[href="/loaddelay"]'
    dynamic_id_link_selector ='a[href="/dynamicid"]'
    hidden_layer_link_selector = 'a[href="/hiddenlayers"]'
    ajax_link_selector = 'a[href="/ajax"]'
    classattr_selector = 'a[href="/classattr"]'
    AJAX_DATA_LINK = 'text="AJAX Data"'
    scrollbarrs_link = 'text="Scrollbarrs"'
    scrollbarrs_selector = 'a[href="/scrollbars"]'
    dynamic_table_selector = 'a[href="/dynamictable"]'
    verify_text_selector = 'a[href="/verifytext"]'
    progress_bar_selector = 'a[href="/progressbar"]'
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

    def click_scrollbarrs_link(self):
            self.page.click(self.scrollbarrs_selector)
    def click_dynamic_table_link(self):
            self.page.click(self.dynamic_table_selector)

    def click_verify_text_link(self):
            self.page.click(self.verify_text_selector)

    def click_progress_bar_link(self):
            self.page.click(self.progress_bar_selector)