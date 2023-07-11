class DynamicTablePage:
    def __init__(self, page):
        self.page = page

    def get_chrome_cpu_label(self):
        chrome_cpu_label = self.page.wait_for_selector(".bg-warning")
        return chrome_cpu_label.inner_text().split(': ')[1]

    def get_chrome_cpu_load(self):
        cpu_value = self.get_chrome_cpu_label()
        print(f"CPU Value from Label: {cpu_value}")
        headers = self.page.query_selector_all("[role='columnheader']")
        cpu_index = None
        for index, header in enumerate(headers):
            if header.inner_text() == 'CPU':
                cpu_index = index
                break
        if cpu_index is None:
            print("CPU Column not found")
            return None  # return None if no CPU column is found
        rows = self.page.query_selector_all("[role='row']")
        for row in rows:
            cells = row.query_selector_all("[role='cell']")
            if cells and cells[0].inner_text() == 'Chrome':
                print(f"CPU Value from Table: {cells[cpu_index].inner_text()}")
                return cells[cpu_index].inner_text()
        print("Chrome row not found")
        return None
