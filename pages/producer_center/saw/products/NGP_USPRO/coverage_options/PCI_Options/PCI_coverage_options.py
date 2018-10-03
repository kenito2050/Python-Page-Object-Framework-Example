from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # 250K
        self.option_978_limit_3740 = self.driver.find_element(By.ID, "option-978-limit-3740")

        # 500K
        self.option_978_limit_3741 = self.driver.find_element(By.ID, "option-978-limit-3741")

        # 1MM
        self.option_978_limit_3742 = self.driver.find_element(By.ID, "option-978-limit-3742")

        # 2MM
        self.option_978_limit_3743 = self.driver.find_element(By.ID, "option-978-limit-3743")

        # # 3MM
        # self.option_978_limit_3744 = self.driver.find_element(By.ID, "option-978-limit-3744")

        # Deductibles
        # $500
        self.option_978_deductible_1465 = self.driver.find_element(By.ID, "option-978-deductible-1465")

        # $1,000
        self.option_978_deductible_1460 = self.driver.find_element(By.ID, "option-978-deductible-1460")

        # $2,500
        self.option_978_deductible_1461 = self.driver.find_element(By.ID, "option-978-deductible-1461")

        # $5,000
        self.option_978_deductible_1462 = self.driver.find_element(By.ID, "option-978-deductible-1462")

        # $10,000
        self.option_978_deductible_1463 = self.driver.find_element(By.ID, "option-978-deductible-1463")

        # $25,000
        self.option_978_deductible_1464 = self.driver.find_element(By.ID, "option-978-deductible-1464")

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit Per Identity

        # Limits

        # 250K
        self.option_1017_limit_3843 = self.driver.find_element(By.ID, "option-1017-limit-3843")

        # 500K
        self.option_1017_limit_3844 = self.driver.find_element(By.ID, "option-1017-limit-3844")

        # 1MM
        self.option_1017_limit_3844 = self.driver.find_element(By.ID, "option-1017-limit-3845")

        # 2MM
        self.option_1017_limit_3846 = self.driver.find_element(By.ID, "option-1017-limit-3846")

        # # 3MM
        # self.option_1017_limit_3847 = self.driver.find_element(By.ID, "option-1017-limit-3847")

        # Deductibles
        # $500
        self.option_1017_deductible_1523 = self.driver.find_element(By.ID, "option-1017-deductible-1523")

        # $1,000
        self.option_1017_deductible_1518 = self.driver.find_element(By.ID, "option-1017-deductible-1518")

        # $2,500
        self.option_1017_deductible_1519 = self.driver.find_element(By.ID, "option-1017-deductible-1519")

        # $5,000
        self.option_1017_deductible_1520 = self.driver.find_element(By.ID, "option-1017-deductible-1520")

        # $10,000
        self.option_1017_deductible_1521 = self.driver.find_element(By.ID, "option-1017-deductible-1521")

        # $25,000
        self.option_1017_deductible_1522 = self.driver.find_element(By.ID, "option-1017-deductible-1522")

        return self

    def select_NetGuard_Plus_with_BrandGuard_PCI_Assessment_1MM_limit_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_978_limit_3742.click()
        PCI_Coverage_Options.PageElements(self).option_978_deductible_1461.click()