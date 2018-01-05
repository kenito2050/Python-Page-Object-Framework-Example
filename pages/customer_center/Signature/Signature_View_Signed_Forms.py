from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Signature_View_Signed_Forms():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Next Button
        self.next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")

        return self

    def click_next_button_after_inputting_signature(self):
        Signature_View_Signed_Forms.Page_Elements(self).next_button.click()