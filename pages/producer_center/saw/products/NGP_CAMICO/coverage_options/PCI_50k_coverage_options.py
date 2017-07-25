from selenium.webdriver.common.by import By

class PCI_50k_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        # NetGuard™ Plus

        # Limits

        # $1,000,000
        self.netguard_plus_1MM_limit_PCI = self.driver.find_element(By.ID, "option-741-limit-2900")

        # Deductibles

        # $0
        self.netguard_plus_0_deductible_50k_embedded_PCI = self.driver.find_element(By.ID, "option-741-deductible-1219")

        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self


    def select_NetGuard_Plus_PCI_1MM_limit_0_Deductible_50k_embedded(self):
        PCI_50k_Coverage_Options.Page_Elements(self).netguard_plus_1MM_limit_PCI.click()
        PCI_50k_Coverage_Options.Page_Elements(self).netguard_plus_0_deductible_50k_embedded_PCI.click()
        PCI_50k_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_all_deselect_all(self):
        PCI_50k_Coverage_Options.Page_Elements(self).select_deselect_all.click()

    def proceed_to_quote(self):
        PCI_50k_Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        PCI_50k_Coverage_Options.Page_Elements(self).return_to_admin_interface.click()