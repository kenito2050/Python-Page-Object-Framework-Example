from selenium.webdriver.common.by import By

class PCI_Doctor_Count_4_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 500K/2MM
        self.option_452_limit_1998 = self.driver.find_element(By.ID, "option-452-limit-1998")

        # 1MM/4MM
        self.option_452_limit_1993 = self.driver.find_element(By.ID, "option-452-limit-1993")

        # Deductibles
        # $0
        self.option_452_deductible_762 = self.driver.find_element(By.ID, "option-452-deductible-762")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_500K_2MM_limit_0_Deduct(self):
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_452_limit_1998.click()
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_452_deductible_762.click()

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_4MM_limit_0_Deduct(self):
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_452_limit_1993.click()
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_452_deductible_762.click()