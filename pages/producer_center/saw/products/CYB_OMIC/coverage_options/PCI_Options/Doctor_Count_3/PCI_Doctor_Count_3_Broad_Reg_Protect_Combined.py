from selenium.webdriver.common.by import By

class PCI_Doctor_Count_3_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 500K/1.5MM
        self.option_452_limit_1997 = self.driver.find_element(By.ID, "option-452-limit-1997")

        # 1MM/3MM
        self.option_452_limit_1992 = self.driver.find_element(By.ID, "option-452-limit-1992")

        # Deductibles
        # $0
        self.option_452_deductible_762 = self.driver.find_element(By.ID, "option-452-deductible-762")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_500K_1_pt_5_MM_limit_0_Deduct(self):
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_452_limit_1997.click()
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_452_deductible_762.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_3MM_limit_0_Deduct(self):
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_452_limit_1992.click()
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_452_deductible_762.click()