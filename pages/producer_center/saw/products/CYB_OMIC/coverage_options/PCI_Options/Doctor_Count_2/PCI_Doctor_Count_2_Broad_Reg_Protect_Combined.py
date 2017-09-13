from selenium.webdriver.common.by import By

class PCI_Doctor_Count_2_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 500K/500K
        self.option_452_limit_1996 = self.driver.find_element(By.ID, "option-452-limit-1996")

        # 1MM/1MM
        self.option_452_limit_1991 = self.driver.find_element(By.ID, "option-452-limit-1991")

        # Deductibles
        # $0
        self.option_452_deductible_762 = self.driver.find_element(By.ID, "option-452-deductible-762")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_500K_1MM_limit_0_Deduct(self):
        PCI_Doctor_Count_2_Broad_Reg_Protect_Combined.PageElements(self).option_452_limit_1996.click()
        PCI_Doctor_Count_2_Broad_Reg_Protect_Combined.PageElements(self).option_452_deductible_762.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_2MM_limit_0_Deduct(self):
        PCI_Doctor_Count_2_Broad_Reg_Protect_Combined.PageElements(self).option_452_limit_1991.click()
        PCI_Doctor_Count_2_Broad_Reg_Protect_Combined.PageElements(self).option_452_deductible_762.click()