from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # NetGuard™ Plus with BrandGuard™ Without PCI

        # Limits

        # $250,000 (Full Sublimits) ($250K PCI)
        self.option_553_limit_2455_250K_pci = self.driver.find_element(By.ID, "option-553-limit-2455")

        # $500,000 (Full Sublimits) ($500K PCI)
        self.option_553_limit_2452_500K_pci = self.driver.find_element(By.ID, "option-553-limit-2452")

        # $1,000,000 (Full Sublimits) ($1MM PCI)
        self.option_553_limit_2453_1MM_pci = self.driver.find_element(By.ID, "option-553-limit-2453")

        # $2,000,000 (Full Sublimits) ($2MM PCI)
        self.option_553_limit_2454_2MM_pci = self.driver.find_element(By.ID, "option-553-limit-2454")

        # Deductibles

        # $500
        self.option_553_deductible_996_500 = self.driver.find_element(By.ID, "option-553-deductible-996")

        # $1,000
        self.option_553_deductible_991_1k = self.driver.find_element(By.ID, "option-553-deductible-991")

        # $2,500
        self.option_553_deductible_992_2pt5k = self.driver.find_element(By.ID, "option-553-deductible-992")

        # $5,000
        self.option_553_deductible_993_5k = self.driver.find_element(By.ID, "option-553-deductible-993")

        # $10,000
        self.option_553_deductible_994_10k = self.driver.find_element(By.ID, "option-553-deductible-994")

        # $25,000
        self.option_553_deductible_995_25k = self.driver.find_element(By.ID, "option-553-deductible-995")

        return self

    def select_250K_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_996_500.click()

    def select_250K_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_991_1k.click()

    def select_250K_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_992_2pt5k.click()

    def select_250K_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_993_5k.click()

    def select_250K_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_994_10k.click()

    def select_250K_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_995_25k.click()

    def select_500K_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_996_500.click()

    def select_500K_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_991_1k.click()

    def select_500K_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_992_2pt5k.click()

    def select_500K_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_993_5k.click()

    def select_500K_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_994_10k.click()

    def select_500K_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_995_25k.click()

    def select_1MM_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_996_500.click()

    def select_1MM_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_991_1k.click()

    def select_1MM_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_992_2pt5k.click()

    def select_1MM_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_993_5k.click()

    def select_1MM_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_994_10k.click()

    def select_1MM_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_995_25k.click()

    def select_2MM_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_996_500.click()

    def select_2MM_limit_1K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_991_1k.click()

    def select_2MM_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_992_2pt5k.click()

    def select_2MM_limit_5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_993_5k.click()

    def select_2MM_limit_10K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_994_10k.click()

    def select_2MM_limit_25K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_995_25k.click()

    def select_250K_500K_1MM_2MM_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_996_500.click()

    def select_250K_500K_limit_500_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_996_500.click()

    def select_250K_500K_1MM_2MM_limit_2pt5K_Deductible(self):
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2455_250K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2452_500K_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2453_1MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_limit_2454_2MM_pci.click()
        No_PCI_Coverage_Options.Page_Elements(self).option_553_deductible_992_2pt5k.click()