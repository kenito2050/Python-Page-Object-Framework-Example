from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

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


        # CyberProtector™ Only w/ Crime

        # Limits

        # 1MM/1MM
        self.option_1053_limit_4021 = self.driver.find_element(By.ID, "option-1053-limit-4021")

        # Deductibles
        # $0
        self.option_1053_deductible_1590 = self.driver.find_element(By.ID, "option-1053-deductible-1590")

        # MEDEFENSE™ Plus and CyberProtector™ Combined w/ Crime

        # Limits

        # 3MM/3MM
        self.option_1054_limit_4022 = self.driver.find_element(By.ID, "option-1054-limit-4022")

        # Deductibles
        # $0
        self.option_1054_deductible_1591 = self.driver.find_element(By.ID, "option-1054-deductible-1591")


        return self

    def select_CyberProtector_Only(self):
        PCI_Coverage_Options.PageElements(self).option_507_limit_2294.click()
        PCI_Coverage_Options.PageElements(self).option_507_deductible_877.click()