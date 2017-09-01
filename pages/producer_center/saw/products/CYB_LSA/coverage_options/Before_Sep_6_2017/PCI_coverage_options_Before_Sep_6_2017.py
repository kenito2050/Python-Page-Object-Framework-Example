from selenium.webdriver.common.by import By

class PCI_Coverage_Options_Before_Sep_6_2017():

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
        self.option_477_limit_2134 = self.driver.find_element(By.ID, "option-477-limit-2134")

        # Deductibles
        # $0/$2,500
        self.option_477_deductible_802 = self.driver.find_element(By.ID, "option-477-deductible-802")

        # Medefense™ Plus with $100K Disciplinary Proceedings Sublimit and Enhanced Cyber Liability with PCI and Cyber Crime Sublimit

        # Limits
        # 1MM/2MM
        self.option_478_limit_2135 = self.driver.find_element(By.ID, "option-478-limit-2135")

        # Deductibles
        # $0/$0/$2,500
        self.option_478_deductible_803 = self.driver.find_element(By.ID, "option-478-deductible-803")

        return self


    def select_Medefense_Plus_with_100K_Disciplinary_Proceedings_Sublimit_1M_Limit_0_Deduct(self):
        PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_479_limit_2136.click()
        PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_479_deductible_801.click()

    def select_TMLT_Enhanced_Cyber_Liability_with_PCI_and_Cyber_Crime_Sublimit_1M_Limit_0_2pt5k_Deduct(self):
        PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_477_limit_2134.click()
        PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_477_deductible_802.click()

    def select_Medefense_Plus_with_100K_Disciplinary_Proceedings_Sublimit_Enhanced_Cyber_Liability_with_PCI_and_Cyber_Crime_Sublimit_1M_Limit_0_0_2pt5k_Deduct(self):
        PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_478_limit_2135.click()
        PCI_Coverage_Options_Before_Sep_6_2017.PageElements(self).option_478_deductible_803.click()