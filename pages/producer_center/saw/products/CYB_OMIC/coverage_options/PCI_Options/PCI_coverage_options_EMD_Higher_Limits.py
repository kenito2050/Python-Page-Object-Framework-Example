from selenium.webdriver.common.by import By

class PCI_Coverage_Options_eMD_Higher_Limits():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # e-MD™ Only

        # Limits

        # 500K/1MM
        self.option_224_limit_762 = self.driver.find_element(By.ID, "option-224-limit-762")

        # 1MM/1MM
        self.option_224_limit_757 = self.driver.find_element(By.ID, "option-224-limit-757")

        # Deductibles
        # $0
        self.option_451_deductible_763 = self.driver.find_element(By.ID, "option-451-deductible-763")


        # $2M e-MD™ Only

        # Limits

        # 2MM/2MM
        self.option_853_limit_3187 = self.driver.find_element(By.ID, "option-853-limit-3187")

        # Deductibles
        # $0
        self.option_853_deductible_763 = self.driver.find_element(By.ID, "option-853-deductible-763")

        # $3M e-MD™ Only

        # Limits

        # 3MM/3MM
        self.option_852_limit_3186 = self.driver.find_element(By.ID, "option-852-limit-3186")

        # Deductibles
        # $0
        self.option_852_deductible_763 = self.driver.find_element(By.ID, "option-852-deductible-763")


        # $2M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 2MM/2MM
        self.option_854_limit_3189 = self.driver.find_element(By.ID, "option-854-limit-3189")

        # Deductibles
        # $0
        self.option_854_deductible_1297 = self.driver.find_element(By.ID, "option-854-deductible-1297")

        # $3M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 3MM/3MM
        self.option_855_limit_3193 = self.driver.find_element(By.ID, "option-855-limit-3193")

        # Deductibles
        # $0
        self.option_855_deductible_762 = self.driver.find_element(By.ID, "option-855-deductible-762")


        return self

    def select_eMD_Only_500K_1MM_limit_0_Deduct(self):
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_224_limit_762.click()
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_451_deductible_763.click()

    def select_eMD_Only_1MM_1MM_limit_0_Deduct(self):
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_224_limit_757.click()
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_451_deductible_763.click()

    def select_2M_eMD_Only_2MM_2MM_limit_0_Deduct(self):
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_853_limit_3187.click()
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_853_deductible_763.click()

    def select_3M_eMD_Only_3MM_3MM_limit_0_Deduct(self):
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_852_limit_3186.click()
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_852_deductible_763.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_2MM_2MM_limit_0_Deduct(self):
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_854_limit_3189.click()
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_854_deductible_1297.click()

    def select_3M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_3MM_3MM_limit_0_Deduct(self):
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_855_limit_3193.click()
        PCI_Coverage_Options_eMD_Higher_Limits.PageElements(self).option_855_deductible_762.click()