from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_651_limit_2720 = self.driver.find_element(By.ID, "option-651-limit-2720")

        # Deductibles
        # $1,500
        self.option_651_deductible_1168 = self.driver.find_element(By.ID, "option-651-deductible-1168")

        # e-MD™ Only
        # 1MM/1MM
        self.option_652_limit_2721 = self.driver.find_element(By.ID, "option-652-limit-2721")

        # $0
        self.option_652_deductible_1169 = self.driver.find_element(By.ID, "option-652-deductible-1169")


        # MEDEFENSE™ Plus and e-MD™ Combined
        # 1MM/1MM
        self.option_654_limit_2723 = self.driver.find_element(By.ID, "option-654-limit-2723")

        # $0
        self.option_654_deductible_1171 = self.driver.find_element(By.ID, "option-654-deductible-1171")


        return self

    def select_MEDEFENSE_Plus_Only(self):
        PCI_Coverage_Options.PageElements(self).option_651_limit_2720.click()
        PCI_Coverage_Options.PageElements(self).option_651_deductible_1168.click()

    def select_e_MD_Only(self):
        PCI_Coverage_Options.PageElements(self).option_652_limit_2721.click()
        PCI_Coverage_Options.PageElements(self).option_652_deductible_1169.click()

    def select_MEDEFENSE_Plus_and_e_MD(self):
        PCI_Coverage_Options.PageElements(self).option_654_limit_2723.click()
        PCI_Coverage_Options.PageElements(self).option_654_deductible_1171.click()

