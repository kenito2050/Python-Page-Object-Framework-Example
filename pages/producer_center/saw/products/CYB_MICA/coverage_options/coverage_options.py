from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PCI_PageElements(self):

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

        Coverage_Options.PCI_PageElements(self).option_658_limit_2753.click()
        Coverage_Options.PCI_PageElements(self).option_658_deductible_1186.click()

    def select_Cyber_Liability_Only(self):

        Coverage_Options.PCI_PageElements(self).option_659_limit_2754.click()
        Coverage_Options.PCI_PageElements(self).option_659_deductible_1187.click()

    def select_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):

        Coverage_Options.PCI_PageElements(self).option_660_limit_2754.click()
        Coverage_Options.PCI_PageElements(self).option_660_deductible_1187.click()


    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):

        Coverage_Options.PCI_PageElements(self).option_661_limit_2757.click()
        Coverage_Options.PCI_PageElements(self).option_661_deductible_1187.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):

        Coverage_Options.PCI_PageElements(self).option_662_limit_2757.click()
        Coverage_Options.PCI_PageElements(self).option_662_deductible_1187.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_Combined(self):

        Coverage_Options.PCI_PageElements(self).option_663_limit_2758.click()
        Coverage_Options.PCI_PageElements(self).option_663_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits(self):

        Coverage_Options.PCI_PageElements(self).option_664_limit_2758.click()
        Coverage_Options.PCI_PageElements(self).option_664_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits(self):
        Coverage_Options.PCI_PageElements(self).option_665_limit_2759.click()
        Coverage_Options.PCI_PageElements(self).option_665_deductible_1188.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits(self):
        Coverage_Options.PCI_PageElements(self).option_666_limit_2759.click()
        Coverage_Options.PCI_PageElements(self).option_666_deductible_1188.click()

    def NO_PCI_PageElements(self):
        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_658_limit_2753 = self.driver.find_element(By.ID, "option-658-limit-2753")

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
        Coverage_Options.NO_PCI_PageElements(self).option_667_limit_2760.click()
        Coverage_Options.NO_PCI_PageElements(self).option_667_deductible_1189.click()

    def select_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(self):
        Coverage_Options.NO_PCI_PageElements(self).option_668_limit_2760.click()
        Coverage_Options.NO_PCI_PageElements(self).option_668_deductible_1189.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_No_PCI(self):
        Coverage_Options.NO_PCI_PageElements(self).option_669_limit_2761.click()
        Coverage_Options.NO_PCI_PageElements(self).option_669_deductible_1189.click()

    def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(
            self):
        Coverage_Options.NO_PCI_PageElements(self).option_670_limit_2761.click()
        Coverage_Options.NO_PCI_PageElements(self).option_670_deductible_1189.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_Combined_No_PCI(self):
        Coverage_Options.NO_PCI_PageElements(self).option_671_limit_2762.click()
        Coverage_Options.NO_PCI_PageElements(self).option_671_deductible_1190.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(self):
        Coverage_Options.NO_PCI_PageElements(self).option_672_limit_2762.click()
        Coverage_Options.NO_PCI_PageElements(self).option_672_deductible_1190.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_No_PCI(self):
        Coverage_Options.NO_PCI_PageElements(self).option_673_limit_2763.click()
        Coverage_Options.NO_PCI_PageElements(self).option_673_deductible_1190.click()

    def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(
            self):

        Coverage_Options.NO_PCI_PageElements(self).option_674_limit_2763.click()
        Coverage_Options.NO_PCI_PageElements(self).option_674_deductible_1190.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()