from selenium.webdriver.common.by import By

class PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits():

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

        # e-MD™ Only

        # Limits

        # 1MM/1MM
        self.option_878_limit_3229 = self.driver.find_element(By.ID, "option-878-limit-3229")

        # Deductibles
        # $1,000
        self.option_878_deductible_1042 = self.driver.find_element(By.ID, "option-878-deductible-1042")


        # $2M e-MD™ Only

        # Limits

        # 2MM/2MM
        self.option_860_limit_3205 = self.driver.find_element(By.ID, "option-860-limit-3205")

        # Deductibles
        # $0
        self.option_860_deductible_1042 = self.driver.find_element(By.ID, "option-860-deductible-1042")

        # $3M e-MD™ Only

        # Limits

        # 3MM/3MM
        self.option_861_limit_3206 = self.driver.find_element(By.ID, "option-861-limit-3206")

        # Deductibles
        # $0
        self.option_861_deductible_1042 = self.driver.find_element(By.ID, "option-861-deductible-1042")

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 1MM/1MM
        self.option_879_limit_3230 = self.driver.find_element(By.ID, "option-879-limit-3230")

        # Deductibles
        # $1,000
        self.option_879_deductible_1044 = self.driver.find_element(By.ID, "option-879-deductible-1044")

        # $2M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 2MM/2MM
        self.option_862_limit_3250 = self.driver.find_element(By.ID, "option-862-limit-3250")

        # Deductibles
        # $0
        self.option_862_deductible_1044 = self.driver.find_element(By.ID, "option-862-deductible-1044")

        # $3M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 3MM/3MM
        self.option_863_limit_3251 = self.driver.find_element(By.ID, "option-863-limit-3251")

        # Deductibles
        # $0
        self.option_863_deductible_1044 = self.driver.find_element(By.ID, "option-863-deductible-1044")


        return self

    def select_eMD_Only_1MM_1MM_limit_1K_Deduct(self):
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_878_limit_3229.click()
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_878_deductible_1042.click()

    def select_2M_eMD_Only_2MM_2MM_limit_1K_Deduct(self):
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_860_limit_3205.click()
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_860_deductible_1042.click()

    def select_3M_eMD_Only_3MM_3MM_limit_1K_Deduct(self):
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_861_limit_3206.click()
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_861_deductible_1042.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_1MM_limit_1K_Deduct(self):
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_879_limit_3230.click()
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_879_deductible_1044.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_2MM_2MM_limit_0_Deduct(self):
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_862_limit_3250.click()
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_862_deductible_1044.click()

    def select_3M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_3MM_3MM_limit_0_Deduct(self):
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_863_limit_3251.click()
        PCI_Coverage_Options_Broad_Regulatory_eMD_Higher_Limits.PageElements(self).option_863_deductible_1044.click()