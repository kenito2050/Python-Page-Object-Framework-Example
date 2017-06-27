from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

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

        # Network Security & Privacy Only - No PCI

        # Limits
        # 250K / 250K
        self.option_688_limit_2803 = self.driver.find_element(By.ID, "option-688-limit-2803")

        # 500K / 500K
        self.option_688_limit_2804 = self.driver.find_element(By.ID, "option-688-limit-2804")

        # 1MM / 1MM
        self.option_688_limit_2805 = self.driver.find_element(By.ID, "option-688-limit-2805")

        # Deductibles
        # $0
        self.option_688_deductible_1203 = self.driver.find_element(By.ID, "option-688-deductible-1203")


        # Regulatory Proceedings and Network Security & Privacy Combined - No PCI

        # Limits
        # 250K / 250K
        self.option_689_limit_2806 = self.driver.find_element(By.ID, "option-689-limit-2806")

        # 500K / 500K
        self.option_689_limit_2807 = self.driver.find_element(By.ID, "option-689-limit-2807")

        # 1MM / 1MM
        self.option_689_limit_2808 = self.driver.find_element(By.ID, "option-689-limit-2808")

        # Deductibles
        # $0 / $0
        self.option_689_deductible_1204 = self.driver.find_element(By.ID, "option-689-deductible-1204")

        return self

    # saw_CC_No_PCI.select_Regulatory_Proceedings_Only_250K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_Only_500K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_Only_1MM_limit()

    # saw_CC_No_PCI.select_Network_Security_Privacy_Only_No_PCI_250K_limit()
    # saw_CC_No_PCI.select_Network_Security_Privacy_Only_No_PCI_500K_limit()
    # saw_CC_No_PCI.select_Network_Security_Privacy_Only_No_PCI_1MM_limit()

    # saw_CC_No_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_No_PCI_250K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_No_PCI_500K_limit()
    # saw_CC_No_PCI.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_No_PCI_1MM_limit()

    def select_Regulatory_Proceedings_Only_250K_limit(self):

        No_PCI_Coverage_Options.PageElements(self).option_171_limit_482.click()
        No_PCI_Coverage_Options.PageElements(self).option_171_deductible_131.click()

    def select_Regulatory_Proceedings_Only_500K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_171_limit_481.click()
        No_PCI_Coverage_Options.PageElements(self).option_171_deductible_131.click()

    def select_Regulatory_Proceedings_Only_1MM_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_171_limit_480.click()
        No_PCI_Coverage_Options.PageElements(self).option_171_deductible_131.click()

    def select_Network_Security_Privacy_Only_No_PCI_250K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_688_limit_2803.click()
        No_PCI_Coverage_Options.PageElements(self).option_688_deductible_1203.click()

    def select_Network_Security_Privacy_Only_No_PCI_500K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_688_limit_2804.click()
        No_PCI_Coverage_Options.PageElements(self).option_688_deductible_1203.click()

    def select_Network_Security_Privacy_Only_No_PCI_1MM_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_688_limit_2805.click()
        No_PCI_Coverage_Options.PageElements(self).option_688_deductible_1203.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_No_PCI_250K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_689_limit_2806.click()
        No_PCI_Coverage_Options.PageElements(self).option_689_deductible_1204.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_No_PCI_500K_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_689_limit_2807.click()
        No_PCI_Coverage_Options.PageElements(self).option_689_deductible_1204.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_No_PCI_1MM_limit(self):
        No_PCI_Coverage_Options.PageElements(self).option_689_limit_2808.click()
        No_PCI_Coverage_Options.PageElements(self).option_689_deductible_1204.click()