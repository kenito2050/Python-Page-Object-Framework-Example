from selenium.webdriver.common.by import By
import time

class Outstanding_Subjectivities():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Submit Button
        self.submit_button = self.driver.find_element(By.XPATH, "//form[@id='binding']/div[1]/div[2]/a/span[2]/span/span")

        # Proceed to Binding Button
        self.proceed_to_binding_button = self.driver.find_element(By.XPATH, "//form[@id='binding']/div[2]/a/span[2]/span/span")

        return self

    def click_proceed_to_binding(self):
        Outstanding_Subjectivities.PageElements(self).proceed_to_binding_button.click()

