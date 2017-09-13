from selenium.webdriver.common.by import By

class Doctor_Count_2_Broad_Reg_Protect():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus Only

        # Limits

        # 500K/500K
        self.option_224_limit_762 = self.driver.find_element(By.ID, "option-224-limit-762")

        # 1MM/1MM
        self.option_224_limit_757 = self.driver.find_element(By.ID, "option-224-limit-757")

        # Deductibles
        # $0
        self.option_224_deductible_286 = self.driver.find_element(By.ID, "option-224-deductible-286")

        return self

    def select_Broad_Regulatory_Protection_Plus_Only_500K_1MM_limit_0_Deduct(self):
        Doctor_Count_2_Broad_Reg_Protect.PageElements(self).option_224_limit_762.click()
        Doctor_Count_2_Broad_Reg_Protect.PageElements(self).option_224_deductible_286.click()

    def select_Broad_Regulatory_Protection_Plus_Only_1MM_2MM_limit_0_Deduct(self):
        Doctor_Count_2_Broad_Reg_Protect.PageElements(self).option_224_limit_757.click()
        Doctor_Count_2_Broad_Reg_Protect.PageElements(self).option_224_deductible_286.click()