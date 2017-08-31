from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options_Before_Sep_6_2017():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Medefense™ Plus with $100,000 Disciplinary Proceedings Sublimit

        # Limits
        # 1MM/1MM
        self.option_479_limit_2136 = self.driver.find_element(By.ID, "option-479-limit-2136")

        # Deductibles
        # $0
        self.option_479_deductible_801 = self.driver.find_element(By.ID, "option-479-deductible-801")

        # TMLT Enhanced Cyber Liability with PCI and Cyber Crime Sublimit

        # Limits
        # 1MM/1MM
        self.option_481_limit_2139 = self.driver.find_element(By.ID, "option-481-limit-2139")

        # Deductibles
        # $0/$2,500
        self.option_481_deductible_805 = self.driver.find_element(By.ID, "option-481-deductible-805")

        # Medefense™ Plus with $100K Disciplinary Proceedings Sublimit and Enhanced Cyber Liability with PCI and Cyber Crime Sublimit

        # Limits
        # 1MM/2MM
        self.option_483_limit_2141 = self.driver.find_element(By.ID, "option-483-limit-2141")

        # Deductibles
        # $0/$0/$2,500
        self.option_483_deductible_807 = self.driver.find_element(By.ID, "option-483-deductible-807")

        return self


    def select_Medefense_Plus_with_100K_Disciplinary_Proceedings_Sublimit_1M_Limit_0_Deduct(self):
        No_PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_479_limit_2136.click()
        No_PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_479_deductible_801.click()

    def select_TMLT_Enhanced_Cyber_Liability_with_PCI_and_Cyber_Crime_Sublimit_1M_Limit_0_2pt5k_Deduct(self):
        No_PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_481_limit_2139.click()
        No_PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_481_deductible_805.click()

    def select_Medefense_Plus_with_100K_Disciplinary_Proceedings_Sublimit_Enhanced_Cyber_Liability_with_PCI_and_Cyber_Crime_Sublimit_1M_Limit_0_0_2pt5k_Deduct(self):
        No_PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_483_limit_2141.click()
        No_PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_483_deductible_807.click()