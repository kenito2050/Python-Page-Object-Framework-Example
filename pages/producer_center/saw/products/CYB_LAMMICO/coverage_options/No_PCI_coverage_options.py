from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™

        # Limits
        # 100K/100K
        self.option_768_limit_3024 = self.driver.find_element(By.ID, "option-658-limit-2753")

        # Deductibles
        # $1,500
        self.option_658_deductible_1186 = self.driver.find_element(By.ID, "option-658-deductible-1186")

        # Cyber Liability Only - No PCI

        # Limits
        # 1MM/1MM
        self.option_667_limit_2760 = self.driver.find_element(By.ID, "option-667-limit-2760")

        # Deductibles
        # $0
        self.option_667_deductible_1189 = self.driver.find_element(By.ID, "option-667-deductible-1189")

        # Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_668_limit_2760 = self.driver.find_element(By.ID, "option-668-limit-2760")

        # Deductibles
        # $0
        self.option_668_deductible_1189 = self.driver.find_element(By.ID, "option-668-deductible-1189")

        # Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_669_limit_2761 = self.driver.find_element(By.ID, "option-669-limit-2761")

        # Deductibles
        # $0
        self.option_669_deductible_1189 = self.driver.find_element(By.ID, "option-669-deductible-1189")

        # Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_670_limit_2761 = self.driver.find_element(By.ID, "option-670-limit-2761")

        # Deductibles
        # $0
        self.option_670_deductible_1189 = self.driver.find_element(By.ID, "option-670-deductible-1189")

        # MEDEFENSE™ Plus and Cyber Liability Combined - No PCI

        # Limits
        # 1MM/1MM
        self.option_671_limit_2762 = self.driver.find_element(By.ID, "option-671-limit-2762")

        # Deductibles
        # $1,500 / $0
        self.option_671_deductible_1190 = self.driver.find_element(By.ID, "option-671-deductible-1190")

        # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_672_limit_2762 = self.driver.find_element(By.ID, "option-672-limit-2762")

        # Deductibles
        # $1,500 / $0
        self.option_672_deductible_1190 = self.driver.find_element(By.ID, "option-672-deductible-1190")

        # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_673_limit_2763 = self.driver.find_element(By.ID, "option-673-limit-2763")

        # Deductibles
        # $1,500 / $0
        self.option_673_deductible_1190 = self.driver.find_element(By.ID, "option-673-deductible-1190")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_674_limit_2763 = self.driver.find_element(By.ID, "option-674-limit-2763")

        # Deductibles
        # $1,500 / $0
        self.option_674_deductible_1190 = self.driver.find_element(By.ID, "option-674-deductible-1190")

        return self

    def select_Cyber_Liability_Only_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_667_limit_2760.click()
        No_PCI_Coverage_Options.PageElements(self).option_667_deductible_1189.click()

    def select_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_668_limit_2760.click()
        No_PCI_Coverage_Options.PageElements(self).option_668_deductible_1189.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_669_limit_2761.click()
        No_PCI_Coverage_Options.PageElements(self).option_669_deductible_1189.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_670_limit_2761.click()
        No_PCI_Coverage_Options.PageElements(self).option_670_deductible_1189.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_Combined_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_671_limit_2762.click()
        No_PCI_Coverage_Options.PageElements(self).option_671_deductible_1190.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_672_limit_2762.click()
        No_PCI_Coverage_Options.PageElements(self).option_672_deductible_1190.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_673_limit_2763.click()
        No_PCI_Coverage_Options.PageElements(self).option_673_deductible_1190.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_674_limit_2763.click()
        No_PCI_Coverage_Options.PageElements(self).option_674_deductible_1190.click()