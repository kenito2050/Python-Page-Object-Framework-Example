from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # 250K
        self.option_898_limit_3413 = self.driver.find_element(By.ID, "option-898-limit-3413")

        # 500K
        self.option_898_limit_3414 = self.driver.find_element(By.ID, "option-898-limit-3414")

        # 1MM
        self.option_898_limit_3415 = self.driver.find_element(By.ID, "option-898-limit-3415")

        # 2MM
        self.option_898_limit_3416 = self.driver.find_element(By.ID, "option-898-limit-3416")

        # 3MM
        self.option_898_limit_3417 = self.driver.find_element(By.ID, "option-898-limit-3417")

        # Deductibles
        # $500
        self.option_898_deductible_1391 = self.driver.find_element(By.ID, "option-898-deductible-1391")

        # $1,000
        self.option_898_deductible_1386 = self.driver.find_element(By.ID, "option-898-deductible-1386")

        # $2,500
        self.option_898_deductible_1387 = self.driver.find_element(By.ID, "option-898-deductible-1387")

        # $5,000
        self.option_898_deductible_1388 = self.driver.find_element(By.ID, "option-898-deductible-1388")

        # $10,000
        self.option_898_deductible_1389 = self.driver.find_element(By.ID, "option-898-deductible-1389")

        # $25,000
        self.option_898_deductible_1390 = self.driver.find_element(By.ID, "option-898-deductible-1390")

        return self

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_250K_limit_500_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3413.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1391.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_250K_limit_1000_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3413.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1386.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_250K_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3413.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1387.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_250K_limit_5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3413.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1388.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_250K_limit_10K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3413.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1389.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_250K_limit_25K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3413.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1390.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_500K_limit_500_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3414.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1391.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_500K_limit_1000_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3414.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1386.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_500K_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3414.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1387.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_500K_limit_5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3414.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1388.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_500K_limit_10K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3414.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1389.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_500K_limit_25K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3414.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1390.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_500_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3415.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1391.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_1000_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3415.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1386.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3415.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1387.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3415.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1388.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_10K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3415.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1389.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_1MM_limit_25K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3415.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1390.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_2MM_limit_500_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3416.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1391.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_2MM_limit_1000_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3416.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1386.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_2MM_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3416.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1387.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_2MM_limit_5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3416.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1388.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_2MM_limit_10K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3416.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1389.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_2MM_limit_25K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3416.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1390.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_3MM_limit_500_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3417.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1391.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_3MM_limit_1000_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3417.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1386.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_3MM_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3417.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1387.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_3MM_limit_5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3417.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1388.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_3MM_limit_10K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3417.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1389.click()

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_Sublimit_3MM_limit_25K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_898_limit_3417.click()
        PCI_Coverage_Options.PageElements(self).option_898_deductible_1390.click()