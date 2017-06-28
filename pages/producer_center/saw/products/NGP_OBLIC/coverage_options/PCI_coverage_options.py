from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        # NetGuard™ Plus

        # Limits

        # $250,000
        self.option_656_limit_2739_250K_pci = self.driver.find_element(By.ID, "option-656-limit-2739")

        # $500,000
        self.option_656_limit_2740_500K_pci = self.driver.find_element(By.ID, "option-656-limit-2740")

        # $1,000,000
        self.option_656_limit_2741_1MM_pci = self.driver.find_element(By.ID, "option-656-limit-2741")

        # Deductibles

        # $0
        self.option_656_deductible_1180_0 = self.driver.find_element(By.ID, "option-656-deductible-1180")

        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    # select_250K_limit_0_Deductible()
    # select_250K_limit_0_Deductible()
    # select_1MM_limit_0_Deductible()

    def select_250K_limit_0_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_656_limit_2739_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_656_deductible_1180_0.click()
        PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_500K_limit_0_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_656_limit_2740_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_656_deductible_1180_0.click()
        PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_1MM_limit_0_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_656_limit_2741_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_656_deductible_1180_0.click()
        PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_all_deselect_all(self):
        PCI_Coverage_Options.Page_Elements(self).select_deselect_all.click()

    def proceed_to_quote(self):
        PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        PCI_Coverage_Options.Page_Elements(self).return_to_admin_interface.click()