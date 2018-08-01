from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # NetGuard™ Plus with BrandGuard™ Without PCI

        # Limits

        # 250K
        self.option_972_limit_3716 = self.driver.find_element(By.ID, "option-972-limit-3716")

        # 500K
        self.option_972_limit_3713 = self.driver.find_element(By.ID, "option-972-limit-3713")

        # 1MM
        self.option_972_limit_3714 = self.driver.find_element(By.ID, "option-972-limit-3714")

        # 2MM
        self.option_972_limit_3715 = self.driver.find_element(By.ID, "option-972-limit-3715")

        # Deductibles
        # $500
        self.option_972_deductible_1439 = self.driver.find_element(By.ID, "option-972-deductible-1439")

        # $1K
        self.option_972_deductible_1434 = self.driver.find_element(By.ID, "option-972-deductible-1434")

        # $2pt5K
        self.option_972_deductible_1435 = self.driver.find_element(By.ID, "option-972-deductible-1435")

        # $5K
        self.option_972_deductible_1436 = self.driver.find_element(By.ID, "option-972-deductible-1436")

        # $10K
        self.option_972_deductible_1437 = self.driver.find_element(By.ID, "option-972-deductible-1437")

        # $25K
        self.option_972_deductible_1438 = self.driver.find_element(By.ID, "option-972-deductible-1438")

        return self

    def select_NGP_with_BrandGuard_No_PCI_1MM_limit_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_972_limit_3714.click()
        No_PCI_Coverage_Options.PageElements(self).option_972_deductible_1435.click()