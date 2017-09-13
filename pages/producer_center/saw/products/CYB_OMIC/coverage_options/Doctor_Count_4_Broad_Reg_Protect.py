from selenium.webdriver.common.by import By

class Doctor_Count_4_Broad_Reg_Protect():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus Only

        # Limits

        # 500K/2MM
        self.option_224_limit_764 = self.driver.find_element(By.ID, "option-224-limit-764")

        # 1MM/4MM
        self.option_224_limit_759 = self.driver.find_element(By.ID, "option-224-limit-759")

        # Deductibles
        # $0
        self.option_224_deductible_286 = self.driver.find_element(By.ID, "option-224-deductible-286")


        return self

    def select_Broad_Regulatory_Protection_Plus_Only_500K_2MM_limit_0_Deduct(self):
        Doctor_Count_4_Broad_Reg_Protect.PageElements(self).option_224_limit_764.click()
        Doctor_Count_4_Broad_Reg_Protect.PageElements(self).option_224_deductible_286.click()

    def select_Broad_Regulatory_Protection_Plus_Only_1MM_4MM_limit_0_Deduct(self):
        Doctor_Count_4_Broad_Reg_Protect.PageElements(self).option_224_limit_759.click()
        Doctor_Count_4_Broad_Reg_Protect.PageElements(self).option_224_deductible_286.click()