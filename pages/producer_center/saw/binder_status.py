from selenium.webdriver.common.by import By
import time

class Binder_Status():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Create Binder Button
        # self.create_binder_button = self.driver.find_element(By.XPATH, "//form[@id='submit-blockui']/span[2]/span/span")

        self.create_binder_button = self.driver.find_element(By.ID, "submit-blockui")

        return self

    def click_create_binder(self):
        Binder_Status.PageElements(self).create_binder_button.click()

