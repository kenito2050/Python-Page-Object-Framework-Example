from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Login():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # User Name Field
        self.user_field = self.driver.find_element(By.ID, "login-username")

        # Password Field
        self.password_field = self.driver.find_element(By.ID, "login-password")

        # Submit Button
        self.submit_button = self.driver.find_element(By.ID, "mmtm-login-submit")

        return self

    def login(self, username, password):

        Login.Page_Elements(self).user_field.send_keys(username)
        Login.Page_Elements(self).password_field.send_keys(password)

    def click_submit_button(self):

        Login.Page_Elements(self).submit_button.click()


