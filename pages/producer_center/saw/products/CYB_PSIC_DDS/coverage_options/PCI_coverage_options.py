from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

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

        # Network Security & Privacy Only Enhanced

        # Limits
        # 250K / 250K
        self.option_682_limit_2776 = self.driver.find_element(By.ID, "option-682-limit-2776")

        # 500K / 500K
        self.option_682_limit_2775 = self.driver.find_element(By.ID, "option-682-limit-2775")

        # 1MM / 1MM
        self.option_682_limit_2774 = self.driver.find_element(By.ID, "option-682-limit-2774")

        # Deductibles
        # $0
        self.option_682_deductible_1197 = self.driver.find_element(By.ID, "option-682-deductible-1197")


        # Regulatory Proceedings and Network Security & Privacy Combined Enhanced

        # Limits
        # 250K / 250K
        self.option_683_limit_2779 = self.driver.find_element(By.ID, "option-683-limit-2779")

        # 500K / 500K
        self.option_683_limit_2778 = self.driver.find_element(By.ID, "option-683-limit-2778")

        # 1MM / 1MM
        self.option_683_limit_2777 = self.driver.find_element(By.ID, "option-683-limit-2777")

        # Deductibles
        # $0 / $1,000
        self.option_683_deductible_1198 = self.driver.find_element(By.ID, "option-683-deductible-1198")

        return self

    # saw_CC_PCI.select_Regulatory_Proceedings_Only_Enhanced_250K_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_Only_Enhanced_500K_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_Only_Enhanced_1MM_limit()
    # saw_CC_PCI.select_Network_Security_Privacy_Only_Enhanced_250K_limit()
    # saw_CC_PCI.select_Network_Security_Privacy_Only_Enhanced_500K_limit()
    # saw_CC_PCI.select_Network_Security_Privacy_Only_Enhanced_1MM_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_250K()
    # saw_CC_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_500K()
    # saw_CC_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_1MM()

    def select_Regulatory_Proceedings_Only_Enhanced_250K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_174_limit_491.click()
        PCI_Coverage_Options.PageElements(self).option_174_deductible_134.click()

    def select_Regulatory_Proceedings_Only_Enhanced_500K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_174_limit_490.click()
        PCI_Coverage_Options.PageElements(self).option_174_deductible_134.click()

    def select_Regulatory_Proceedings_Only_Enhanced_1MM_limit(self):
        PCI_Coverage_Options.PageElements(self).option_174_limit_489.click()
        PCI_Coverage_Options.PageElements(self).option_174_deductible_134.click()

    def select_Network_Security_Privacy_Only_Enhanced_250K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_682_limit_2776.click()
        PCI_Coverage_Options.PageElements(self).option_682_deductible_1197.click()

    def select_Network_Security_Privacy_Only_Enhanced_500K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_682_limit_2775.click()
        PCI_Coverage_Options.PageElements(self).option_682_deductible_1197.click()

    def select_Network_Security_Privacy_Only_Enhanced_1MM_limit(self):
        PCI_Coverage_Options.PageElements(self).option_682_limit_2774.click()
        PCI_Coverage_Options.PageElements(self).option_682_deductible_1197.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_250K(self):
        PCI_Coverage_Options.PageElements(self).option_683_limit_2779.click()
        PCI_Coverage_Options.PageElements(self).option_683_deductible_1198.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_500K(self):
        PCI_Coverage_Options.PageElements(self).option_683_limit_2778.click()
        PCI_Coverage_Options.PageElements(self).option_683_deductible_1198.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_683_limit_2777.click()
        PCI_Coverage_Options.PageElements(self).option_683_deductible_1198.click()