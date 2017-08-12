from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_789_limit_3095 = self.driver.find_element(By.ID, "option-789-limit-3095")

        # Deductibles
        # $0
        self.option_789_deductible_1242 = self.driver.find_element(By.ID, "option-789-deductible-1242")

        # Cyber Liability Only

        # Limits
        # 1MM/1MM
        self.option_791_limit_3097 = self.driver.find_element(By.ID, "option-791-limit-3097")

        # Deductibles
        # $0 / $2,500
        self.option_791_deductible_1244 = self.driver.find_element(By.ID, "option-791-deductible-1244")

        # MEDEFENSE™ Plus with $100,000 Medical Board Proceedings Sublimit

        # Limits
        # 1MM/100K/1MM
        self.option_790_limit_3096 = self.driver.find_element(By.ID, "option-790-limit-3096")

        # Deductibles
        # $0/$1,000
        self.option_790_deductible_1243 = self.driver.find_element(By.ID, "option-790-deductible-1243")

        # MEDEFENSE™ Plus and Cyber Liability

        # Limits
        # 1MM/1MM
        self.option_792_limit_3098 = self.driver.find_element(By.ID, "option-792-limit-3098")

        # Deductibles
        # $0/$2,500
        self.option_792_deductible_1245 = self.driver.find_element(By.ID, "option-792-deductible-1245")

        # MEDEFENSE™ Plus with $100K Medical Board Proceedings Sublimit and Cyber Liability

        # Limits
        # 1MM/100K/1MM
        self.option_793_limit_3099 = self.driver.find_element(By.ID, "option-793-limit-3099")

        # Deductibles
        # $0/$1,000/$2,500
        self.option_793_deductible_1246 = self.driver.find_element(By.ID, "option-793-deductible-1246")

        return self

    def select_MEDEFENSE_Plus_Only_1MM_1MM_limit_0_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_789_limit_3095.click()
        PCI_Coverage_Options.PageElements(self).option_789_deductible_1242.click()

    def select_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_791_limit_3097.click()
        PCI_Coverage_Options.PageElements(self).option_791_deductible_1244.click()

    def select_MEDEFENSE_Plus_with_100K_Medical_Board_Proceedings_Sublimit_1MM_100K_1M_limit_0_1K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_790_limit_3096.click()
        PCI_Coverage_Options.PageElements(self).option_790_deductible_1243.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_1MM_1M_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_792_limit_3098.click()
        PCI_Coverage_Options.PageElements(self).option_792_deductible_1245.click()

    def select_MEDEFENSE_Plus_with_100K_Medical_Board_Proceedings_Sublimit_and_Cyber_Liability_1MM_1M_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_793_limit_3099.click()
        PCI_Coverage_Options.PageElements(self).option_793_deductible_1246.click()