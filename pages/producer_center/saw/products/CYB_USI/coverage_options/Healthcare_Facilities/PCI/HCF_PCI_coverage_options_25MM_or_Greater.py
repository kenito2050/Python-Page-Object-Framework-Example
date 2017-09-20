from selenium.webdriver.common.by import By

class HCF_PCI_Coverage_Options_25MM_or_Greater():

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

        # USI PrivaSafe Only

        # Limits
        # 1MM/1MM
        self.option_539_limit_2386 = self.driver.find_element(By.ID, "option-539-limit-2386")

        # Deductibles
        # $5,000
        self.option_539_deductible_922 = self.driver.find_element(By.ID, "option-539-deductible-922")

        # $10,000
        self.option_539_deductible_940 = self.driver.find_element(By.ID, "option-539-deductible-940")

        # USI PrivaSafe Higher Limits Only without PCI

        # Limits
        # $2,000,000
        self.option_881_limit_2409 = self.driver.find_element(By.ID, "option-881-limit-2409")

        # $3,000,000
        self.option_881_limit_3237 = self.driver.find_element(By.ID, "option-881-limit-3237")

        # Deductibles

        # $5,000
        self.option_881_deductible_922 = self.driver.find_element(By.ID, "option-881-deductible-922")

        # $10,000
        self.option_881_deductible_940 = self.driver.find_element(By.ID, "option-881-deductible-940")

        # USI PrivaSafe with MEDEFENSE™ Plus Combined

        # Limits
        # 1MM/1MM
        self.option_540_limit_2387 = self.driver.find_element(By.ID, "option-540-limit-2387")

        # Deductibles
        # $5,000 / $5,000
        self.option_540_deductible_923 = self.driver.find_element(By.ID, "option-540-deductible-923")

        # $10,000 / $10,000
        self.option_540_deductible_941 = self.driver.find_element(By.ID, "option-540-deductible-941")

        # USI PrivaSafe Higher Limits with MEDEFENSE™ Plus Combined

        # Limits
        # $2,000,000 Privasafe/$1,000,000 Medefense
        self.option_882_limit_2418 = self.driver.find_element(By.ID, "option-882-limit-2418")

        # $3,000,000 Privasafe/$1,000,000 Medefense
        self.option_882_limit_3239 = self.driver.find_element(By.ID, "option-882-limit-3239")

        # Deductibles

        # $5,000
        self.option_882_deductible_923 = self.driver.find_element(By.ID, "option-882-deductible-923")

        # $10,000
        self.option_882_deductible_941 = self.driver.find_element(By.ID, "option-882-deductible-941")

        return self

        ### Revenue Between 10MM and 25MM

    def select_USI_PrivaSafe_MEDEFENSE_Plus_Only_1MM_1MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_538_limit_2384.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_538_deductible_924.click()

    def select_USI_PrivaSafe_Only_1MM_1MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_539_limit_2386.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_539_deductible_940.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_2MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_881_limit_2409.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_881_deductible_940.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_3MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_881_limit_3237.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_881_deductible_940.click()

    def select_USI_PrivaSafe_with_MEDEFENSE_Plus_Combined_1MM_1MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_540_limit_2387.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_540_deductible_941.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_2MM_1MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_882_limit_3239.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_882_deductible_941.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_3MM_1MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_882_limit_3239.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_882_deductible_941.click()