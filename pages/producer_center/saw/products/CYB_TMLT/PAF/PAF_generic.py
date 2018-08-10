from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

class PAF_generic():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        return self


    #TODO
    # Ask Dev to create ID for next button
    def click_next_button(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[5]/a/span[2]/span/span")
        next_button.click()