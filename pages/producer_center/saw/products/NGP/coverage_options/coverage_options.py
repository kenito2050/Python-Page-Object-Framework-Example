from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PCI_Page_Elements(self):

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

    def select_250K_limit_500_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_990_500.click()

    def select_250K_limit_1K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_985_1k.click()


    def select_250K_limit_2pt5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_250K_limit_5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_987_5k.click()

    def select_250K_limit_10K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_988_10k.click()

    def select_250K_limit_25K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_989_25k.click()

    def select_500K_limit_500_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_990_500.click()

    def select_500K_limit_1K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_985_1k.click()

    def select_500K_limit_2pt5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_500K_limit_5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_987_5k.click()

    def select_500K_limit_10K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_988_10k.click()

    def select_500K_limit_25K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_989_25k.click()

    def select_1MM_limit_500_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_990_500.click()

    def select_1MM_limit_1K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_985_1k.click()

    def select_1MM_limit_2pt5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_1MM_limit_5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_987_5k.click()

    def select_1MM_limit_10K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_988_10k.click()

    def select_1MM_limit_25K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_989_25k.click()

    def select_2MM_limit_500_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_990_500.click()

    def select_2MM_limit_1K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_985_1k.click()

    def select_2MM_limit_2pt5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_986_2pt5k.click()

    def select_2MM_limit_5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_987_5k.click()

    def select_2MM_limit_10K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_988_10k.click()

    def select_2MM_limit_25K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_989_25k.click()

    def select_250K_500K_1MM_2MM_limit_500_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_990_500.click()

    def select_250K_500K_limit_500_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_990_500.click()

    def select_250K_500K_1MM_2MM_limit_2pt5K_Deductible(self):
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2448_250K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2449_500K_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2450_1MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_limit_2451_2MM_pci.click()
        Coverage_Options.PCI_Page_Elements(self).option_552_deductible_986_2pt5k.click()


    def select_PCI_DSS_limits_deductibles_on_coverage_options(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # $250,000 (Full Sublimits) ($500K PCI)
        option_552_limit_2448_500K_pci = self.driver.find_element(By.ID, "option-552-limit-2448")

        # $500,000 (Full Sublimits) ($500K PCI)
        option_552_limit_2449_500K_pci = self.driver.find_element(By.ID, "option-552-limit-2449")

        #$1,000,000 (Full Sublimits) ($1MM PCI)
        option_552_limit_2450_1MM_pci = self.driver.find_element(By.ID, "option-552-limit-2450")

        #$2,000,000 (Full Sublimits) ($2MM PCI)
        option_552_limit_2451_2MM_pci = self.driver.find_element(By.ID, "option-552-limit-2451")

        # Deductibles

        # $500
        option_552_deductible_990_500 = self.driver.find_element(By.ID, "option-552-deductible-990")

        # $1,000
        option_552_deductible_985_1k = self.driver.find_element(By.ID, "option-552-deductible-985")

        # $2,500
        option_552_deductible_986_2pt5k = self.driver.find_element(By.ID, "option-552-deductible-986")

        # $5,000
        option_552_deductible_987_5k = self.driver.find_element(By.ID, "option-552-deductible-987")

        # $10,000
        option_552_deductible_988_10k = self.driver.find_element(By.ID, "option-552-deductible-988")

        # $25,000
        option_552_deductible_989_25k = self.driver.find_element(By.ID, "option-552-deductible-989")

        # NetGuard™ Plus with BrandGuard™ Without PCI

        # Limits

        # $500,000 (Full Sublimits) ($500K PCI)
        #option_334_limit_1746_500K_pci = self.driver.find_element(By.ID, "option-334-limit-1746")

        #$1,000,000 (Full Sublimits) ($1MM PCI)
        #option_334_limit_1747_1MM_pci = self.driver.find_element(By.ID, "option-334-limit-1747")

        #$2,000,000 (Full Sublimits) ($2MM PCI)
        #option_334_limit_1748_2MM_pci = self.driver.find_element(By.ID, "option-334-limit-1748")

        # Deductibles

        # $500
        #option_334_deductible_637_500 = self.driver.find_element(By.ID, "option-334-deductible-637")

        # $1,000
        #option_334_deductible_632_1k = self.driver.find_element(By.ID, "option-334-deductible-632")

        # $2,500
        #option_334_deductible_633_2pt5k = self.driver.find_element(By.ID, "option-334-deductible-633")

        # $5,000
        #option_334_deductible_634_5k = self.driver.find_element(By.ID, "option-334-deductible-634")

        # $10,000
        #option_334_deductible_635_10k = self.driver.find_element(By.ID, "option-334-deductible-635")

        # $25,000
        #option_334_deductible_636_25k = self.driver.find_element(By.ID, "option-334-deductible-636")

        # Select Limit and Deductible
        option_552_limit_2450_1MM_pci.click()
        option_552_deductible_986_2pt5k.click()

    def select_no_PCI_DSS_limits_deductibles_on_coverage_options(self):
            # NetGuard™ Plus with BrandGuard™ Without PCI

            # Limits

            # $250,000 (Full Sublimits) ($250K PCI)
            option_553_limit_2455_250K_pci = self.driver.find_element(By.ID, "option-553-limit-2455")

            # $500,000 (Full Sublimits) ($500K PCI)
            option_553_limit_2452_500K_pci = self.driver.find_element(By.ID, "option-553-limit-2452")

            # $1,000,000 (Full Sublimits) ($1MM PCI)
            option_553_limit_2453_1MM_pci = self.driver.find_element(By.ID, "option-553-limit-2453")

            # $2,000,000 (Full Sublimits) ($2MM PCI)
            option_553_limit_2454_2MM_pci = self.driver.find_element(By.ID, "option-553-limit-2454")

            # Deductibles

            # $500
            option_553_deductible_996_500 = self.driver.find_element(By.ID, "option-553-deductible-996")

            # $1,000
            option_553_deductible_991_1k = self.driver.find_element(By.ID, "option-553-deductible-991")

            # $2,500
            option_553_deductible_992_2pt5k = self.driver.find_element(By.ID, "option-553-deductible-992")

            # $5,000
            option_553_deductible_993_5k = self.driver.find_element(By.ID, "option-553-deductible-993")

            # $10,000
            option_553_deductible_994_10k = self.driver.find_element(By.ID, "option-553-deductible-994")

            # $25,000
            option_553_deductible_995_25k = self.driver.find_element(By.ID, "option-553-deductible-995")

            # Select Limit and Deductible
            option_553_limit_2453_1MM_pci.click()
            option_553_deductible_992_2pt5k.click()

            # Select / Deselect All

    def select_all_deselect_all(self):
        select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")
        select_deselect_all.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()