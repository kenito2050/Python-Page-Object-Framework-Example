from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Account_Creation():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Name Field
        self.name_field = self.driver.find_element(By.ID, "name")

        # Email Address Field
        self.email_address_field = self.driver.find_element(By.ID, "email")

        # Username Field
        self.username_field = self.driver.find_element(By.ID, "create-username")

        # Password Field
        self.password_field = self.driver.find_element(By.ID, "create-password")

        # Submit Button
        self.submit_button = self.driver.find_element(By.ID, "mmtm-customer-info-submit")

        return self

    def input_name_email_username_password(self, name, email_address, username, password):

        Account_Creation.Page_Elements(self).name_field.send_keys(name)
        Account_Creation.Page_Elements(self).email_address_field.send_keys(email_address)
        Account_Creation.Page_Elements(self).username_field.send_keys(username)
        Account_Creation.Page_Elements(self).password_field.send_keys(password)

    def click_submit_button(self):

        Account_Creation.Page_Elements(self).submit_button.click()