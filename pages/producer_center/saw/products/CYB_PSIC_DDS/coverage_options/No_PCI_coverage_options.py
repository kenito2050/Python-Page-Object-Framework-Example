from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Regulatory Proceedings Only Enhanced

        # Limits
        # 250K / 250K
        self.option_174_limit_491 = self.driver.find_element(By.ID, "option-174-limit-491")

        # 500K / 500K
        self.option_174_limit_490 = self.driver.find_element(By.ID, "option-174-limit-490")

        # 1MM / 1MM
        self.option_174_limit_489 = self.driver.find_element(By.ID, "option-174-limit-489")

        # Deductibles
        # $1,000
        self.option_174_deductible_134 = self.driver.find_element(By.ID, "option-174-deductible-134")

        # Network Security & Privacy Only Enhanced - No PCI

        # Limits
        # 250K / 250K
        self.option_684_limit_2782 = self.driver.find_element(By.ID, "option-684-limit-2782")

        # 500K / 500K
        self.option_684_limit_2781 = self.driver.find_element(By.ID, "option-684-limit-2781")

        # 1MM / 1MM
        self.option_684_limit_2780 = self.driver.find_element(By.ID, "option-684-limit-2780")

        # Deductibles
        # $0
        self.option_684_deductible_1199 = self.driver.find_element(By.ID, "option-684-deductible-1199")


        # Regulatory Proceedings and Network Security & Privacy Combined Enhanced - No PCI

        # Limits
        # 250K / 250K
        self.option_685_limit_2785 = self.driver.find_element(By.ID, "option-685-limit-2785")

        # 500K / 500K
        self.option_685_limit_2784 = self.driver.find_element(By.ID, "option-685-limit-2784")

        # 1MM / 1MM
        self.option_685_limit_2783 = self.driver.find_element(By.ID, "option-685-limit-2783")

        # Deductibles
        # $0 / $1,000
        self.option_685_deductible_1200 = self.driver.find_element(By.ID, "option-685-deductible-1200")

        return self

    # saw_CC_No_PCI.select_Regulatory_Proceedings_Only_Enhanced_250K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_Only_Enhanced_500K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_Only_Enhanced_1MM_limit()
    # saw_CC_No_PCI.select_Network_Security_Privacy_Only_Enhanced_No_PCI_250K_limit()
    # saw_CC_No_PCI.select_Network_Security_Privacy_Only_Enhanced_No_PCI_500K_limit()
    # saw_CC_No_PCI.select_Network_Security_Privacy_Only_Enhanced_No_PCI_1MM_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_No_PCI_250K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_No_PCI_500K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_No_PCI_1MM_limit()

    def select_Regulatory_Proceedings_Only_Enhanced_250K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_174_limit_491.click()
        No_PCI_Coverage_Options.PageElements(self).option_174_deductible_134.click()

    def select_Regulatory_Proceedings_Only_Enhanced_500K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_174_limit_490.click()
        No_PCI_Coverage_Options.PageElements(self).option_174_deductible_134.click()

    def select_Regulatory_Proceedings_Only_Enhanced_1MM_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_174_limit_489.click()
        No_PCI_Coverage_Options.PageElements(self).option_174_deductible_134.click()

    def select_Network_Security_Privacy_Only_Enhanced_No_PCI_250K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_684_limit_2782.click()
        No_PCI_Coverage_Options.PageElements(self).option_684_deductible_1199.click()

    def select_Network_Security_Privacy_Only_Enhanced_No_PCI_500K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_684_limit_2781.click()
        No_PCI_Coverage_Options.PageElements(self).option_684_deductible_1199.click()

    def select_Network_Security_Privacy_Only_Enhanced_No_PCI_1MM_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_684_limit_2780.click()
        No_PCI_Coverage_Options.PageElements(self).option_684_deductible_1199.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_No_PCI_250K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_685_limit_2785.click()
        No_PCI_Coverage_Options.PageElements(self).option_685_deductible_1200.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_No_PCI_500K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_685_limit_2784.click()
        No_PCI_Coverage_Options.PageElements(self).option_685_deductible_1200.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_No_PCI_1MM_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_685_limit_2783.click()
        No_PCI_Coverage_Options.PageElements(self).option_685_deductible_1200.click()