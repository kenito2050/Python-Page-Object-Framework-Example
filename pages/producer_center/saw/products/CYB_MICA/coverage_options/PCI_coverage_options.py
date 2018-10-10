from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_1180_limit_4524 = self.driver.find_element(By.ID, "option-1180-limit-4524")

        # Deductibles
        # $1,500
        self.option_1180_deductible_1816 = self.driver.find_element(By.ID, "option-1180-deductible-1816")

        # Cyber Liability Only

        # Limits
        # 1MM/1MM
        self.option_1195_limit_4539 = self.driver.find_element(By.ID, "option-1195-limit-4539")

        # Deductibles
        # $0
        self.option_1195_deductible_1817 = self.driver.find_element(By.ID, "option-1195-deductible-1817")

        # Cyber Liability with Breach Event Costs Outside the Limit (Enhancement)
        # Limits
        # 1MM/1MM
        self.option_1196_limit_4539 = self.driver.find_element(By.ID, "option-1196-limit-4539")

        # Deductibles
        # $0
        self.option_1196_deductible_1817 = self.driver.find_element(By.ID, "option-1196-deductible-1817")

        # Cyber Liability with Additional Defense Costs Outside the Limit
        # Limits
        # 1MM/1MM
        self.option_1197_limit_4525 = self.driver.find_element(By.ID, "option-1197-limit-4525")

        # Deductibles
        # $0
        self.option_1197_deductible_1817 = self.driver.find_element(By.ID, "option-1197-deductible-1817")

        # Cyber Liability with Additional Defense Costs Outside the Limit and Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 1MM/1MM
        self.option_1181_limit_4525 = self.driver.find_element(By.ID, "option-1181-limit-4525")

        # Deductibles
        # $0
        self.option_1181_deductible_1817 = self.driver.find_element(By.ID, "option-1181-deductible-1817")

        # MEDEFENSE™ Plus and Cyber Liability Combined

        # Limits
        # 1MM/1MM
        self.option_1198_limit_4542 = self.driver.find_element(By.ID, "option-1198-limit-4542")

        # Deductibles
        # $0
        self.option_1198_deductible_4542 = self.driver.find_element(By.ID, "option-1198-deductible-1818")

        # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 1MM/1MM
        self.option_1199_limit_4542 = self.driver.find_element(By.ID, "option-1199-limit-4542")

        # Deductibles
        # $0
        self.option_1199_deductible_1818 = self.driver.find_element(By.ID, "option-1199-deductible-1818")

        # MEDEFENSE™ Plus and Cyber Liability with Additional Defense Costs Outside the Limit

        # Limits
        # 1MM/1MM
        self.option_1200_limit_4526 = self.driver.find_element(By.ID, "option-1200-limit-4526")

        # Deductibles
        # $0
        self.option_1200_deductible_1818 = self.driver.find_element(By.ID, "option-1200-deductible-1818")

        # MEDEFENSE™ Plus and Cyber Liability with Additional Defense Costs Outside the Limit and Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 1MM/1MM
        self.option_1182_limit_4526 = self.driver.find_element(By.ID, "option-1182-limit-4526")

        # Deductibles
        # $0
        self.option_1182_deductible_1818 = self.driver.find_element(By.ID, "option-1182-deductible-1818")

        # $2M Cyber Liability Only

        # Limits
        # 2MM/2MM
        self.option_1210_limit_4543 = self.driver.find_element(By.ID, "option-1210-limit-4543")

        # Deductibles
        # $0
        self.option_1210_deductible_1817 = self.driver.find_element(By.ID, "option-1210-deductible-1817")

        # $3M Cyber Liability Only

        # Limits
        # 3MM/3MM
        self.option_1211_limit_4544 = self.driver.find_element(By.ID, "option-1211-limit-4544")

        # Deductibles
        # $0
        self.option_1211_deductible_1877 = self.driver.find_element(By.ID, "option-1211-deductible-1817")

        # $2M Cyber Liability with Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 2MM/2MM
        self.option_1212_limit_4543 = self.driver.find_element(By.ID, "option-1212-limit-4543")

        # Deductibles
        # $0
        self.option_1212_deductible_1817 = self.driver.find_element(By.ID, "option-1212-deductible-1817")

        # $2M Cyber Liability with Additional Defense Costs Outside the Limit

        # Limits
        # 2MM/2MM
        self.option_1214_limit_4529 = self.driver.find_element(By.ID, "option-1214-limit-4529")

        # Deductibles
        # $0
        self.option_1214_deductible_1817 = self.driver.find_element(By.ID, "option-1214-deductible-1817")

        # $3M Cyber Liability with Additional Defense Costs Outside the Limit

        # Limits
        # 3MM/3MM
        self.option_1215_limit_4530 = self.driver.find_element(By.ID, "option-1215-limit-4530")

        # Deductibles
        # $0
        self.option_1215_deductible_1817 = self.driver.find_element(By.ID, "option-1215-deductible-1817")

        # $2M Cyber Liability with Additional Defense Costs Outside the Limit and Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 2MM/2MM
        self.option_1185_limit_4529 = self.driver.find_element(By.ID, "option-1185-limit-4529")

        # Deductibles
        # $1,500 / $0
        self.option_1185_deductible_1817 = self.driver.find_element(By.ID, "option-1185-deductible-1817")

        # $3M Cyber Liability with Additional Defense Costs Outside the Limit and Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 3MM/3MM
        self.option_1186_limit_4530 = self.driver.find_element(By.ID, "option-1186-limit-4530")

        # Deductibles
        # $0
        self.option_1186_deductible_1817 = self.driver.find_element(By.ID, "option-1186-deductible-1817")

        # $2M Cyber Liability and MEDEFENSE™ Plus Combined

        # Limits
        # 2MM/2MM
        self.option_1222_limit_4547 = self.driver.find_element(By.ID, "option-1222-limit-4547")

        # Deductibles
        # $1,500 / $0
        self.option_1222_deductible_1818 = self.driver.find_element(By.ID, "option-1222-deductible-1818")

        # $3M Cyber Liability and MEDEFENSE™ Plus Combined

        # Limits
        # 3MM/3MM
        self.option_1223_limit_4548 = self.driver.find_element(By.ID, "option-1223-limit-4548")

        # Deductibles
        # $1,500 / $0
        self.option_1223_deductible_1818 = self.driver.find_element(By.ID, "option-1223-deductible-1818")

        # $2M Cyber Liability and MEDEFENSE™ Plus with Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 2MM/2MM
        self.option_1224_limit_4547 = self.driver.find_element(By.ID, "option-1224-limit-4547")

        # Deductibles
        # $1,500 / $0
        self.option_1224_deductible_1818 = self.driver.find_element(By.ID, "option-1224-deductible-1818")

        # $3M Cyber Liability and MEDEFENSE™ Plus with Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 3MM/3MM
        self.option_1225_limit_4548 = self.driver.find_element(By.ID, "option-1225-limit-4548")

        # Deductibles
        # $1,500 / $0
        self.option_1225_deductible_18818 = self.driver.find_element(By.ID, "option-1225-deductible-1818")

        # $2M Cyber Liability and MEDEFENSE™ Plus with Additional Defense Costs Outside the Limit

        # Limits
        # 2MM/2MM
        self.option_1226_limit_4531 = self.driver.find_element(By.ID, "option-1226-limit-4531")

        # Deductibles
        # $1,500 / $0
        self.option_1226_deductible_1818 = self.driver.find_element(By.ID, "option-1226-deductible-1818")

        # $3M Cyber Liability and MEDEFENSE™ Plus with Additional Defense Costs Outside the Limit

        # Limits
        # 3MM/3MM
        self.option_1227_limit_4532 = self.driver.find_element(By.ID, "option-1227-limit-4532")

        # Deductibles
        # $1,500 / $0
        self.option_1227_deductible_1818 = self.driver.find_element(By.ID, "option-1227-deductible-1818")

        # $2M Cyber Liability and MEDEFENSE™ Plus with Additional Defense Costs Outside the Limit and Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 2MM/2MM
        self.option_1190_limit_4531 = self.driver.find_element(By.ID, "option-1190-limit-4531")

        # Deductibles
        # $1,500 / $0
        self.option_1190_deductible_1818 = self.driver.find_element(By.ID, "option-1190-deductible-1818")

        # $3M Cyber Liability and MEDEFENSE™ Plus with Additional Defense Costs Outside the Limit and Breach Event Costs Outside the Limit (Enhancement)

        # Limits
        # 3MM/3MM
        self.option_1189_limit_4532 = self.driver.find_element(By.ID, "option-1189-limit-4532")

        # Deductibles
        # $1,500 / $0
        self.option_1189_deductible_1818 = self.driver.find_element(By.ID, "option-1189-deductible-1818")

        return self

    def select_MEDEFENSE_Plus_Only(self):
        PCI_Coverage_Options.PageElements(self).option_1180_limit_4524.click()
        PCI_Coverage_Options.PageElements(self).option_1180_deductible_1816.click()