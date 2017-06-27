from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Regulatory Proceedings Only

        # Limits
        # 250K / 250K
        self.option_171_limit_482 = self.driver.find_element(By.ID, "option-171-limit-482")

        # 500K / 500K
        self.option_171_limit_481 = self.driver.find_element(By.ID, "option-171-limit-481")

        # 1MM / 1MM
        self.option_171_limit_480 = self.driver.find_element(By.ID, "option-171-limit-480")

        # Deductibles
        # $1,000
        self.option_171_deductible_131 = self.driver.find_element(By.ID, "option-171-deductible-131")

        # Network Security & Privacy Only

        # Limits
        # 250K / 250K
        self.option_686_limit_2797 = self.driver.find_element(By.ID, "option-686-limit-2797")

        # 500K / 500K
        self.option_686_limit_2798 = self.driver.find_element(By.ID, "option-686-limit-2798")

        # 1MM / 1MM
        self.option_686_limit_2799 = self.driver.find_element(By.ID, "option-686-limit-2799")

        # Deductibles
        # $0
        self.option_686_deductible_1201 = self.driver.find_element(By.ID, "option-686-deductible-1201")


        # Regulatory Proceedings and Network Security & Privacy Combined

        # Limits
        # 250K / 250K
        self.option_687_limit_2800 = self.driver.find_element(By.ID, "option-687-limit-2800")

        # 500K / 500K
        self.option_687_limit_2801 = self.driver.find_element(By.ID, "option-687-limit-2801")

        # 1MM / 1MM
        self.option_687_limit_2802 = self.driver.find_element(By.ID, "option-687-limit-2802")

        # Deductibles
        # $0 / $0
        self.option_687_deductible_1202 = self.driver.find_element(By.ID, "option-687-deductible-1202")

        return self

    # saw_CC_PCI.select_Regulatory_Proceedings_Only_250K_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_Only_500K_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_Only_1MM_limit()

    # saw_CC_PCI.select_Network_Security_Privacy_Only_250K_limit()
    # saw_CC_PCI.select_Network_Security_Privacy_Only_500K_limit()
    # saw_CC_PCI.select_Network_Security_Privacy_Only_1MM_limit()

    # saw_CC_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_250K_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_500K_limit()
    # saw_CC_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_1MM_limit()

    def select_Regulatory_Proceedings_Only_250K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_171_limit_482.click()
        PCI_Coverage_Options.PageElements(self).option_171_deductible_131.click()

    def select_Regulatory_Proceedings_Only_500K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_171_limit_481.click()
        PCI_Coverage_Options.PageElements(self).option_171_deductible_131.click()

    def select_Regulatory_Proceedings_Only_1MM_limit(self):
        PCI_Coverage_Options.PageElements(self).option_171_limit_480.click()
        PCI_Coverage_Options.PageElements(self).option_171_deductible_131.click()

    def select_Network_Security_Privacy_Only_250K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_686_limit_2797.click()
        PCI_Coverage_Options.PageElements(self).option_686_deductible_1201.click()

    def select_Network_Security_Privacy_Only_500K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_686_limit_2798.click()
        PCI_Coverage_Options.PageElements(self).option_686_deductible_1201.click()

    def select_Network_Security_Privacy_Only_1MM_limit(self):
        PCI_Coverage_Options.PageElements(self).option_686_limit_2799.click()
        PCI_Coverage_Options.PageElements(self).option_686_deductible_1201.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_250K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_687_limit_2800.click()
        PCI_Coverage_Options.PageElements(self).option_687_deductible_1202.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_500K_limit(self):
        PCI_Coverage_Options.PageElements(self).option_687_limit_2801.click()
        PCI_Coverage_Options.PageElements(self).option_687_deductible_1202.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_1MM_limit(self):
        PCI_Coverage_Options.PageElements(self).option_687_limit_2802.click()
        PCI_Coverage_Options.PageElements(self).option_687_deductible_1202.click()