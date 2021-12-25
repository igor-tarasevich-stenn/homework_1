from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ApplicationGroup:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        wd = self.wd
        # login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        wd = self.wd
        # create group
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        # return to groups page
        wd.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()
