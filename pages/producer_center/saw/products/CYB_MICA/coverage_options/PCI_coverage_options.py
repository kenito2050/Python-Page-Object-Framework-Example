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

        # $2M Cyber Liability Only
        # Limits
        # 2MM/2MM
        self.option_934_limit_3668 = self.driver.find_element(By.ID, "option-934-limit-3668")

        # Deductibles
        # $0
        self.option_934_deductible_1187 = self.driver.find_element(By.ID, "option-934-deductible-1187")

        # $3M Cyber Liability Only
        # Limits
        # 3MM/3MM
        self.option_935_limit_3669 = self.driver.find_element(By.ID, "option-935-limit-3669")

        # Deductibles
        # $0
        self.option_935_deductible_1187 = self.driver.find_element(By.ID, "option-935-deductible-1187")

        # Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_661_limit_2757 = self.driver.find_element(By.ID, "option-661-limit-2757")

        # Deductibles
        # $0
        self.option_661_deductible_1187 = self.driver.find_element(By.ID, "option-661-deductible-1187")

        # 2MM Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 2MM/2MM
        self.option_938_limit_3670 = self.driver.find_element(By.ID, "option-938-limit-3670")

        # Deductibles
        # $0
        self.option_938_deductible_1187 = self.driver.find_element(By.ID, "option-938-deductible-1187")

        # 3MM Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 3MM/3MM
        self.option_939_limit_3671 = self.driver.find_element(By.ID, "option-939-limit-3671")

        # Deductibles
        # $0
        self.option_939_deductible_1187 = self.driver.find_element(By.ID, "option-939-deductible-1187")

        # Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_660_limit_2754 = self.driver.find_element(By.ID, "option-660-limit-2754")

        # Deductibles
        # $0
        self.option_660_deductible_1187 = self.driver.find_element(By.ID, "option-660-deductible-1187")

        # 2MM Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 2MM/2MM
        self.option_936_limit_3668 = self.driver.find_element(By.ID, "option-936-limit-3668")

        # Deductibles
        # $0
        self.option_936_deductible_1187 = self.driver.find_element(By.ID, "option-936-deductible-1187")

        # 3MM Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 3MM/3MM
        self.option_937_limit_3669 = self.driver.find_element(By.ID, "option-937-limit-3669")

        # Deductibles
        # $0
        self.option_937_deductible_1187 = self.driver.find_element(By.ID, "option-937-deductible-1187")

        # Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_662_limit_2757 = self.driver.find_element(By.ID, "option-662-limit-2757")

        # Deductibles
        # $0
        self.option_662_deductible_1187 = self.driver.find_element(By.ID, "option-662-deductible-1187")

        # 2M Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 2MM/2MM
        self.option_940_limit_3670 = self.driver.find_element(By.ID, "option-940-limit-3670")

        # Deductibles
        # $0
        self.option_940_deductible_1187 = self.driver.find_element(By.ID, "option-940-deductible-1187")

        # 3M Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 3MM/3MM
        self.option_941_limit_3671 = self.driver.find_element(By.ID, "option-941-limit-3671")

        # Deductibles
        # $0
        self.option_941_deductible_1187 = self.driver.find_element(By.ID, "option-941-deductible-1187")

        # MEDEFENSE™ Plus and Cyber Liability Combined

        # Limits
        # 1MM/1MM
        self.option_663_limit_2758 = self.driver.find_element(By.ID, "option-663-limit-2758")

        # Deductibles
        # $1,500 / $0
        self.option_663_deductible_1188 = self.driver.find_element(By.ID, "option-663-deductible-1188")

        # 2M MEDEFENSE™ Plus and Cyber Liability Combined

        # Limits
        # 2MM/2MM
        self.option_950_limit_3672 = self.driver.find_element(By.ID, "option-950-limit-3672")

        # Deductibles
        # $1,500 / $0
        self.option_950_deductible_1188 = self.driver.find_element(By.ID, "option-950-deductible-1188")

        # 3M MEDEFENSE™ Plus and Cyber Liability Combined

        # Limits
        # 3MM/3MM
        self.option_951_limit_3673 = self.driver.find_element(By.ID, "option-951-limit-3673")

        # Deductibles
        # $1,500 / $0
        self.option_951_deductible_1188 = self.driver.find_element(By.ID, "option-951-deductible-1188")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_666_limit_2759 = self.driver.find_element(By.ID, "option-666-limit-2759")

        # Deductibles
        # $1,500 / $0
        self.option_666_deductible_1188 = self.driver.find_element(By.ID, "option-666-deductible-1188")

        # 2M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 2MM/2MM
        self.option_956_limit_3674 = self.driver.find_element(By.ID, "option-956-limit-3674")

        # Deductibles
        # $1,500 / $0
        self.option_956_deductible_1188 = self.driver.find_element(By.ID, "option-956-deductible-1188")


        # 3M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits

        # Limits
        # 3MM/3MM
        self.option_957_limit_3675 = self.driver.find_element(By.ID, "option-957-limit-3675")

        # Deductibles
        # $1,500 / $0
        self.option_957_deductible_1188 = self.driver.find_element(By.ID, "option-957-deductible-1188")

        # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_664_limit_2758 = self.driver.find_element(By.ID, "option-664-limit-2758")

        # Deductibles
        # $1,500 / $0
        self.option_664_deductible_1188 = self.driver.find_element(By.ID, "option-664-deductible-1188")

        # 2M MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 2MM/2MM
        self.option_952_limit_3672 = self.driver.find_element(By.ID, "option-952-limit-3672")

        # Deductibles
        # $1,500 / $0
        self.option_952_deductible_1188 = self.driver.find_element(By.ID, "option-952-deductible-1188")

        # 3M MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits

        # Limits
        # 3MM/3MM
        self.option_953_limit_3673 = self.driver.find_element(By.ID, "option-953-limit-3673")

        # Deductibles
        # $1,500 / $0
        self.option_953_deductible_1188 = self.driver.find_element(By.ID, "option-953-deductible-1188")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 1MM/1MM
        self.option_665_limit_2759 = self.driver.find_element(By.ID, "option-665-limit-2759")

        # Deductibles
        # $1,500 / $0
        self.option_665_deductible_1188 = self.driver.find_element(By.ID, "option-665-deductible-1188")

        # 2M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 2MM/2MM
        self.option_958_limit_3674 = self.driver.find_element(By.ID, "option-958-limit-3674")

        # Deductibles
        # $1,500 / $0
        self.option_958_deductible_1188 = self.driver.find_element(By.ID, "option-958-deductible-1188")

        # 3M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits

        # Limits
        # 3MM/3MM
        self.option_955_limit_3675 = self.driver.find_element(By.ID, "option-955-limit-3675")

        # Deductibles
        # $1,500 / $0
        self.option_955_deductible_1188 = self.driver.find_element(By.ID, "option-955-deductible-1188")

        return self

    def select_MEDEFENSE_Plus_Only(self):
        PCI_Coverage_Options.PageElements(self).option_658_limit_2753.click()
        PCI_Coverage_Options.PageElements(self).option_658_deductible_1186.click()

    def select_Cyber_Liability_Only(self):
        PCI_Coverage_Options.PageElements(self).option_659_limit_2754.click()
        PCI_Coverage_Options.PageElements(self).option_659_deductible_1187.click()

    def select_2MM_Cyber_Liability_Only(self):
        PCI_Coverage_Options.PageElements(self).option_934_limit_3668.click()
        PCI_Coverage_Options.PageElements(self).option_934_deductible_1187.click()

    def select_3MM_Cyber_Liability_Only(self):
        PCI_Coverage_Options.PageElements(self).option_935_limit_3669.click()
        PCI_Coverage_Options.PageElements(self).option_935_deductible_1187.click()

    def select_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_660_limit_2754.click()
        PCI_Coverage_Options.PageElements(self).option_660_deductible_1187.click()

    def select_2MM_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_936_limit_3668.click()
        PCI_Coverage_Options.PageElements(self).option_936_deductible_1187.click()

    def select_3MM_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_937_limit_3669.click()
        PCI_Coverage_Options.PageElements(self).option_937_deductible_1187.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_662_limit_2757.click()
        PCI_Coverage_Options.PageElements(self).option_662_deductible_1187.click()

    def select_2MM_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_940_limit_3670.click()
        PCI_Coverage_Options.PageElements(self).option_940_deductible_1187.click()

    def select_3MM_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_941_limit_3671.click()
        PCI_Coverage_Options.PageElements(self).option_941_deductible_1187.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_661_limit_2757.click()
        PCI_Coverage_Options.PageElements(self).option_661_deductible_1187.click()

    def select_2MM_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_938_limit_3670.click()
        PCI_Coverage_Options.PageElements(self).option_938_deductible_1187.click()

    def select_3MM_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_939_limit_3671.click()
        PCI_Coverage_Options.PageElements(self).option_939_deductible_1187.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_Combined(self):
        PCI_Coverage_Options.PageElements(self).option_663_limit_2758.click()
        PCI_Coverage_Options.PageElements(self).option_663_deductible_1188.click()

    def select_2MM_MEDEFENSE_Plus_and_Cyber_Liability_Combined(self):
        PCI_Coverage_Options.PageElements(self).option_950_limit_3672.click()
        PCI_Coverage_Options.PageElements(self).option_950_deductible_1188.click()

    def select_3MM_MEDEFENSE_Plus_and_Cyber_Liability_Combined(self):
        PCI_Coverage_Options.PageElements(self).option_951_limit_3673.click()
        PCI_Coverage_Options.PageElements(self).option_951_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_666_limit_2759.click()
        PCI_Coverage_Options.PageElements(self).option_666_deductible_1188.click()

    def select_2MM_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_956_limit_3674.click()
        PCI_Coverage_Options.PageElements(self).option_956_deductible_1188.click()

    def select_3MM_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_957_limit_3675.click()
        PCI_Coverage_Options.PageElements(self).option_957_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_664_limit_2758.click()
        PCI_Coverage_Options.PageElements(self).option_664_deductible_1188.click()

    def select_2MM_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_952_limit_3672.click()
        PCI_Coverage_Options.PageElements(self).option_952_deductible_1188.click()

    def select_3MM_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_953_limit_3673.click()
        PCI_Coverage_Options.PageElements(self).option_953_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_665_limit_2759.click()
        PCI_Coverage_Options.PageElements(self).option_665_deductible_1188.click()

    def select_2MM_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_958_limit_3674.click()
        PCI_Coverage_Options.PageElements(self).option_958_deductible_1188.click()

    def select_3MM_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_955_limit_3675.click()
        PCI_Coverage_Options.PageElements(self).option_955_deductible_1188.click()

