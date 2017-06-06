from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def select_PCI_DSS_limits_deductibles_on_coverage_options(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # $250,000 (Full Sublimits) ($250K PCI)
        option_645_limit_2684_250K_pci = self.driver.find_element(By.ID, "option-645-limit-2684")

        # $500,000 (Full Sublimits) ($500K PCI)
        option_645_limit_2685_500K_pci = self.driver.find_element(By.ID, "option-645-limit-2685")

        #$1,000,000 (Full Sublimits) ($1MM PCI)
        option_645_limit_2686_1MM_pci = self.driver.find_element(By.ID, "option-645-limit-2686")

        #$2,000,000 (Full Sublimits) ($2MM PCI)
        option_645_limit_2687_2MM_pci = self.driver.find_element(By.ID, "option-645-limit-2687")

        # Deductibles

        # $500
        #option_645_deductible_1138_500 = self.driver.find_element(By.ID, "option-645-deductible-1138")

        # $1,000
        #option_645_deductible_1133_1k = self.driver.find_element(By.ID, "option-645-deductible-1133")

        # $2,500
        #option_645_deductible_1134_2pt5k = self.driver.find_element(By.ID, "option-645-deductible-1134")

        # $5,000
        option_645_deductible_1135_5k = self.driver.find_element(By.ID, "option-645-deductible-1135")

        # $10,000
        option_645_deductible_1136_10k = self.driver.find_element(By.ID, "option-645-deductible-1136")

        # $25,000
        option_645_deductible_1137_25k = self.driver.find_element(By.ID, "option-645-deductible-1137")

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
        option_645_limit_2686_1MM_pci.click()
        option_645_deductible_1135_5k.click()

    def select_no_PCI_DSS_limits_deductibles_on_coverage_options(self):
            # NetGuard™ Plus with BrandGuard™ Without PCI

            # Limits

            # $250,000 (Full Sublimits) ($250K PCI)
            option_646_limit_2692_250K_pci = self.driver.find_element(By.ID, "option-646-limit-2692")

            # $500,000 (Full Sublimits) ($500K PCI)
            option_646_limit_2689_500K_pci = self.driver.find_element(By.ID, "option-646-limit-2689")

            # $1,000,000 (Full Sublimits) ($1MM PCI)
            option_646_limit_2690_1MM_pci = self.driver.find_element(By.ID, "option-646-limit-2690")

            # $2,000,000 (Full Sublimits) ($2MM PCI)
            option_646_limit_2691_2MM_pci = self.driver.find_element(By.ID, "option-646-limit-2691")

            # Deductibles

            # $500
            option_646_deductible_1145_500 = self.driver.find_element(By.ID, "option-646-deductible-1145")

            # $1,000
            option_646_deductible_1140_1k = self.driver.find_element(By.ID, "option-646-deductible-1140")

            # $2,500
            option_646_deductible_1141_2pt5k = self.driver.find_element(By.ID, "option-646-deductible-1141")

            # $5,000
            option_646_deductible_1142_5k = self.driver.find_element(By.ID, "option-646-deductible-1142")

            # $10,000
            option_646_deductible_1143_10k = self.driver.find_element(By.ID, "option-646-deductible-1143")

            # $25,000
            option_646_deductible_1144_25k = self.driver.find_element(By.ID, "option-646-deductible-1144")

            # Select Limit and Deductible
            option_646_limit_2690_1MM_pci.click()
            option_646_deductible_1141_2pt5k.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()