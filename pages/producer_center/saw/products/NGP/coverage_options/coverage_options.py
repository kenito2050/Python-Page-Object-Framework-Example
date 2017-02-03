from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def select_PCI_DSS_limits_deductibles_on_coverage_options(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # $500,000 (Full Sublimits) ($500K PCI)
        option_312_limit_1755_500K_pci = self.driver.find_element(By.ID, "option-312-limit-1755")

        #$1,000,000 (Full Sublimits) ($1MM PCI)
        option_312_limit_1760_1MM_pci = self.driver.find_element(By.ID, "option-312-limit-1760")

        #$2,000,000 (Full Sublimits) ($2MM PCI)
        option_312_limit_1763_2MM_pci = self.driver.find_element(By.ID, "option-312-limit-1763")

        # Deductibles

        # $500
        option_312_deductible_624_500 = self.driver.find_element(By.ID, "option-312-deductible-624")

        # $1,000
        option_312_deductible_619_1k = self.driver.find_element(By.ID, "option-312-deductible-619")

        # $2,500
        option_312_deductible_620_2pt5k = self.driver.find_element(By.ID, "option-312-deductible-620")

        # $5,000
        option_312_deductible_621_5k = self.driver.find_element(By.ID, "option-312-deductible-621")

        # $10,000
        option_312_deductible_622_10k = self.driver.find_element(By.ID, "option-312-deductible-622")

        # $25,000
        option_312_deductible_623_25k = self.driver.find_element(By.ID, "option-312-deductible-623")

        # NetGuard™ Plus with BrandGuard™ Without PCI

        # Limits

        # $500,000 (Full Sublimits) ($500K PCI)
        option_334_limit_1746_500K_pci = self.driver.find_element(By.ID, "option-334-limit-1746")

        #$1,000,000 (Full Sublimits) ($1MM PCI)
        option_334_limit_1747_1MM_pci = self.driver.find_element(By.ID, "option-334-limit-1747")

        #$2,000,000 (Full Sublimits) ($2MM PCI)
        option_334_limit_1748_2MM_pci = self.driver.find_element(By.ID, "option-334-limit-1748")

        # Deductibles

        # $500
        option_334_deductible_637_500 = self.driver.find_element(By.ID, "option-334-deductible-637")

        # $1,000
        option_334_deductible_632_1k = self.driver.find_element(By.ID, "option-334-deductible-632")

        # $2,500
        option_334_deductible_633_2pt5k = self.driver.find_element(By.ID, "option-334-deductible-633")

        # $5,000
        option_334_deductible_634_5k = self.driver.find_element(By.ID, "option-334-deductible-634")

        # $10,000
        option_334_deductible_635_10k = self.driver.find_element(By.ID, "option-334-deductible-635")

        # $25,000
        option_334_deductible_636_25k = self.driver.find_element(By.ID, "option-334-deductible-636")

        # Select Limit and Deductible
        option_312_limit_1760_1MM_pci.click()
        option_312_deductible_620_2pt5k.click()

    def select_no_PCI_DSS_limits_deductibles_on_coverage_options(self):
            # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

            # Limits

            # $500,000 (Full Sublimits) ($500K PCI)
            option_334_limit_1746_500K_pci = self.driver.find_element(By.ID, "option-334-limit-1746")

            # $1,000,000 (Full Sublimits) ($1MM PCI)
            option_334_limit_1747_1MM_pci = self.driver.find_element(By.ID, "option-334-limit-1747")

            # $2,000,000 (Full Sublimits) ($2MM PCI)
            option_334_limit_1748_2MM_pci = self.driver.find_element(By.ID, "option-334-limit-1748")

            # Deductibles

            # $500
            option_334_deductible_637_500 = self.driver.find_element(By.ID, "option-334-deductible-637")

            # $1,000
            option_334_deductible_632_1k = self.driver.find_element(By.ID, "option-334-deductible-632")

            # $2,500
            option_334_deductible_633_2pt5k = self.driver.find_element(By.ID, "option-334-deductible-633")

            # $5,000
            option_334_deductible_634_5k = self.driver.find_element(By.ID, "option-334-deductible-634")

            # $10,000
            option_334_deductible_635_10k = self.driver.find_element(By.ID, "option-334-deductible-635")

            # $25,000
            option_334_deductible_636_25k = self.driver.find_element(By.ID, "option-334-deductible-636")

            # Select Limit and Deductible
            option_334_limit_1747_1MM_pci.click()
            option_334_deductible_633_2pt5k.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()