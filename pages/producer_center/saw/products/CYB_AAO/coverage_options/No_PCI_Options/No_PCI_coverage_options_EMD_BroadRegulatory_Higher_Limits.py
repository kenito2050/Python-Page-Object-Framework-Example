from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus Only

        # Limits

        # 1MM/1MM
        self.option_227_limit_283 = self.driver.find_element(By.ID, "option-227-limit-283")

        # Deductibles
        # $1,000
        self.option_227_deductible_1041 = self.driver.find_element(By.ID, "option-227-deductible-1041")

        # e-MD™ Only - No PCI

        # Limits

        # 1MM/1MM
        self.option_875_limit_3223 = self.driver.find_element(By.ID, "option-875-limit-3223")

        # Deductibles
        # $1,000
        self.option_875_deductible_1298 = self.driver.find_element(By.ID, "option-875-deductible-1298")


        # $2M e-MD™ Only - No PCI

        # Limits

        # 2MM/2MM
        self.option_864_limit_3214 = self.driver.find_element(By.ID, "option-864-limit-3214")

        # Deductibles
        # $0
        self.option_864_deductible_1298 = self.driver.find_element(By.ID, "option-864-deductible-1298")

        # $3M e-MD™ Only - No PCI

        # Limits

        # 3MM/3MM
        self.option_866_limit_3219 = self.driver.find_element(By.ID, "option-866-limit-3219")

        # Deductibles
        # $0
        self.option_866_deductible_1298 = self.driver.find_element(By.ID, "option-866-deductible-1298")

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 1MM/1MM
        self.option_876_limit_3224 = self.driver.find_element(By.ID, "option-876-limit-3224")

        # Deductibles
        # $1,000
        self.option_876_deductible_1299 = self.driver.find_element(By.ID, "option-876-deductible-1299")

        # $2M Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 2MM/2MM
        self.option_865_limit_3215 = self.driver.find_element(By.ID, "option-865-limit-3215")

        # Deductibles
        # $0
        self.option_865_deductible_1299 = self.driver.find_element(By.ID, "option-865-deductible-1299")

        # $3M Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 3MM/3MM
        self.option_867_limit_3220 = self.driver.find_element(By.ID, "option-867-limit-3220")

        # Deductibles
        # $0
        self.option_867_deductible_1299 = self.driver.find_element(By.ID, "option-867-deductible-1299")


        return self

    def select_eMD_Only_No_PCI_1MM_1MM_limit_1K_Deduct(self):
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_875_limit_3223.click()
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_875_deductible_1298.click()

    def select_2M_eMD_Only_No_PCI_2MM_2MM_limit_1K_Deduct(self):
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_864_limit_3214.click()
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_864_deductible_1298.click()

    def select_3M_eMD_Only_No_PCI_3MM_3MM_limit_1K_Deduct(self):
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_866_limit_3219.click()
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_866_deductible_1298.click()

    def select_Broad_Regulatory_Protection_Plus_eMD_Combined_No_PCI_1MM_1MM_limit_1K_Deduct(self):
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_876_limit_3224.click()
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_876_deductible_1299.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_2MM_2MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_865_limit_3215.click()
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_865_deductible_1299.click()

    def select_3M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_3MM_3MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_867_limit_3220.click()
        No_PCI_Coverage_Options_eMD_Broad_Regulatory_Higher_Limits.PageElements(self).option_867_deductible_1299.click()