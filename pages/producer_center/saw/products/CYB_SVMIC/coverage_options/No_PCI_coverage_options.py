from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

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

        # e-MD™ Only - No PCI
        # 1MM/1MM
        self.option_653_limit_2722 = self.driver.find_element(By.ID, "option-653-limit-2722")

        # $0
        self.option_653_deductible_1170 = self.driver.find_element(By.ID, "option-653-deductible-1170")


        # MEDEFENSE™ Plus and e-MD™ Combined - No PCI
        # 1MM/1MM
        self.option_655_limit_2724 = self.driver.find_element(By.ID, "option-655-limit-2724")

        # $0
        self.option_655_deductible_1172 = self.driver.find_element(By.ID, "option-655-deductible-1172")



        return self

    def select_MEDEFENSE_Plus_Only(self):
        No_PCI_Coverage_Options.PageElements(self).option_651_limit_2720.click()
        No_PCI_Coverage_Options.PageElements(self).option_651_deductible_1168.click()

    def select_e_MD_Only_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_653_limit_2722.click()
        No_PCI_Coverage_Options.PageElements(self).option_653_deductible_1170.click()

    def select_MEDEFENSE_Plus_and_e_MD_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_655_limit_2724.click()
        No_PCI_Coverage_Options.PageElements(self).option_655_deductible_1172.click()