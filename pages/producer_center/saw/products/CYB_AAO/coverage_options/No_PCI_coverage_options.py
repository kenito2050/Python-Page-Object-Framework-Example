from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_789_limit_3095 = self.driver.find_element(By.ID, "option-789-limit-3095")

        # Deductibles
        # $0
        self.option_789_deductible_1242 = self.driver.find_element(By.ID, "option-789-deductible-1242")

        # Cyber Liability Only - No PCI

        # Limits
        # 1MM/1MM
        self.option_796_limit_3100 = self.driver.find_element(By.ID, "option-796-limit-3100")

        # Deductibles
        # $0 / $2,500
        self.option_796_deductible_1247 = self.driver.find_element(By.ID, "option-796-deductible-1247")

        # MEDEFENSE™ Plus with $100,000 Medical Board Proceedings Sublimit

        # Limits
        # 1MM/100K/1MM
        self.option_790_limit_3096 = self.driver.find_element(By.ID, "option-790-limit-3096")

        # Deductibles
        # $0/$1,000
        self.option_790_deductible_1243 = self.driver.find_element(By.ID, "option-790-deductible-1243")

        # MEDEFENSE™ Plus and Cyber Liability - No PCI

        # Limits
        # 1MM/1MM
        self.option_797_limit_3101 = self.driver.find_element(By.ID, "option-797-limit-3101")

        # Deductibles
        # $0/$2,500
        self.option_797_deductible_1248 = self.driver.find_element(By.ID, "option-797-deductible-1248")

        # MEDEFENSE™ Plus with $100K Medical Board Proceedings Sublimit and Cyber Liability - No PCI

        # Limits
        # 1MM/100K/1MM
        self.option_798_limit_3102 = self.driver.find_element(By.ID, "option-798-limit-3102")

        # Deductibles
        # $0/$1,000/$2,500
        self.option_798_deductible_1249 = self.driver.find_element(By.ID, "option-798-deductible-1249")

        return self

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_789_limit_3095.click()
        No_PCI_Coverage_Options.PageElements(self).option_789_deductible_1242.click()

    def select_Cyber_Liability_Only_No_PCI_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_796_limit_3100.click()
        No_PCI_Coverage_Options.PageElements(self).option_796_deductible_1247.click()

    def select_MEDEFENSE_Plus_with_100K_Medical_Board_Proceedings_Sublimit_1MM_100K_1M_limit_0_1K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_790_limit_3096.click()
        No_PCI_Coverage_Options.PageElements(self).option_790_deductible_1243.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_No_PCI_1MM_1M_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_797_limit_3101.click()
        No_PCI_Coverage_Options.PageElements(self).option_797_deductible_1248.click()

    def select_MEDEFENSE_Plus_with_100K_Medical_Board_Proceedings_Sublimit_and_Cyber_Liability_No_PCI_1MM_1M_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_798_limit_3102.click()
        No_PCI_Coverage_Options.PageElements(self).option_798_deductible_1249.click()