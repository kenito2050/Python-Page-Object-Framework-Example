from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Signature():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Handwritten
        self.handwritten_radio_button = self.driver.find_element(By.ID, "sig-toggle-signature")

        # Typed
        self.typed_radio_button = self.driver.find_element(By.ID, "sig-toggle-typed")

        # Clear Signature Button
        self.clear_signature_button = self.driver.find_element(By.CLASS_NAME, "text-button-ds")

        # Save Signature Button
        self.save_signature_button = self.driver.find_element(By.ID, "sign-button-text")

        return self

    def select_typed(self):
        Signature.Page_Elements(self).typed_radio_button.click()

    def input_typed_signature(self, signature):
        typed_signature_field = self.driver.find_element(By.ID, "signature-typed")
        typed_signature_field.send_keys(signature)

    def click_save_signature_button(self):
        Signature.Page_Elements(self).save_signature_button.click()

    # def click_next_button_after_inputting_signature(self):
    #     next_button = self.driver.find_element(By.CLASS_NAME, "text-button-ds")
    #     next_button.click()