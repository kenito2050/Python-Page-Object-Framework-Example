from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # CyberRisk™ with Cyber Crime Only

        # Limits
        # 1MM/1MM
        self.option_435_limit_1920 = self.driver.find_element(By.ID, "option-435-limit-1920")

        # Deductibles
        # $50,000
        self.option_435_deductible_772 = self.driver.find_element(By.ID, "option-435-deductible-772")

        # CyberRisk™ Only with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_436_limit_1942 = self.driver.find_element(By.ID, "option-436-limit-1942")

        # Deductibles
        # $25,000
        self.option_436_deductible_772 = self.driver.find_element(By.ID, "option-436-deductible-772")

        # Medefense™ Plus Only

        # Limits
        # 1MM/2MM
        self.option_660_limit_2754 = self.driver.find_element(By.ID, "option-660-limit-2754")

        # Deductibles
        # $25,000
        self.option_660_deductible_1187 = self.driver.find_element(By.ID, "option-660-deductible-1187")

        # Medefense™ Plus with Peer Review Proceeding Sublimit

        # Limits
        # 1MM/5MM
        self.option_310_limit_1528 = self.driver.find_element(By.ID, "option-310-limit-1528")

        # Deductibles
        # $25,000
        self.option_310_deductible_195 = self.driver.find_element(By.ID, "option-310-deductible-195")

        # Medefense™ Plus and CyberRisk™ with Cyber Crime Combined Shared Limits

        # Limits
        # 1MM/1MM
        self.option_431_limit_1923 = self.driver.find_element(By.ID, "option-431-limit-1923")

        # Deductibles
        # $25K/$50K
        self.option_431_deductible_773 = self.driver.find_element(By.ID, "option-431-deductible-773")

        # Medefense™ Plus and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_437_limit_1945 = self.driver.find_element(By.ID, "option-437-limit-1945")

        # Deductibles
        # $25K/$50K
        self.option_437_deductible_773 = self.driver.find_element(By.ID, "option-437-deductible-773")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_432_limit_1929 = self.driver.find_element(By.ID, "option-432-limit-1929")

        # Deductibles
        # $25K/$50K
        self.option_432_deductible_773 = self.driver.find_element(By.ID, "option-432-deductible-773")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_438_limit_1952 = self.driver.find_element(By.ID, "option-438-limit-1952")

        # Deductibles
        # $25K/$50K
        self.option_438_deductible_773 = self.driver.find_element(By.ID, "option-438-deductible-773")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_433_limit_1932 = self.driver.find_element(By.ID, "option-433-limit-1932")

        # Deductibles
        # $25K/$50K
        self.option_433_deductible_759 = self.driver.find_element(By.ID, "option-433-deductible-759")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_439_limit_1955 = self.driver.find_element(By.ID, "option-439-limit-1955")

        # Deductibles
        # $25K/$50K
        self.option_439_deductible_759 = self.driver.find_element(By.ID, "option-439-deductible-759")

        #

        # Limits
        # 1MM/1MM
        self.option_433_limit_1932 = self.driver.find_element(By.ID, "option-433-limit-1932")

        # Deductibles
        # $25K/$50K
        self.option_433_deductible_759 = self.driver.find_element(By.ID, "option-433-deductible-759")

        #

        # Limits
        # 1MM/1MM
        self.option_433_limit_1932 = self.driver.find_element(By.ID, "option-433-limit-1932")

        # Deductibles
        # $25K/$50K
        self.option_433_deductible_759 = self.driver.find_element(By.ID, "option-433-deductible-759")


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