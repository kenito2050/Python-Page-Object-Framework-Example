from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits

        # 1MM/1MM
        self.option_507_limit_2294 = self.driver.find_element(By.ID, "option-507-limit-2294")

        # Deductibles
        # $0
        self.option_507_deductible_877 = self.driver.find_element(By.ID, "option-507-deductible-877")


        # CyberProtector™ Only with Crime - No PCI

        # Limits

        # 1MM/1MM
        self.option_1051_limit_4019 = self.driver.find_element(By.ID, "option-1051-limit-4019")

        # Deductibles
        # $0
        self.option_1051_deductible_1592 = self.driver.find_element(By.ID, "option-1051-deductible-1592")

        # MEDEFENSE™ Plus and CyberProtector™ Combined with Crime - No PCI

        # Limits

        # 3MM/3MM
        self.option_1052_limit_4020 = self.driver.find_element(By.ID, "option-1052-limit-4020")

        # Deductibles
        # $0
        self.option_1052_deductible_1589 = self.driver.find_element(By.ID, "option-1052-deductible-1589")

        return self

    def select_CyberProtector_Only_with_Crime_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_507_limit_2294.click()
        No_PCI_Coverage_Options.PageElements(self).option_507_deductible_877.click()