from selenium.webdriver.common.by import By

class HCF_No_PCI_Coverage_Options_25MM_or_Greater():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # USI PrivaSafe MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_538_limit_2384 = self.driver.find_element(By.ID, "option-538-limit-2384")

        # Deductibles
        # $5,000
        self.option_538_deductible_924 = self.driver.find_element(By.ID, "option-538-deductible-924")

        # $10,000
        self.option_538_deductible_939 = self.driver.find_element(By.ID, "option-538-deductible-939")

        # USI PrivaSafe Only without PCI

        # Limits
        # 1MM/1MM
        self.option_541_limit_2389 = self.driver.find_element(By.ID, "option-541-limit-2389")

        # Deductibles

        # $5,000
        self.option_541_deductible_927 = self.driver.find_element(By.ID, "option-541-deductible-927")

        # $10,000
        self.option_541_deductible_942 = self.driver.find_element(By.ID, "option-541-deductible-942")

        # USI PrivaSafe Higher Limits Only without PCI

        # Limits
        # $2,000,000
        self.option_883_limit_2410 = self.driver.find_element(By.ID, "option-883-limit-2410")

        # $3,000,000
        self.option_883_limit_3238 = self.driver.find_element(By.ID, "option-883-limit-3238")

        # Deductibles

        # $5,000
        self.option_883_deductible_927 = self.driver.find_element(By.ID, "option-883-deductible-927")

        # $10,000
        self.option_883_deductible_942 = self.driver.find_element(By.ID, "option-883-deductible-942")

        # USI PrivaSafe with MEDEFENSE™ Plus Combined without PCI

        # Limits
        # 1MM/1MM
        self.option_542_limit_2390 = self.driver.find_element(By.ID, "option-542-limit-2390")

        # Deductibles

        # $5,000 / $5,000
        self.option_542_deductible_928 = self.driver.find_element(By.ID, "option-542-deductible-928")

        # $10,000 / $10,000
        self.option_542_deductible_943 = self.driver.find_element(By.ID, "option-542-deductible-943")

        # USI PrivaSafe Higher Limits with MEDEFENSE™ Plus Combined without PCI

        # Limits
        # $2,000,000 Privasafe/$1,000,000 Medefense
        self.option_884_limit_2419 = self.driver.find_element(By.ID, "option-884-limit-2419")

        # $3,000,000 Privasafe/$1,000,000 Medefense
        self.option_884_limit_3240 = self.driver.find_element(By.ID, "option-884-limit-3240")

        # Deductibles

        # $5,000 / $5,000
        self.option_884_deductible_928 = self.driver.find_element(By.ID, "option-884-deductible-928")

        # $10,000 / $10,000
        self.option_884_deductible_943 = self.driver.find_element(By.ID, "option-884-deductible-943")

        return self
    ### Revenue Greater than 25MM

    def select_USI_PrivaSafe_MEDEFENSE_Plus_Only_1MM_1MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_538_limit_2384.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_538_deductible_939.click()

    def select_USI_PrivaSafe_Only_without_PCI_1MM_1MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_541_limit_2389.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_541_deductible_942.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_without_PCI_2MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_883_limit_2410.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_883_deductible_942.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_without_PCI_3MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_883_limit_3238.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_883_deductible_942.click()

    def select_USI_PrivaSafe_with_MEDEFENSE_Plus_Combined_without_PCI_1MM_1MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_542_limit_2390.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_542_deductible_943.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_without_PCI_2MM_1MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_884_limit_2419.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_884_deductible_943.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_without_PCI_3MM_1MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_884_limit_3240.click()
        HCF_No_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_884_deductible_943.click()