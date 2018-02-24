from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
            # NetGuard™ Plus with BrandGuard™ Without PCI

            # Limits

            # $250,000 (Full Sublimits) ($250K PCI)
            self.option_646_limit_2692_250K_pci = self.driver.find_element(By.ID, "option-646-limit-2692")

            # $500,000 (Full Sublimits) ($500K PCI)
            self.option_646_limit_2689_500K_pci = self.driver.find_element(By.ID, "option-646-limit-2689")

            # $1,000,000 (Full Sublimits) ($1MM PCI)
            self.option_646_limit_2690_1MM_pci = self.driver.find_element(By.ID, "option-646-limit-2690")

            # $2,000,000 (Full Sublimits) ($2MM PCI)
            self.option_646_limit_2691_2MM_pci = self.driver.find_element(By.ID, "option-646-limit-2691")

            # Deductibles

            # $500
            self.option_646_deductible_1145_500 = self.driver.find_element(By.ID, "option-646-deductible-1145")

            # $1,000
            self.option_646_deductible_1140_1k = self.driver.find_element(By.ID, "option-646-deductible-1140")

            # $2,500
            self.option_646_deductible_1141_2pt5k = self.driver.find_element(By.ID, "option-646-deductible-1141")

            # $5,000
            self.option_646_deductible_1142_5k = self.driver.find_element(By.ID, "option-646-deductible-1142")

            # $10,000
            self.option_646_deductible_1143_10k = self.driver.find_element(By.ID, "option-646-deductible-1143")

            # $25,000
            self.option_646_deductible_1144_25k = self.driver.find_element(By.ID, "option-646-deductible-1144")

            return self

        # select_250K_limit_500_Deductible()
        # select_250K_limit_1K_Deductible()
        # select_250K_limit_2pt5K_Deductible()
        # select_250K_limit_5K_Deductible()
        # select_250K_limit_10K_Deductible()
        # select_250K_limit_25K_Deductible()
        # select_500K_limit_500_Deductible()
        # select_500K_limit_1K_Deductible()
        # select_500K_limit_2pt5K_Deductible()
        # select_500K_limit_5K_Deductible()
        # select_500K_limit_10K_Deductible()
        # select_500K_limit_25K_Deductible()
        # select_1MM_limit_500_Deductible()
        # select_1MM_limit_1K_Deductible()
        # select_1MM_limit_2pt5K_Deductible()
        # select_1MM_limit_5K_Deductible()
        # select_1MM_limit_10K_Deductible()
        # select_1MM_limit_25K_Deductible()
        # select_2MM_limit_500_Deductible()
        # select_2MM_limit_1K_Deductible()
        # select_2MM_limit_2pt5K_Deductible()
        # select_2MM_limit_5K_Deductible()
        # select_2MM_limit_10K_Deductible()
        # select_2MM_limit_25K_Deductible()

    def select_250K_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2692_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1145_500.click()

    def select_250K_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2692_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1140_1k.click()

    def select_250K_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2692_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1141_2pt5k.click()

    def select_250K_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2692_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1142_5k.click()

    def select_250K_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2692_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1143_10k.click()

    def select_250K_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2692_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1144_25k.click()

    def select_500K_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2689_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1145_500.click()

    def select_500K_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2689_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1140_1k.click()

    def select_500K_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2689_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1141_2pt5k.click()

    def select_500K_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2689_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1142_5k.click()

    def select_500K_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2689_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1143_10k.click()

    def select_500K_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2689_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1144_25k.click()

    def select_1MM_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2690_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1145_500.click()

    def select_1MM_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2690_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1140_1k.click()

    def select_1MM_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2690_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1141_2pt5k.click()

    def select_1MM_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2690_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1142_5k.click()

    def select_1MM_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2690_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1143_10k.click()

    def select_1MM_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2690_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1144_25k.click()

    def select_2MM_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2691_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1145_500.click()

    def select_2MM_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2691_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1140_1k.click()

    def select_2MM_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2691_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1141_2pt5k.click()

    def select_2MM_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2691_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1142_5k.click()

    def select_2MM_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2691_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1143_10k.click()

    def select_2MM_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_646_limit_2691_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_646_deductible_1144_25k.click()


    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()