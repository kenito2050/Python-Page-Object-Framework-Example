from selenium.webdriver.common.by import By

class PCI_Doctor_Count_2_Broad_Reg_Protect_Combined():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Broad Regulatory Protection Plus and e-MD™ Combined

        # Limits

        # 1MM/2MM
        self.option_879_limit_3231 = self.driver.find_element(By.ID, "option-879-limit-3231")

        # Deductibles
        # $1,000
        self.option_879_deductible_1044 = self.driver.find_element(By.ID, "option-879-deductible-1044")

        return self

    def select_Broad_Regulatory_Protection_Plus_and_eMD_Combined_Only_1MM_2MM_limit_1K_Deduct(self):
        PCI_Doctor_Count_2_Broad_Reg_Protect_Combined.PageElements(self).option_879_limit_3231.click()
        PCI_Doctor_Count_2_Broad_Reg_Protect_Combined.PageElements(self).option_879_deductible_1044.click()