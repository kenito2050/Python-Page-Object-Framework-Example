from selenium.webdriver.common.by import By

class HCF_No_PCI_Coverage_Options_10MM_to_25MM():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_799_limit_160 = self.driver.find_element(By.ID, "option-799-limit-160")

        # Deductibles
        # $2,500
        self.option_799_deductible_145 = self.driver.find_element(By.ID, "option-799-deductible-145")

        # $5,000
        self.option_799_deductible_146 = self.driver.find_element(By.ID, "option-799-deductible-146")

        # $10,000
        self.option_799_deductible_147 = self.driver.find_element(By.ID, "option-799-deductible-147")

        # e-MD™ Only With Cyber Crime and Without PCI

        # Limits
        # 1MM/1MM/100K Cyber Crime/NIL PCI
        self.option_801_limit_3107 = self.driver.find_element(By.ID, "option-801-limit-3107")

        # Deductibles
        # $2,500
        self.option_801_deductible_1254 = self.driver.find_element(By.ID, "option-801-deductible-1254")

        # $5,000
        self.option_801_deductible_1255 = self.driver.find_element(By.ID, "option-801-deductible-1255")

        # $10,000
        self.option_801_deductible_1256 = self.driver.find_element(By.ID, "option-801-deductible-1256")

        # e-MD™ Higher Limits Only With Cyber Crime and Without PCI

        # Limits
        # 2MM/2MM/100K Cyber Crime/NIL PCI
        self.option_804_limit_3110 = self.driver.find_element(By.ID, "option-804-limit-3110")

        # 3MM/3MM/100K Cyber Crime/NIL PCI
        self.option_804_limit_3111 = self.driver.find_element(By.ID, "option-804-limit-3111")

        # Deductibles
        # $2,500
        self.option_804_deductible_1254 = self.driver.find_element(By.ID, "option-804-deductible-1254")

        # $5,000
        self.option_804_deductible_1255 = self.driver.find_element(By.ID, "option-804-deductible-1255")

        # $10,000
        self.option_804_deductible_1256 = self.driver.find_element(By.ID, "option-804-deductible-1256")

        # Medefense™ Plus and e-MD™ With Cyber Crime and Without PCI Combined

        # Limits
        # 1MM/1MM/100K Cyber Crime/NIL PCI
        self.option_807_limit_3117 = self.driver.find_element(By.ID, "option-807-limit-3117")

        # Deductibles
        # $2,500
        self.option_807_deductible_1264 = self.driver.find_element(By.ID, "option-807-deductible-1264")

        # $5,000
        self.option_807_deductible_1265 = self.driver.find_element(By.ID, "option-807-deductible-1265")

        # $10,000
        self.option_807_deductible_1263 = self.driver.find_element(By.ID, "option-807-deductible-1263")

        # Medefense™ Plus and e-MD™ Higher Limits With Cyber Crime and Without PCI Combined

        # Limits
        # 2MM/2MM/100k Cyber Crime/NIL PCI
        self.option_810_limit_3124 = self.driver.find_element(By.ID, "option-810-limit-3124")

        # 3MM/3MM/100k Cyber Crime/NIL PCI
        self.option_810_limit_3125 = self.driver.find_element(By.ID, "option-810-limit-3125")

        # Deductibles
        # $2,500
        self.option_810_deductible_1264 = self.driver.find_element(By.ID, "option-810-deductible-1264")

        # $5,000
        self.option_810_deductible_1265 = self.driver.find_element(By.ID, "option-810-deductible-1265")

        # $10,000
        self.option_810_deductible_1263 = self.driver.find_element(By.ID, "option-810-deductible-1263")

        return self

    ### Revenue Between 10MM and 25MM

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_799_limit_160.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_799_deductible_145.click()

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_799_limit_160.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_799_deductible_146.click()

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_799_limit_160.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_799_deductible_147.click()

    def select_eMD_Only_Without_PCI_and_Cyber_Crime_1MM_1MM_100K_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_801_limit_3107.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_801_deductible_1254.click()

    def select_eMD_Only_Without_PCI_and_Cyber_Crime_1MM_1MM_100K_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_801_limit_3107.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_801_deductible_1255.click()

    def select_eMD_Only_Without_PCI_and_Cyber_Crime_1MM_1MM_100K_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_801_limit_3107.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_801_deductible_1256.click()

    def select_eMD_Higher_Limits_Only_Without_PCI_and_Cyber_Crime_2MM_2MM_100K_250K_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_limit_3110.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_deductible_1254.click()

    def select_eMD_Higher_Limits_Only_Without_PCI_and_Cyber_Crime_2MM_2MM_100K_250K_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_limit_3110.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_deductible_1255.click()

    def select_eMD_Higher_Limits_Only_Without_PCI_and_Cyber_Crime_2MM_2MM_100K_250K_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_limit_3110.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_deductible_1256.click()

    def select_eMD_Higher_Limits_Only_Without_PCI_and_Cyber_Crime_3MM_3MM_100K_250K_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_limit_3111.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_deductible_1254.click()

    def select_eMD_Higher_Limits_Only_Without_PCI_and_Cyber_Crime_3MM_3MM_100K_250K_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_limit_3111.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_deductible_1255.click()

    def select_eMD_Higher_Limits_Only_Without_PCI_and_Cyber_Crime_3MM_3MM_100K_250K_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_limit_3111.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_804_deductible_1256.click()

    def select_MEDEFENSE_Plus_and_eMD_Without_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_807_limit_3117.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_807_deductible_1264.click()

    def select_MEDEFENSE_Plus_and_eMD_Without_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_807_limit_3117.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_807_deductible_1265.click()

    def select_MEDEFENSE_Plus_and_eMD_Without_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_807_limit_3117.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_807_deductible_1263.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_limit_3124.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_deductible_1264.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_limit_3124.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_deductible_1265.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_limit_3124.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_deductible_1263.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_2pt5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_limit_3125.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_deductible_1264.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_5K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_limit_3125.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_deductible_1265.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_10K_Deduct(self):
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_limit_3125.click()
        HCF_No_PCI_Coverage_Options_10MM_to_25MM.PageElements(self).option_810_deductible_1263.click()