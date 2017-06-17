from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PCI_PageElements(self):

        # e-MD™ and MEDEFENSE+

        # Limits
        # 500K/500K
        self.option_446_limit_1966 = self.driver.find_element(By.ID, "option-446-limit-1966")

        # 1MM/1MM
        self.option_446_limit_1965 = self.driver.find_element(By.ID, "option-446-limit-1965")

        # Deductibles
        # $0
        self.option_446_deductible_760 = self.driver.find_element(By.ID, "option-446-deductible-760")

        # e-MD™ and MEDEFENSE+ with $50k Disciplinary

        # Limits
        # 500K/50K/500K
        self.option_447_limit_1968 = self.driver.find_element(By.ID, "option-447-limit-1968")

        # 1MM/50K/1MM
        self.option_447_limit_1967 = self.driver.find_element(By.ID, "option-447-limit-1967")

        # Deductibles
        # $0 / $0
        self.option_447_deductible_760 = self.driver.find_element(By.ID, "option-447-deductible-760")

        # e-MD™ and MEDEFENSE+ Separate Limits

        # Limits
        # 500K/500K/1MM
        self.option_448_limit_1970 = self.driver.find_element(By.ID, "option-448-limit-1970")

        # 1MM/1MM
        self.option_448_limit_1969 = self.driver.find_element(By.ID, "option-448-limit-1969")

        # Deductibles
        # $0
        self.option_448_deductible_760 = self.driver.find_element(By.ID, "option-448-deductible-760")


        # e-MD™ and MEDEFENSE+ with $50k Disciplinary Separate Limits

        # Limits
        # 500K/50K/500K/1MM
        self.option_449_limit_1972 = self.driver.find_element(By.ID, "option-449-limit-1972")

        # 1MM/50K/1MM/2MM
        self.option_449_limit_1971 = self.driver.find_element(By.ID, "option-449-limit-1971")

        # Deductibles
        # $0/ $0
        self.option_449_deductible_760 = self.driver.find_element(By.ID, "option-449-deductible-760")

        # MEDEFENSE+ with $50K Disciplinary

        # Limits

        # 500K/50K/500K
        self.option_519_limit_2311 = self.driver.find_element(By.ID, "option-519-limit-2311")

        # 1MM/50K/1MM
        self.option_519_limit_2310 = self.driver.find_element(By.ID, "option-519-limit-2310")

        # Deductibles
        # $0
        self.option_519_deductible_884 = self.driver.find_element(By.ID, "option-519-deductible-884")

        # MEDEFENSE™ Plus Only

        # Limits
        # 500K/500K
        self.option_320_limit_1646 = self.driver.find_element(By.ID, "option-320-limit-1646")

        # 1MM/1MM
        self.option_320_limit_1645 = self.driver.find_element(By.ID, "option-320-limit-1645")

        # Deductibles
        # $0
        self.option_320_deductible_613 = self.driver.find_element(By.ID, "option-320-deductible-613")

        # e-MD™

        # Limits

        # 500K/500K
        self.option_463_limit_2028 = self.driver.find_element(By.ID, "option-463-limit-2028")

        # 1MM/1MM
        self.option_463_limit_2027 = self.driver.find_element(By.ID, "option-463-limit-2027")

        # Deductibles
        # $0
        self.option_463_deductible_774 = self.driver.find_element(By.ID, "option-463-deductible-774")

        ### This section was used for testing Class-Based Limits
        # # e-MD™ Higher Limits
        #
        # # Limits
        # # 2MM/2MM
        # self.option_679_limit_2770 = self.driver.find_element(By.ID, "option-679-limit-2770")
        #
        # # Deductibles
        # # $0
        # self.option_679_deductible_774 = self.driver.find_element(By.ID, "option-679-deductible-774")

        return self

    # saw_CC.select_e_MD_and_MEDEFENSE_500K_limit()
    # saw_CC.select_e_MD_and_MEDEFENSE_1MM_limit()
    # saw_CC.select_MEDEFENSE_with_50K_Disciplinary_500K_limit()
    # saw_CC.select_MEDEFENSE_with_50K_Disciplinary_1MM_limit()
    # saw_CC.select_e_MD_and_MEDEFENSE_Separate_Limits_500K_limit()
    # saw_CC.select_e_MD_and_MEDEFENSE_Separate_Limits_1MM_limit()
    # saw_CC.select_e_MD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_500K_limit()
    # saw_CC.select_e_MD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_1MM_limit()
    # saw_CC.select_MEDEFENSE_with_50K_Disciplinary_500K_limit()
    # saw_CC.select_MEDEFENSE_with_50K_Disciplinary_1MM_limit()
    # saw_CC.select_MEDEFENSE_Only_500K_limit()
    # saw_CC.select_MEDEFENSE_Only_1MM_limit()
    # saw_CC.select_e_MD_500K_limit()
    # saw_CC.select_e_MD_1MM_limit()

    def select_e_MD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_449_limit_1972.click()
        Coverage_Options.PCI_PageElements(self).option_449_deductible_760.click()

    def select_e_MD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_449_limit_1971.click()
        Coverage_Options.PCI_PageElements(self).option_449_deductible_760.click()

    def select_e_MD_and_MEDEFENSE_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_446_limit_1966.click()
        Coverage_Options.PCI_PageElements(self).option_446_deductible_760.click()

    def select_e_MD_and_MEDEFENSE_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_446_limit_1965.click()
        Coverage_Options.PCI_PageElements(self).option_446_deductible_760.click()

    def select_MEDEFENSE_with_50K_Disciplinary_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_447_limit_1968.click()
        Coverage_Options.PCI_PageElements(self).option_447_deductible_760.click()

    def select_MEDEFENSE_with_50K_Disciplinary_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_447_limit_1967.click()
        Coverage_Options.PCI_PageElements(self).option_447_deductible_760.click()

    def select_e_MD_and_MEDEFENSE_Separate_Limits_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_448_limit_1970.click()
        Coverage_Options.PCI_PageElements(self).option_448_deductible_760.click()

    def select_e_MD_and_MEDEFENSE_Separate_Limits_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_448_limit_1969.click()
        Coverage_Options.PCI_PageElements(self).option_448_deductible_760.click()

    def select_MEDEFENSE_with_50k_Disciplinary_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_519_limit_2311.click()
        Coverage_Options.PCI_PageElements(self).option_519_deductible_884.click()

    def select_MEDEFENSE_with_50k_Disciplinary_500K_limit_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_519_limit_2310.click()
        Coverage_Options.PCI_PageElements(self).option_519_deductible_884.click()

    def select_MEDEFENSE_Only_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_320_limit_1646.click()
        Coverage_Options.PCI_PageElements(self).option_320_deductible_613.click()

    def select_MEDEFENSE_Only_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_320_limit_1645.click()
        Coverage_Options.PCI_PageElements(self).option_320_deductible_613.click()

    def select_e_MD_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_463_limit_2028.click()
        Coverage_Options.PCI_PageElements(self).option_463_deductible_774.click()

    def select_e_MD_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_463_limit_2027.click()
        Coverage_Options.PCI_PageElements(self).option_463_deductible_774.click()

    # def select_e_MD_Higher_Limits(self):
    #
    #     Coverage_Options.PCI_PageElements(self).option_679_limit_2770.click()
    #     Coverage_Options.PCI_PageElements(self).option_679_deductible_774.click()

    # ALL Elements & Options below this line were updated on 6-16-17 -- Ken

    # saw_CC.select_MEDEFENSE_with_50K_Disciplinary_500K_limit()
    # saw_CC.select_MEDEFENSE_with_50K_Disciplinary_1MM_limit()
    # saw_CC.select_MEDEFENSE_Only_500K_limit()
    # saw_CC.select_MEDEFENSE_Only_1MM_limit()


    # def NO_PCI_PageElements(self):
    #     # MEDEFENSE™ Plus Only
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_658_limit_2753 = self.driver.find_element(By.ID, "option-658-limit-2753")
    #
    #     # Deductibles
    #     # $1,500
    #     self.option_658_deductible_1186 = self.driver.find_element(By.ID, "option-658-deductible-1186")
    #
    #     # Cyber Liability Only - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_667_limit_2760 = self.driver.find_element(By.ID, "option-667-limit-2760")
    #
    #     # Deductibles
    #     # $0
    #     self.option_667_deductible_1189 = self.driver.find_element(By.ID, "option-667-deductible-1189")
    #
    #     # Cyber Liability with Breach Event Costs Outside the Limits - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_668_limit_2760 = self.driver.find_element(By.ID, "option-668-limit-2760")
    #
    #     # Deductibles
    #     # $0
    #     self.option_668_deductible_1189 = self.driver.find_element(By.ID, "option-668-deductible-1189")
    #
    #     # Cyber Liability with Claims Expenses Outside the Limits - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_669_limit_2761 = self.driver.find_element(By.ID, "option-669-limit-2761")
    #
    #     # Deductibles
    #     # $0
    #     self.option_669_deductible_1189 = self.driver.find_element(By.ID, "option-669-deductible-1189")
    #
    #     # Cyber Liability with Claims Expenses Outside the Limits and with Breach Event Costs Outside the Limits - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_670_limit_2761 = self.driver.find_element(By.ID, "option-670-limit-2761")
    #
    #     # Deductibles
    #     # $0
    #     self.option_670_deductible_1189 = self.driver.find_element(By.ID, "option-670-deductible-1189")
    #
    #     # MEDEFENSE™ Plus and Cyber Liability Combined - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_671_limit_2762 = self.driver.find_element(By.ID, "option-671-limit-2762")
    #
    #     # Deductibles
    #     # $1,500 / $0
    #     self.option_671_deductible_1190 = self.driver.find_element(By.ID, "option-671-deductible-1190")
    #
    #     # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_672_limit_2762 = self.driver.find_element(By.ID, "option-672-limit-2762")
    #
    #     # Deductibles
    #     # $1,500 / $0
    #     self.option_672_deductible_1190 = self.driver.find_element(By.ID, "option-672-deductible-1190")
    #
    #     # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_673_limit_2763 = self.driver.find_element(By.ID, "option-673-limit-2763")
    #
    #     # Deductibles
    #     # $1,500 / $0
    #     self.option_673_deductible_1190 = self.driver.find_element(By.ID, "option-673-deductible-1190")
    #
    #     # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits - No PCI
    #
    #     # Limits
    #     # 1MM/1MM
    #     self.option_674_limit_2763 = self.driver.find_element(By.ID, "option-674-limit-2763")
    #
    #     # Deductibles
    #     # $1,500 / $0
    #     self.option_674_deductible_1190 = self.driver.find_element(By.ID, "option-674-deductible-1190")
    #
    #     return self
    #
    # def select_Cyber_Liability_Only_No_PCI(self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_667_limit_2760.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_667_deductible_1189.click()
    #
    # def select_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_668_limit_2760.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_668_deductible_1189.click()
    #
    # def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_No_PCI(self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_669_limit_2761.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_669_deductible_1189.click()
    #
    # def select_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(
    #         self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_670_limit_2761.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_670_deductible_1189.click()
    #
    # def select_MEDEFENSE_Plus_and_Cyber_Liability_Combined_No_PCI(self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_671_limit_2762.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_671_deductible_1190.click()
    #
    # def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_672_limit_2762.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_672_deductible_1190.click()
    #
    # def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_No_PCI(self):
    #     Coverage_Options.NO_PCI_PageElements(self).option_673_limit_2763.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_673_deductible_1190.click()
    #
    # def select_MEDEFENSE_Plus_and_Cyber_Liability_with_Claims_Expenses_Outside_the_Limits_and_with_Breach_Event_Costs_Outside_the_Limits_No_PCI(
    #         self):
    #
    #     Coverage_Options.NO_PCI_PageElements(self).option_674_limit_2763.click()
    #     Coverage_Options.NO_PCI_PageElements(self).option_674_deductible_1190.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()