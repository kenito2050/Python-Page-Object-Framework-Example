from selenium.webdriver.common.by import By

class Non_HCF_No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # USI PrivaSafe Medefense™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_538_limit_2384 = self.driver.find_element(By.ID, "option-538-limit-2384")

        # Deductibles
        # $2,500
        self.option_538_deductible_919 = self.driver.find_element(By.ID, "option-538-deductible-919")

        # USI PrivaSafe Only without PCI

        # Limits
        # 1MM/1MM
        self.option_541_limit_2389 = self.driver.find_element(By.ID, "option-541-limit-2389")

        # Deductibles
        # $1,000
        self.option_541_deductible_925 = self.driver.find_element(By.ID, "option-541-deductible-925")

        # USI PrivaSafe Higher Limits Only without PCI

        # Limits
        # 2MM
        self.option_883_limit_2410 = self.driver.find_element(By.ID, "option-883-limit-2410")

        # 3MM
        self.option_883_limit_3238 = self.driver.find_element(By.ID, "option-883-limit-3238")

        # Deductibles
        # $2,500
        self.option_883_deductible_925 = self.driver.find_element(By.ID, "option-883-deductible-925")

        # $5,000
        self.option_883_deductible_927 = self.driver.find_element(By.ID, "option-883-deductible-927")

        # USI PrivaSafe with MEDEFENSE™ Plus Combined without PCI

        # Limits
        # 1MM/1MM/100k Cyber Crime/250k PCI
        self.option_542_limit_2390 = self.driver.find_element(By.ID, "option-542-limit-2390")

        # Deductibles
        # $1,000
        self.option_542_deductible_926 = self.driver.find_element(By.ID, "option-542-deductible-926")

        # USI PrivaSafe Higher Limits with MEDEFENSE™ Plus Combined without PCI

        # Limits
        # $2,000,000 Privasafe/$1,000,000 Medefense
        self.option_884_limit_2419 = self.driver.find_element(By.ID, "option-884-limit-2419")

        # $3,000,000 Privasafe/$1,000,000 Medefense
        self.option_884_limit_3240 = self.driver.find_element(By.ID, "option-884-limit-3240")

        # Deductibles
        # $2,500
        self.option_884_deductible_926 = self.driver.find_element(By.ID, "option-884-deductible-926")

        # $5,000
        self.option_884_deductible_928 = self.driver.find_element(By.ID, "option-884-deductible-928")

        return self

    def select_USI_PrivaSafe_Medefense_Plus_Only_1MM_1MM_limit_2pt5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_538_limit_2384.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_538_deductible_919.click()

    def select_USI_PrivaSafe_Only_1MM_1MM_100K_limit_1K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_541_limit_2389.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_541_deductible_925.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_2MM_limit_2pt5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_limit_2410.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_deductible_925.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_2MM_limit_5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_limit_2410.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_deductible_927.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_3MM_limit_2pt5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_limit_3238.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_deductible_925.click()

    def select_USI_PrivaSafe_Higher_Limits_Only_3MM_limit_5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_limit_3238.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_883_deductible_927.click()

    def select_USI_PrivaSafe_with_MEDEFENSE_Plus_Combined_1MM_1MM_limit_2pt5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_542_limit_2390.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_542_deductible_926.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_2MM_1MM_limit_2pt5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_limit_2419.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_deductible_926.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_3MM_1MM_limit_2pt5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_limit_3240.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_deductible_926.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_2MM_1MM_limit_5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_limit_2419.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_deductible_928.click()

    def select_USI_PrivaSafe_Higher_Limits_with_MEDEFENSE_Plus_Combined_3MM_1MM_limit_5K_Deduct(self):
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_limit_3240.click()
        Non_HCF_No_PCI_Coverage_Options.PageElements(self).option_884_deductible_928.click()