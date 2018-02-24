from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit
        #
        # # Limits
        #
        # # 250K
        # self.option_898_limit_3413 = self.driver.find_element(By.ID, "option-898-limit-3413")
        #
        # # 500K
        # self.option_898_limit_3414 = self.driver.find_element(By.ID, "option-898-limit-3414")
        #
        # # 1MM
        # self.option_898_limit_3415 = self.driver.find_element(By.ID, "option-898-limit-3415")
        #
        # # 2MM
        # self.option_898_limit_3416 = self.driver.find_element(By.ID, "option-898-limit-3416")
        #
        # # 3MM
        # self.option_898_limit_3417 = self.driver.find_element(By.ID, "option-898-limit-3417")
        #
        # # Deductibles
        # # $500
        # self.option_898_deductible_1391 = self.driver.find_element(By.ID, "option-898-deductible-1391")
        #
        # # $1,000
        # self.option_898_deductible_1386 = self.driver.find_element(By.ID, "option-898-deductible-1386")
        #
        # # $2,500
        # self.option_898_deductible_1387 = self.driver.find_element(By.ID, "option-898-deductible-1387")
        #
        # # $5,000
        # self.option_898_deductible_1388 = self.driver.find_element(By.ID, "option-898-deductible-1388")
        #
        # # $10,000
        # self.option_898_deductible_1389 = self.driver.find_element(By.ID, "option-898-deductible-1389")
        #
        # # $25,000
        # self.option_898_deductible_1390 = self.driver.find_element(By.ID, "option-898-deductible-1390")

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # 1MM
        self.option_981_limit_3752 = self.driver.find_element(By.ID, "option-981-limit-3752")

        # Deductibles

        # $2,500
        self.option_981_deductible_1475 = self.driver.find_element(By.ID, "option-981-deductible-1475")

        return self

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_981_limit_3752.click()
        PCI_Coverage_Options.PageElements(self).option_981_deductible_1475.click()