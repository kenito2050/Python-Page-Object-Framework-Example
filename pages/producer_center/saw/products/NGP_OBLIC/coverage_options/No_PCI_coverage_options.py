from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        # NetGuard™ Plus - No PCI

        # Limits

        # $250,000
        self.option_657_limit_2742_250K_pci = self.driver.find_element(By.ID, "option-657-limit-2742")

        # $500,000
        self.option_657_limit_2743_500K_pci = self.driver.find_element(By.ID, "option-657-limit-2743")

        # $1,000,000
        self.option_657_limit_2744_1MM_pci = self.driver.find_element(By.ID, "option-657-limit-2744")

        # Deductibles

        # $0
        self.option_657_deductible_1181_0 = self.driver.find_element(By.ID, "option-657-deductible-1181")

        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    # select_250K_limit_0_Deductible
    # select_250K_limit_0_Deductible
    # select_1MM_limit_0_Deductible

    def select_250K_limit_0_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_657_limit_2742_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_657_deductible_1181_0.click()
        No_PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_500K_limit_0_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_657_limit_2743_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_657_deductible_1181_0.click()
        No_PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_1MM_limit_0_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_657_limit_2744_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_657_deductible_1181_0.click()
        No_PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_all_deselect_all(self):
        No_PCI_Coverage_Options.Page_Elements(self).select_deselect_all.click()

    def proceed_to_quote(self):
        No_PCI_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        No_PCI_Coverage_Options.Page_Elements(self).return_to_admin_interface.click()