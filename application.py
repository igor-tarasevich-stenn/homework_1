from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Application_contact:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def go_to_home_page(self):
        wd = self.wd
        # go to home page
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, username, password):
        wd = self.wd
        self.go_to_home_page(wd)
        # login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def add_contact(self, contact):
        wd = self.wd
        # add contact
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home_tel)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.wd
        # return to home page
        wd.find_element(By.LINK_TEXT, "home page").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()

