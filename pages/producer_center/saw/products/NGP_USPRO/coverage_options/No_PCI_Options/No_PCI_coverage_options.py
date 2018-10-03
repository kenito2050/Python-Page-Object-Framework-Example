from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # NetGuard™ Plus with BrandGuard™ Without PCI

        # Limits

        # 250K
        self.option_979_limit_3748 = self.driver.find_element(By.ID, "option-979-limit-3748")

        # 500K
        self.option_979_limit_3745 = self.driver.find_element(By.ID, "option-979-limit-3745")

        # 1MM
        self.option_979_limit_3746 = self.driver.find_element(By.ID, "option-979-limit-3746")

        # 2MM
        self.option_979_limit_3747 = self.driver.find_element(By.ID, "option-979-limit-3747")

        # # 3MM
        # self.option_978_limit_3744 = self.driver.find_element(By.ID, "option-978-limit-3744")

        # Deductibles
        # $500
        self.option_979_deductible_1472 = self.driver.find_element(By.ID, "option-979-deductible-1472")

        # $1,000
        self.option_979_deductible_1467 = self.driver.find_element(By.ID, "option-979-deductible-1467")

        # $2,500
        self.option_979_deductible_1468 = self.driver.find_element(By.ID, "option-979-deductible-1468")

        # $5,000
        self.option_979_deductible_1469 = self.driver.find_element(By.ID, "option-979-deductible-1469")

        # $10,000
        self.option_979_deductible_1470 = self.driver.find_element(By.ID, "option-979-deductible-1470")

        # $25,000
        self.option_979_deductible_1471 = self.driver.find_element(By.ID, "option-979-deductible-1471")

        # NetGuard™ Plus with BrandGuard™ Without PCI Per Identity

        # Limits

        # 250K
        self.option_1018_limit_3851 = self.driver.find_element(By.ID, "option-1018-limit-3851")

        # 500K
        self.option_1018_limit_3848 = self.driver.find_element(By.ID, "option-1018-limit-3848")

        # 1MM
        self.option_1018_limit_3849 = self.driver.find_element(By.ID, "option-1018-limit-3849")

        # 2MM
        self.option_1018_limit_3850 = self.driver.find_element(By.ID, "option-1018-limit-3850")

        # # 3MM
        # self.option_1017_limit_3847 = self.driver.find_element(By.ID, "option-1017-limit-3847")

        # Deductibles
        # $500
        self.option_1018_deductible_1530 = self.driver.find_element(By.ID, "option-1018-deductible-1530")

        # $1,000
        self.option_1018_deductible_1525 = self.driver.find_element(By.ID, "option-1018-deductible-1525")

        # $2,500
        self.option_1018_deductible_1526 = self.driver.find_element(By.ID, "option-1018-deductible-1526")

        # $5,000
        self.option_1018_deductible_1527 = self.driver.find_element(By.ID, "option-1018-deductible-1527")

        # $10,000
        self.option_1018_deductible_1528 = self.driver.find_element(By.ID, "option-1018-deductible-1528")

        # $25,000
        self.option_1018_deductible_1529 = self.driver.find_element(By.ID, "option-1018-deductible-1529")

        return self

    def select_NetGuard_Plus_with_BrandGuard_Without_PCI_1MM_limit_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_979_limit_3746.click()
        No_PCI_Coverage_Options.PageElements(self).option_979_deductible_1468.click()