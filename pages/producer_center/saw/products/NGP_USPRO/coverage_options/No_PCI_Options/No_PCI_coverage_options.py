from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # e-MD™ Only - No PCI

        # Limits

        # 500K/1MM
        self.option_850_limit_3169 = self.driver.find_element(By.ID, "option-850-limit-3169")

        # 1MM/1MM
        self.option_850_limit_3168 = self.driver.find_element(By.ID, "option-850-limit-3168")

        # Deductibles
        # $0
        self.option_850_deductible_1296 = self.driver.find_element(By.ID, "option-850-deductible-1296")

        # $2M e-MD™ Only - No PCI

        # Limits

        # 2MM/2MM
        self.option_856_limit_3196 = self.driver.find_element(By.ID, "option-856-limit-3196")

        # Deductibles
        # $0
        self.option_856_deductible_1296 = self.driver.find_element(By.ID, "option-856-deductible-1296")

        # $3M e-MD™ Only - No PCI

        # Limits

        # 3MM/3MM
        self.option_858_limit_3201 = self.driver.find_element(By.ID, "option-858-limit-3201")

        # Deductibles
        # $0
        self.option_858_deductible_1296 = self.driver.find_element(By.ID, "option-858-deductible-1296")

        # $2M Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 2MM/2MM
        self.option_857_limit_3257 = self.driver.find_element(By.ID, "option-857-limit-3257")

        # Deductibles
        # $0
        self.option_857_deductible_1297 = self.driver.find_element(By.ID, "option-857-deductible-1297")

        # $3M Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 3MM/3MM
        self.option_859_limit_3263 = self.driver.find_element(By.ID, "option-859-limit-3263")

        # Deductibles
        # $0
        self.option_859_deductible_1297 = self.driver.find_element(By.ID, "option-859-deductible-1297")

        return self

    def select_eMD_Only_No_PCI_500K_1MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_850_limit_3169.click()
        No_PCI_Coverage_Options.PageElements(self).option_850_deductible_1296.click()

    def select_eMD_Only_No_PCI_1MM_1MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_850_limit_3168.click()
        No_PCI_Coverage_Options.PageElements(self).option_850_deductible_1296.click()

    def select_2M_eMD_Only_No_PCI_2MM_2MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_856_limit_3196.click()
        No_PCI_Coverage_Options.PageElements(self).option_856_deductible_1296.click()

    def select_3M_eMD_Only_No_PCI_3MM_3MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_858_limit_3201.click()
        No_PCI_Coverage_Options.PageElements(self).option_858_deductible_1296.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_2MM_2MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_857_limit_3257.click()
        No_PCI_Coverage_Options.PageElements(self).option_857_deductible_1297.click()

    def select_3M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_3MM_3MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_859_limit_3263.click()
        No_PCI_Coverage_Options.PageElements(self).option_859_deductible_1297.click()