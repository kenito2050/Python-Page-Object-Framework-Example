from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_658_limit_2753 = self.driver.find_element(By.ID, "option-658-limit-2753")

        # Deductibles
        # $1,500
        self.option_658_deductible_1186 = self.driver.find_element(By.ID, "option-658-deductible-1186")

        # Cyber Liability Only

        # Limits
        # 1MM/1MM
        self.option_659_limit_2754 = self.driver.find_element(By.ID, "option-659-limit-2754")

        # Deductibles
        # $0
        self.option_659_deductible_1187 = self.driver.find_element(By.ID, "option-659-deductible-1187")

        # Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_660_limit_2754 = self.driver.find_element(By.ID, "option-660-limit-2754")

        # Deductibles
        # $0
        self.option_660_deductible_1187 = self.driver.find_element(By.ID, "option-660-deductible-1187")

        # Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_661_limit_2757 = self.driver.find_element(By.ID, "option-661-limit-2757")

        # Deductibles
        # $0
        self.option_661_deductible_1187 = self.driver.find_element(By.ID, "option-661-deductible-1187")

        # Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_662_limit_2757 = self.driver.find_element(By.ID, "option-662-limit-2757")

        # Deductibles
        # $0
        self.option_662_deductible_1187 = self.driver.find_element(By.ID, "option-662-deductible-1187")

        # MEDEFENSE™ Plus and Cyber Liability Combined

        # Limits
        # 1MM/1MM
        self.option_663_limit_2758 = self.driver.find_element(By.ID, "option-663-limit-2758")

        # Deductibles
        # $1,500 / $0
        self.option_663_deductible_1188 = self.driver.find_element(By.ID, "option-663-deductible-1188")

        # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_664_limit_2758 = self.driver.find_element(By.ID, "option-664-limit-2758")

        # Deductibles
        # $1,500 / $0
        self.option_664_deductible_1188 = self.driver.find_element(By.ID, "option-664-deductible-1188")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_665_limit_2759 = self.driver.find_element(By.ID, "option-665-limit-2759")

        # Deductibles
        # $1,500 / $0
        self.option_665_deductible_1188 = self.driver.find_element(By.ID, "option-665-deductible-1188")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_666_limit_2759 = self.driver.find_element(By.ID, "option-666-limit-2759")

        # Deductibles
        # $1,500 / $0
        self.option_666_deductible_1188 = self.driver.find_element(By.ID, "option-666-deductible-1188")

        return self

    def select_MEDEFENSE_Plus_Only(self):
        PCI_Coverage_Options.PageElements(self).option_658_limit_2753.click()
        PCI_Coverage_Options.PageElements(self).option_658_deductible_1186.click()

    def select_Cyber_Liability_Only(self):
        PCI_Coverage_Options.PageElements(self).option_659_limit_2754.click()
        PCI_Coverage_Options.PageElements(self).option_659_deductible_1187.click()

    def select_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_660_limit_2754.click()
        PCI_Coverage_Options.PageElements(self).option_660_deductible_1187.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_661_limit_2757.click()
        PCI_Coverage_Options.PageElements(self).option_661_deductible_1187.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_662_limit_2757.click()
        PCI_Coverage_Options.PageElements(self).option_662_deductible_1187.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_Combined(self):
        PCI_Coverage_Options.PageElements(self).option_663_limit_2758.click()
        PCI_Coverage_Options.PageElements(self).option_663_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_664_limit_2758.click()
        PCI_Coverage_Options.PageElements(self).option_664_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_665_limit_2759.click()
        PCI_Coverage_Options.PageElements(self).option_665_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_666_limit_2759.click()
        PCI_Coverage_Options.PageElements(self).option_666_deductible_1188.click()