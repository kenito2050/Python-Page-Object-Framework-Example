from selenium.webdriver.common.by import By

class No_PCI_Doctor_Count_3_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 500K/1.5MM
        self.option_851_limit_3177 = self.driver.find_element(By.ID, "option-851-limit-3177")

        # 1MM/3MM
        self.option_851_limit_3172 = self.driver.find_element(By.ID, "option-851-limit-3172")

        # Deductibles
        # $0
        self.option_851_deductible_762 = self.driver.find_element(By.ID, "option-452-deductible-762")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_500K_1_pt_5_MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3177.click()
        No_PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_762.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_1MM_3MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3172.click()
        No_PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_762.click()