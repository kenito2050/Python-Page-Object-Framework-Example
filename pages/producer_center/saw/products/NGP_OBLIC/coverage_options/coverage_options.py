from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

            # Select / Deselect All
            self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

            # Proceed to Quote
            self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                        "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
            # Return to Admin Interface
            self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

            return self


    def select_PCI_DSS_option_limits_deductibles_on_coverage_options(self):

        # NetGuard™ Plus

        # Limits

        # $250,000
        option_656_limit_2739_250K_pci = self.driver.find_element(By.ID, "option-656-limit-2739")

        # $500,000
        option_656_limit_2740_500K_pci = self.driver.find_element(By.ID, "option-656-limit-2740")

        #$1,000,000
        option_656_limit_2741_1MM_pci = self.driver.find_element(By.ID, "option-656-limit-2741")

        # Deductibles

        # $0
        option_656_deductible_1180_0 = self.driver.find_element(By.ID, "option-656-deductible-1180")

        # Click Select / Deselect All
        # Select Limit and Deductible
        # Proceed to Next Page
        Coverage_Options.Page_Elements(self).select_deselect_all.click()
        option_656_limit_2739_250K_pci.click()
        option_656_limit_2740_500K_pci.click()
        option_656_limit_2741_1MM_pci.click()
        option_656_deductible_1180_0.click()
        Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_NO_PCI_DSS_option_limits_deductibles_on_coverage_options(self):
        # NetGuard™ Plus - No PCI

        # Limits

        # $250,000
        option_657_limit_2742_250K_pci = self.driver.find_element(By.ID, "option-657-limit-2742")

        # $500,000
        option_657_limit_2743_500K_pci = self.driver.find_element(By.ID, "option-657-limit-2743")

        # $1,000,000
        option_657_limit_2744_1MM_pci = self.driver.find_element(By.ID, "option-657-limit-2744")

        # Deductibles

        # $0
        option_657_deductible_1181_0 = self.driver.find_element(By.ID, "option-657-deductible-1181")

        # Click Select / Deselect All
        # Select Limit and Deductible
        # Proceed to Next Page
        Coverage_Options.Page_Elements(self).select_deselect_all.click()
        option_657_limit_2742_250K_pci.click()
        option_657_limit_2743_500K_pci.click()
        option_657_limit_2744_1MM_pci.click()
        option_657_deductible_1181_0.click()
        Coverage_Options.Page_Elements(self).proceed_to_quote.click()