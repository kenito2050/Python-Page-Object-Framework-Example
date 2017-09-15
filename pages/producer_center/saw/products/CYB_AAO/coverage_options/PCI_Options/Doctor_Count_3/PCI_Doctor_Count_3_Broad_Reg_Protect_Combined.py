from selenium.webdriver.common.by import By

class PCI_Doctor_Count_3_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 1MM/3MM
        self.option_879_limit_3232 = self.driver.find_element(By.ID, "option-879-limit-3232")

        # Deductibles
        # $1,000
        self.option_879_deductible_1044 = self.driver.find_element(By.ID, "option-879-deductible-1044")

        # $2M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 2MM/3MM
        self.option_862_limit_3208 = self.driver.find_element(By.ID, "option-862-limit-3208")

        # Deductibles
        # $0
        self.option_862_deductible_1044 = self.driver.find_element(By.ID, "option-862-deductible-1044")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_3MM_limit_1K_Deduct(self):
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_879_limit_3232.click()
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_879_deductible_1044.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_2MM_2MM_limit_0_Deduct(self):
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_862_limit_3208.click()
        PCI_Doctor_Count_3_Broad_Reg_Protect_Combined.PageElements(self).option_862_deductible_1044.click()