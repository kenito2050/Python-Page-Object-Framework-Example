from selenium.webdriver.common.by import By

class No_PCI_Doctor_Count_5_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 500K/2.5MM
        self.option_851_limit_3179 = self.driver.find_element(By.ID, "option-851-limit-3179")

        # 1MM/5MM
        self.option_851_limit_3174 = self.driver.find_element(By.ID, "option-851-limit-3174")

        # Deductibles
        # $0
        self.option_851_deductible_1297 = self.driver.find_element(By.ID, "option-851-deductible-1297")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_500K_2_pt_5_MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_5_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3179.click()
        No_PCI_Doctor_Count_5_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_1297.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_1MM_5MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_5_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3174.click()
        No_PCI_Doctor_Count_5_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_1297.click()