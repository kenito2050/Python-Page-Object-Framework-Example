from selenium.webdriver.common.by import By
import time

class PAF_data_security_encrypted():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Is such data encrypted to industry standards?

        # DISPLAYS IF YES TO ABOVE QUESTION

        self.data_security_encrypted_yes = self.driver.find_element(By.ID, "cyb_aao_data_security_encrypted-yes")

        self.data_security_encrypted_no = self.driver.find_element(By.ID, "cyb_aao_data_security_encrypted-no")

        return self

    def click_yes_data_security_encrypted(self):

        PAF_data_security_encrypted.Page_Elements(self).data_security_encrypted_yes.click()

    def click_no_data_security_encrypted(self):
        PAF_data_security_encrypted.Page_Elements(self).data_security_encrypted_no.click()



    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):

        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[5]/a/span[2]")

        # scroll to element
        self.driver.execute_script("return arguments[0].scrollIntoView();", next_button)

        next_button.click()