from selenium.webdriver.common.by import By

class Doctor_Count_1_Broad_Reg_Protect():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus Only

        # Limits

        # 1MM/1MM
        self.option_227_limit_283 = self.driver.find_element(By.ID, "option-227-limit-283")

        # Deductibles
        # $1,000
        self.option_227_deductible_1041 = self.driver.find_element(By.ID, "option-227-deductible-1041")

        return self

    def select_Broad_Regulatory_Protection_Plus_Only_1MM_1MM_limit_1K_Deduct(self):
        Doctor_Count_1_Broad_Reg_Protect.PageElements(self).option_227_limit_283.click()
        Doctor_Count_1_Broad_Reg_Protect.PageElements(self).option_227_deductible_1041.click()