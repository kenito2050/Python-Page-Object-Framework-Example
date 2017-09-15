from selenium.webdriver.common.by import By

class PCI_Doctor_Count_4_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 1MM/4MM
        self.option_879_limit_3233 = self.driver.find_element(By.ID, "option-879-limit-3233")

        # Deductibles
        # $1,000
        self.option_879_deductible_1044 = self.driver.find_element(By.ID, "option-879-deductible-1044")

        # $2M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 2MM/4MM
        self.option_862_limit_3209 = self.driver.find_element(By.ID, "option-862-limit-3209")

        # Deductibles
        # $0
        self.option_862_deductible_1044 = self.driver.find_element(By.ID, "option-862-deductible-1044")

        # $3M Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 3MM/4MM
        self.option_863_limit_3212 = self.driver.find_element(By.ID, "option-863-limit-3212")

        # Deductibles
        # $0
        self.option_863_deductible_1044 = self.driver.find_element(By.ID, "option-863-deductible-1044")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_4MM_limit_1K_Deduct(self):
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_879_limit_3233.click()
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_879_deductible_1044.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_2MM_4MM_limit_0_Deduct(self):
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_862_limit_3209.click()
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_862_deductible_1044.click()

    def select_3M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_3MM_4MM_limit_0_Deduct(self):
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_863_limit_3212.click()
        PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_863_deductible_1044.click()