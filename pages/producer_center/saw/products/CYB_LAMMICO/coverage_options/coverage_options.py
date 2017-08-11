from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        # MEDEFENSE™

        # Limits
        # 100K/100K
        self._100K_100K_limit = self.driver.find_element(By.ID, "option-768-limit-3024")

        # 250K/250K
        self._250K_250K_limit = self.driver.find_element(By.ID, "option-768-limit-3025")

        # 500K/500K
        self._500K_500K_limit = self.driver.find_element(By.ID, "option-768-limit-3026")

        # 1MM/1MM
        self._1MM_1MM_limit = self.driver.find_element(By.ID, "option-768-limit-3027")

        # Deductibles
        # $1,500
        self._0_deductible = self.driver.find_element(By.ID, "option-768-deductible-1235")

        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self


    def select_MeDefense_100K_100K_Limit_0_Deduct(self):
        Coverage_Options.PageElements(self)._100K_100K_limit.click()
        Coverage_Options.PageElements(self)._0_deductible.click()

    def select_MeDefense_250K_250K_Limit_0_Deduct(self):
        Coverage_Options.PageElements(self)._250K_250K_limit.click()
        Coverage_Options.PageElements(self)._0_deductible.click()

    def select_MeDefense_500K_500K_Limit_0_Deduct(self):
        Coverage_Options.PageElements(self)._500K_500K_limit.click()
        Coverage_Options.PageElements(self)._0_deductible.click()

    def select_MeDefense_1MM_1MM_Limit_0_Deduct(self):
        Coverage_Options.PageElements(self)._1MM_1MM_limit.click()
        Coverage_Options.PageElements(self)._0_deductible.click()

    def select_all_deselect_all(self):
        Coverage_Options.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        Coverage_Options.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        Coverage_Options.PageElements(self).return_to_admin_interface.click()