from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # CyberRisk Only

        # Limits
        # 1MM/1MM
        self.option_746_limit_2912 = self.driver.find_element(By.ID, "option-746-limit-2912")

        # Deductibles
        # $50,000
        self.option_746_deductible_1227 = self.driver.find_element(By.ID, "option-746-deductible-1227")

        return self

    def select_CyberRisk_Only(self):
        PCI_Coverage_Options.PageElements(self).option_746_limit_2912.click()
        PCI_Coverage_Options.PageElements(self).option_746_deductible_1227.click()