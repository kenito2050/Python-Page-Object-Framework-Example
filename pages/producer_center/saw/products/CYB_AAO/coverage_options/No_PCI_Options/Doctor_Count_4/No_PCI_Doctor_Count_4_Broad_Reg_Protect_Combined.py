from selenium.webdriver.common.by import By

class No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 1MM/4MM
        self.option_876_limit_3227 = self.driver.find_element(By.ID, "option-876-limit-3227")

        # Deductibles
        # $1,000
        self.option_876_deductible_1299 = self.driver.find_element(By.ID, "option-876-deductible-1299")

        # $2M Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 2MM/4MM
        self.option_865_limit_3217 = self.driver.find_element(By.ID, "option-865-limit-3217")

        # Deductibles
        # $0
        self.option_865_deductible_1299 = self.driver.find_element(By.ID, "option-865-deductible-1299")

        # $3M Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 3MM/4MM
        self.option_867_limit_3221 = self.driver.find_element(By.ID, "option-867-limit-3221")

        # Deductibles
        # $0
        self.option_867_deductible_1299 = self.driver.find_element(By.ID, "option-867-deductible-1299")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_1MM_4MM_limit_1K_Deduct(self):
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_876_limit_3227.click()
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_876_deductible_1299.click()

    def select_2M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_2MM_4MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_865_limit_3217.click()
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_865_deductible_1299.click()

    def select_3M_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_3MM_4MM_limit_0_Deduct(self):
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_867_limit_3221.click()
        No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined.PageElements(self).option_867_deductible_1299.click()