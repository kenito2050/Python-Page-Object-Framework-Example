from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # $250,000 (Full Sublimits) ($250K PCI)
        self.option_645_limit_2684_250K_pci = self.driver.find_element(By.ID, "option-645-limit-2684")

        # $500,000 (Full Sublimits) ($500K PCI)
        self.option_645_limit_2685_500K_pci = self.driver.find_element(By.ID, "option-645-limit-2685")

        #$1,000,000 (Full Sublimits) ($1MM PCI)
        self.option_645_limit_2686_1MM_pci = self.driver.find_element(By.ID, "option-645-limit-2686")

        #$2,000,000 (Full Sublimits) ($2MM PCI)
        self.option_645_limit_2687_2MM_pci = self.driver.find_element(By.ID, "option-645-limit-2687")

        # Deductibles

        # $500
        self.option_645_deductible_1138_500 = self.driver.find_element(By.ID, "option-645-deductible-1138")

        # $1,000
        self.option_645_deductible_1133_1k = self.driver.find_element(By.ID, "option-645-deductible-1133")

        # $2,500
        self.option_645_deductible_1134_2pt5k = self.driver.find_element(By.ID, "option-645-deductible-1134")

        # $5,000
        self.option_645_deductible_1135_5k = self.driver.find_element(By.ID, "option-645-deductible-1135")

        # $10,000
        self.option_645_deductible_1136_10k = self.driver.find_element(By.ID, "option-645-deductible-1136")

        # $25,000
        self.option_645_deductible_1137_25k = self.driver.find_element(By.ID, "option-645-deductible-1137")

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
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2684_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1138_500.click()

    def select_250K_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2684_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1133_1k.click()

    def select_250K_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2684_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1134_2pt5k.click()

    def select_250K_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2684_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1135_5k.click()

    def select_250K_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2684_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1136_10k.click()

    def select_250K_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2684_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1137_25k.click()

    def select_500K_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2685_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1138_500.click()

    def select_500K_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2685_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1133_1k.click()

    def select_500K_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2685_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1134_2pt5k.click()

    def select_500K_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2685_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1135_5k.click()

    def select_500K_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2685_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1136_10k.click()

    def select_500K_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2685_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1137_25k.click()

    def select_1MM_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2686_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1138_500.click()

    def select_1MM_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2686_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1133_1k.click()

    def select_1MM_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2686_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1134_2pt5k.click()

    def select_1MM_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2686_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1135_5k.click()

    def select_1MM_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2686_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1136_10k.click()

    def select_1MM_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2686_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1137_25k.click()

    def select_2MM_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2687_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1138_500.click()

    def select_2MM_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2687_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1133_1k.click()

    def select_2MM_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2687_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1134_2pt5k.click()

    def select_2MM_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2687_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1135_5k.click()

    def select_2MM_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2687_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1136_10k.click()

    def select_2MM_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_645_limit_2687_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_645_deductible_1137_25k.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()