from selenium.webdriver.common.by import By

class No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 500K/500K
        self.option_851_limit_3175 = self.driver.find_element(By.ID, "option-851-limit-3175")

        # 1MM/1MM
        self.option_851_limit_3170 = self.driver.find_element(By.ID, "option-851-limit-3170")

        # Deductibles
        # $0
        self.option_851_deductible_762 = self.driver.find_element(By.ID, "option-851-deductible-1297")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_500K_500K_limit_0_Deduct(self):
        No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3175.click()
        No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_762.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_1MM_1MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3170.click()
        No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_762.click()