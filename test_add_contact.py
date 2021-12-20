# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.go_to_home_page(wd)
        self.login(wd)
        self.add_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element("link text", "Logout").click()

    def return_to_home_page(self, wd):
        # return to home page
        wd.find_element("link text", "home page").click()

    def add_contact(self, wd):
        # add contact
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys("name")
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys("lastname")
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys("test")
        wd.find_element("name", "home").click()
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys("123")
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys("test@mail.com")
        wd.find_element("name", "bday").click()
        Select(wd.find_element("name", "bday")).select_by_visible_text("15")
        wd.find_element("xpath", "//option[@value='15']").click()
        wd.find_element("name", "bmonth").click()
        Select(wd.find_element("name", "bmonth")).select_by_visible_text("October")
        wd.find_element("xpath", "//option[@value='October']").click()
        wd.find_element("name", "byear").click()
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys("1995")
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()

    def login(self, wd):
        # login
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("admin")
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("secret")
        wd.find_element("xpath", "//input[@value='Login']").click()

    def go_to_home_page(self, wd):
        # go to home page
        wd.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
