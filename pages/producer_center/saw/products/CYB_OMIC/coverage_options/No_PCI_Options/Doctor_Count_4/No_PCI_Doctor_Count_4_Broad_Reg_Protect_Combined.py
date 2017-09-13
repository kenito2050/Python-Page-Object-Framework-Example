from selenium.webdriver.common.by import By

class No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 500K/2MM
        self.option_851_limit_3178 = self.driver.find_element(By.ID, "option-851-limit-3178")

        # 1MM/4MM
        self.option_851_limit_3173 = self.driver.find_element(By.ID, "option-851-limit-3173")

        # Deductibles
        # $0
        self.option_851_deductible_762 = self.driver.find_element(By.ID, "option-452-deductible-762")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_500K_2MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3178.click()
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_762.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_No_PCI_1MM_4MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_851_limit_3173.click()
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_851_deductible_762.click()