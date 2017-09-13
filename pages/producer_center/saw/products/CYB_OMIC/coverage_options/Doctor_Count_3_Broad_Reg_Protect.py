from selenium.webdriver.common.by import By

class Doctor_Count_3_Broad_Reg_Protect():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus Only

        # Limits

        # 500K/1.5MM
        self.option_224_limit_763 = self.driver.find_element(By.ID, "option-224-limit-763")

        # 1MM/3MM
        self.option_224_limit_758 = self.driver.find_element(By.ID, "option-224-limit-758")

        # Deductibles
        # $0
        self.option_224_deductible_286 = self.driver.find_element(By.ID, "option-224-deductible-286")

        return self

    def select_Broad_Regulatory_Protection_Plus_Only_500K_1_pt_5_MM_limit_0_Deduct(self):
        Doctor_Count_3_Broad_Reg_Protect.PageElements(self).option_224_limit_763.click()
        Doctor_Count_3_Broad_Reg_Protect.PageElements(self).option_224_deductible_286.click()

    def select_Broad_Regulatory_Protection_Plus_Only_1MM_3MM_limit_0_Deduct(self):
        Doctor_Count_3_Broad_Reg_Protect.PageElements(self).option_224_limit_758.click()
        Doctor_Count_3_Broad_Reg_Protect.PageElements(self).option_224_deductible_286.click()