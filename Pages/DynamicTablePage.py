class DynamicTablePage:
    def __init__(self, page):
        self.page = page



    def get_chrome_cpu_load_and_assert(self):
        war_var = self.page.locator(".bg-warning").inner_text().split(" ")[2]

        table_list = self.page.locator("span[role=\"cell\"]").all_inner_texts()
        chrome_values = table_list[table_list.index("Chrome"):
                                   table_list.index("Chrome") + 5]
        tab_val = 'None'
        for value in chrome_values:
            if '%' in value:
                tab_val = value
                break

        print("Warning value: ", war_var)
        print("Table value: ", tab_val)
        assert tab_val == war_var
