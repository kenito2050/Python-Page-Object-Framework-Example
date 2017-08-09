from selenium.webdriver.common.by import By

class HCF_PCI_Coverage_Options_25MM_or_Greater():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_799_limit_160 = self.driver.find_element(By.ID, "option-799-limit-160")

        # Deductibles
        # $2,500
        # self.option_799_deductible_145 = self.driver.find_element(By.ID, "option-799-deductible-145")

        # $5,000
        self.option_799_deductible_146 = self.driver.find_element(By.ID, "option-799-deductible-146")

        # $10,000
        self.option_799_deductible_147 = self.driver.find_element(By.ID, "option-799-deductible-147")

        # e-MD™ Only With PCI and Cyber Crime

        # Limits
        # 1MM/1MM/100k Cyber Crime/250k PCI
        self.option_800_limit_3106 = self.driver.find_element(By.ID, "option-800-limit-3106")

        # Deductibles
        # $2,500
        # self.option_800_deductible_1250 = self.driver.find_element(By.ID, "option-800-deductible-1250")

        # $5,000
        self.option_800_deductible_1251 = self.driver.find_element(By.ID, "option-800-deductible-1251")

        # $10,000
        self.option_800_deductible_1252 = self.driver.find_element(By.ID, "option-800-deductible-1252")

        # e-MD™ Higher Limits Only With PCI and Cyber Crime

        # Limits
        # 2MM/2MM/100k Cyber Crime/250k PCI
        self.option_803_limit_3108 = self.driver.find_element(By.ID, "option-803-limit-3108")

        # 3MM/3MM/100k Cyber Crime/250k PCI
        self.option_803_limit_3109 = self.driver.find_element(By.ID, "option-803-limit-3109")

        # Deductibles
        # $2,500
        # self.option_803_deductible_1250 = self.driver.find_element(By.ID, "option-803-deductible-1250")

        # $5,000
        self.option_803_deductible_1251 = self.driver.find_element(By.ID, "option-803-deductible-1251")

        # $10,000
        self.option_803_deductible_1252 = self.driver.find_element(By.ID, "option-803-deductible-1252")

        # Medefense™ Plus and e-MD™ With PCI and Cyber Crime Combined

        # Limits
        # 1MM/1MM/100k Cyber Crime/250k PCI
        self.option_806_limit_3112 = self.driver.find_element(By.ID, "option-806-limit-3112")

        # Deductibles
        # $2,500
        # self.option_806_deductible_1260 = self.driver.find_element(By.ID, "option-806-deductible-1260")

        # $5,000
        self.option_806_deductible_1261 = self.driver.find_element(By.ID, "option-806-deductible-1261")

        # $10,000
        self.option_806_deductible_1259 = self.driver.find_element(By.ID, "option-806-deductible-1259")


        # Medefense™ Plus and e-MD™ Higher Limits With PCI and Cyber Crime Combined

        # Limits
        # 2MM/2MM/100k Cyber Crime/250k PCI
        self.option_809_limit_3122 = self.driver.find_element(By.ID, "option-809-limit-3122")

        # 3MM/3MM/100k Cyber Crime/250k PCI
        self.option_809_limit_3123 = self.driver.find_element(By.ID, "option-809-limit-3123")

        # Deductibles
        # $2,500
        # self.option_809_deductible_1260 = self.driver.find_element(By.ID, "option-809-deductible-1260")

        # $5,000
        self.option_809_deductible_1261 = self.driver.find_element(By.ID, "option-809-deductible-1261")

        # $10,000
        self.option_809_deductible_1259 = self.driver.find_element(By.ID, "option-809-deductible-1259")

        return self

        ### Revenue Between 10MM and 25MM

    # def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_2pt5K_Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_799_limit_160.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_799_deductible_145.click()

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_799_limit_160.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_799_deductible_146.click()

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_799_limit_160.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_799_deductible_147.click()

    # def select_eMD_Only_With_PCI_and_Cyber_Crime_1MM_1MM_100K_limit_2pt5K_Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_800_limit_3106.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_800_deductible_1250.click()

    def select_eMD_Only_With_PCI_and_Cyber_Crime_1MM_1MM_100K_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_800_limit_3106.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_800_deductible_1251.click()

    def select_eMD_Only_With_PCI_and_Cyber_Crime_1MM_1MM_100K_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_800_limit_3106.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_800_deductible_1252.click()

    # def select_eMD_Higher_Limits_Only_With_PCI_and_Cyber_Crime_2MM_2MM_100K_250K_limit_2pt5K_Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_803_limit_3108.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_803_deductible_1250.click()

    def select_eMD_Higher_Limits_Only_With_PCI_and_Cyber_Crime_2MM_2MM_100K_250K_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_limit_3108.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_deductible_1251.click()

    def select_eMD_Higher_Limits_Only_With_PCI_and_Cyber_Crime_2MM_2MM_100K_250K_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_limit_3108.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_deductible_1252.click()

    # def select_eMD_Higher_Limits_Only_With_PCI_and_Cyber_Crime_3MM_3MM_100K_250K_limit_2pt5K_Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_803_limit_3109.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_803_deductible_1250.click()

    def select_eMD_Higher_Limits_Only_With_PCI_and_Cyber_Crime_3MM_3MM_100K_250K_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_limit_3109.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_deductible_1251.click()

    def select_eMD_Higher_Limits_Only_With_PCI_and_Cyber_Crime_3MM_3MM_100K_250K_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_limit_3109.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_803_deductible_1252.click()

    # def select_MEDEFENSE_Plus_and_eMD_With_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_2pt5K_Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_806_limit_3112.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_806_deductible_1260.click()

    def select_MEDEFENSE_Plus_and_eMD_With_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_806_limit_3112.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_806_deductible_1261.click()

    def select_MEDEFENSE_Plus_and_eMD_With_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_806_limit_3112.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_806_deductible_1259.click()

    # def select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_2pt5K_Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_809_limit_3123.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_809_deductible_1260.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_limit_3123.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_deductible_1261.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_limit_3123.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_deductible_1259.click()

    # def select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_2pt5K__Deduct(self):
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_809_limit_3123.click()
    #     Coverage_Options_25MM_or_Greater.PageElements(self).option_809_deductible_1260.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_5K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_limit_3123.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_deductible_1261.click()

    def select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_10K_Deduct(self):
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_limit_3123.click()
        HCF_PCI_Coverage_Options_25MM_or_Greater.PageElements(self).option_809_deductible_1259.click()