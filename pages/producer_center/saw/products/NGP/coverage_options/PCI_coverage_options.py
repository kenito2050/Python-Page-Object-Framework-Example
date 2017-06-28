from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # $250,000 (Full Sublimits) ($250K PCI)
        self.option_552_limit_2448_250K_pci = self.driver.find_element(By.ID, "option-552-limit-2448")

        # $500,000 (Full Sublimits) ($500K PCI)
        self.option_552_limit_2449_500K_pci = self.driver.find_element(By.ID, "option-552-limit-2449")

        # $1,000,000 (Full Sublimits) ($1MM PCI)
        self.option_552_limit_2450_1MM_pci = self.driver.find_element(By.ID, "option-552-limit-2450")

        # $2,000,000 (Full Sublimits) ($2MM PCI)
        self.option_552_limit_2451_2MM_pci = self.driver.find_element(By.ID, "option-552-limit-2451")

        # Deductibles

        # $500
        self.option_552_deductible_990_500 = self.driver.find_element(By.ID, "option-552-deductible-990")

        # $1,000
        self.option_552_deductible_985_1k = self.driver.find_element(By.ID, "option-552-deductible-985")

        # $2,500
        self.option_552_deductible_986_2pt5k = self.driver.find_element(By.ID, "option-552-deductible-986")

        # $5,000
        self.option_552_deductible_987_5k = self.driver.find_element(By.ID, "option-552-deductible-987")

        # $10,000
        self.option_552_deductible_988_10k = self.driver.find_element(By.ID, "option-552-deductible-988")

        # $25,000
        self.option_552_deductible_989_25k = self.driver.find_element(By.ID, "option-552-deductible-989")

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
    # select_250K_500K_1MM_2MM_limit_500_Deductible()
    # select_250K_500K_limit_500_Deductible()
    # select_250K_500K_1MM_2MM_limit_2pt5K_Deductible()

    def select_250K_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_990_500.click()

    def select_250K_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_985_1k.click()

    def select_250K_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_250K_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_987_5k.click()

    def select_250K_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_988_10k.click()

    def select_250K_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_989_25k.click()

    def select_500K_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_990_500.click()

    def select_500K_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_985_1k.click()

    def select_500K_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_500K_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_987_5k.click()

    def select_500K_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_988_10k.click()

    def select_500K_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_989_25k.click()

    def select_1MM_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_990_500.click()

    def select_1MM_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_985_1k.click()

    def select_1MM_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_1MM_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_987_5k.click()

    def select_1MM_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_988_10k.click()

    def select_1MM_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_989_25k.click()

    def select_2MM_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_990_500.click()

    def select_2MM_limit_1K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_985_1k.click()

    def select_2MM_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_2MM_limit_5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_987_5k.click()

    def select_2MM_limit_10K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_988_10k.click()

    def select_2MM_limit_25K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_989_25k.click()


    def select_250K_500K_1MM_2MM_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_990_500.click()

    def select_250K_500K_limit_500_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_990_500.click()

    def select_250K_500K_1MM_2MM_limit_2pt5K_Deductible(self):
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2448_250K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2449_500K_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        PCI_Coverage_Options.Page_Elements(self).option_552_deductible_986_2pt5k.click()