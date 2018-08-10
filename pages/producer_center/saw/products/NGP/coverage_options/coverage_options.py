from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        return self

    def select_all_deselect_all(self):
        Coverage_Options.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        Coverage_Options.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):

        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        self.return_to_admin_interface.click()