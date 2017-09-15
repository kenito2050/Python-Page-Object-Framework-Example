from selenium.webdriver.common.by import By

class No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined - No PCI

        # Limits

        # 1MM/1MM
        self.option_876_limit_3224 = self.driver.find_element(By.ID, "option-876-limit-3224")

        # Deductibles
        # $1,000
        self.option_876_deductible_1299 = self.driver.find_element(By.ID, "option-876-deductible-1299")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_No_PCI_1MM_1MM_limit_1K_Deduct(self):
        No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined.PageElements(self).option_876_limit_3224.click()
        No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined.PageElements(self).option_876_deductible_1299.click()