# test_class_attribute.py
from Pages.HomePage import HomePage
from Pages.ClassAttributePage import ClassAttributePage

def test_class_attribute(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_classattr_link()
    class_attr_page = ClassAttributePage(page)
    class_attr_page.handle_alert()
    class_attr_page.click_primary_button()
