from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only
        # Limits
        # 500K/500K
        self.option_690_limit_2816 = self.driver.find_element(By.ID, "option-690-limit-2816")

        # 1MM/1MM
        self.option_690_limit_2815 = self.driver.find_element(By.ID, "option-690-limit-2815")

        # Deductibles
        # $0
        self.option_690_deductible_884 = self.driver.find_element(By.ID, "option-690-deductible-884")

        # MEDEFENSE+ with $50K Disciplinary
        # Limits
        # 500K/50K/500K
        self.option_691_limit_2818 = self.driver.find_element(By.ID, "option-691-limit-2818")

        # 1MM/50K/1MM
        self.option_691_limit_2817 = self.driver.find_element(By.ID, "option-691-limit-2817")

        # Deductibles
        # $0
        self.option_691_deductible_884 = self.driver.find_element(By.ID, "option-691-deductible-884")

        # e-MD™
        # Limits
        # 500K/500K
        self.option_694_limit_2825 = self.driver.find_element(By.ID, "option-694-limit-2825")

        # 1MM/1MM
        self.option_694_limit_2824 = self.driver.find_element(By.ID, "option-694-limit-2824")

        # Deductibles
        # $0
        self.option_694_deductible_1212 = self.driver.find_element(By.ID, "option-694-deductible-1212")

        # e-MD™ Higher Limits
        # Limits
        # 500K/500K
        self.option_679_limit_2770 = self.driver.find_element(By.ID, "option-679-limit-2770")

        # 1MM/1MM
        self.option_679_limit_2819 = self.driver.find_element(By.ID, "option-679-limit-2819")

        # Deductibles
        # $0
        self.option_679_deductible_1212 = self.driver.find_element(By.ID, "option-679-deductible-1212")

        # e-MD™ and MEDEFENSE+
        # Limits
        # 500K/500K
        self.option_703_limit_2840 = self.driver.find_element(By.ID, "option-703-limit-2840")

        # 1MM/1MM
        self.option_703_limit_2842 = self.driver.find_element(By.ID, "option-703-limit-2842")

        # Deductibles
        # $0
        self.option_703_deductible_1211 = self.driver.find_element(By.ID, "option-703-deductible-1211")

        # e-MD™ Higher Limits and MEDEFENSE+
        # Limits
        # 2MM/1MM/2MM
        self.option_675_limit_2766 = self.driver.find_element(By.ID, "option-675-limit-2766")

        # 3MM/1MM/3MM
        self.option_675_limit_2820 = self.driver.find_element(By.ID, "option-675-limit-2820")

        # Deductibles
        # $0
        self.option_675_deductible_1211 = self.driver.find_element(By.ID, "option-675-deductible-1211")

        # e-MD™ and MEDEFENSE+ with $50k Disciplinary
        # 500K/50K/500K
        self.option_704_limit_2841 = self.driver.find_element(By.ID, "option-704-limit-2841")

        # 1MM/50K/1MM
        self.option_704_limit_2843 = self.driver.find_element(By.ID, "option-704-limit-2843")

        # Deductibles
        # $0
        self.option_704_deductible_1211 = self.driver.find_element(By.ID, "option-704-deductible-1211")

        # e-MD™ Higher Limits and MEDEFENSE+ with $50k Disciplinary

        # Limits
        # 2MM/50K/1MM/2MM
        self.option_676_limit_2767 = self.driver.find_element(By.ID, "option-676-limit-2767")

        # 3MM/50K/1MM/3MM
        self.option_676_limit_2821 = self.driver.find_element(By.ID, "option-676-limit-2821")

        # Deductibles
        # $0
        self.option_676_deductible_1211 = self.driver.find_element(By.ID, "option-676-deductible-1211")

        # e-MD™ and MEDEFENSE+ Separate Limits

        # Limits
        # 500K/1MM
        self.option_706_limit_2844 = self.driver.find_element(By.ID, "option-706-limit-2844")

        # 1MM/2MM
        self.option_706_limit_2845 = self.driver.find_element(By.ID, "option-706-limit-2845")

        # Deductibles
        # $0
        self.option_706_deductible_1211 = self.driver.find_element(By.ID, "option-706-deductible-1211")

        # e-MD™ Higher Limits and MEDEFENSE+ Separate Limits
        # Limits
        # 2MM/1MM/3MM
        self.option_677_limit_2768 = self.driver.find_element(By.ID, "option-677-limit-2768")

        # 3MM/1MM/4MM
        self.option_677_limit_2822 = self.driver.find_element(By.ID, "option-677-limit-2822")

        # Deductibles
        # $0
        self.option_677_deductible_1211 = self.driver.find_element(By.ID, "option-677-deductible-1211")

        # e-MD™ and MEDEFENSE+ with $50k Disciplinary Separate Limits
        # Limits
        # 500K/50K/1MM
        self.option_707_limit_2846 = self.driver.find_element(By.ID, "option-707-limit-2846")

        # 1MM/50K/2MM
        self.option_707_limit_2847 = self.driver.find_element(By.ID, "option-707-limit-2847")

        # Deductibles
        # $0
        self.option_707_deductible_1211 = self.driver.find_element(By.ID, "option-707-deductible-1211")

        # e-MD™ Higher Limits and MEDEFENSE+ with $50k Disciplinary Separate Limits
        # Limits
        # 2MM/50K/1MM/3MM
        self.option_678_limit_2769 = self.driver.find_element(By.ID, "option-678-limit-2769")

        # 3MM/50K/1MM/4MM
        self.option_678_limit_2823 = self.driver.find_element(By.ID, "option-678-limit-2823")

        # Deductibles
        # $0
        self.option_678_deductible_1211 = self.driver.find_element(By.ID, "option-678-deductible-1211")

        return self

    # PCI Options

    # select_MEDEFENSE_Plus_Only_500K()
    # select_MEDEFENSE_Plus_Only_1MM()
    # select_MEDEFENSE_with_50K_Disciplinary_500K()
    # select_MEDEFENSE_with_50K_Disciplinary_1MM()
    # select_eMD_500K()
    # select_eMD_1MM()
    # select_eMD_Higher_Limits_2MM()
    # select_eMD_Higher_Limits_3MM()
    # select_eMD_MEDEFENSE_Plus_500K()
    # select_eMD_MEDEFENSE_Plus_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_3MM()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_500K()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_3MM()
    # select_eMD_and_MEDEFENSE_Separate_Limits_500K()
    # select_eMD_and_MEDEFENSE_Separate_Limits_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_3MM()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_500K()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_3MM()

    def select_MEDEFENSE_Plus_Only_500K(self):
        PCI_Coverage_Options.PageElements(self).option_690_limit_2816.click()
        PCI_Coverage_Options.PageElements(self).option_690_deductible_884.click()

    def select_MEDEFENSE_Plus_Only_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_690_limit_2815.click()
        PCI_Coverage_Options.PageElements(self).option_690_deductible_884.click()

    def select_MEDEFENSE_with_50K_Disciplinary_500K(self):
        PCI_Coverage_Options.PageElements(self).option_691_limit_2818.click()
        PCI_Coverage_Options.PageElements(self).option_691_deductible_884.click()

    def select_MEDEFENSE_with_50K_Disciplinary_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_691_limit_2817.click()
        PCI_Coverage_Options.PageElements(self).option_691_deductible_884.click()

    def select_eMD_500K(self):
        PCI_Coverage_Options.PageElements(self).option_694_limit_2825.click()
        PCI_Coverage_Options.PageElements(self).option_694_deductible_1212.click()

    def select_eMD_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_694_limit_2824.click()
        PCI_Coverage_Options.PageElements(self).option_694_deductible_1212.click()

    def select_eMD_Higher_Limits_2MM(self):
        PCI_Coverage_Options.PageElements(self).option_679_limit_2770.click()
        PCI_Coverage_Options.PageElements(self).option_679_deductible_1212.click()

    def select_eMD_Higher_Limits_3MM(self):
        PCI_Coverage_Options.PageElements(self).option_679_limit_2819.click()
        PCI_Coverage_Options.PageElements(self).option_679_deductible_1212.click()

    def select_eMD_MEDEFENSE_Plus_500K(self):
        PCI_Coverage_Options.PageElements(self).option_703_limit_2840.click()
        PCI_Coverage_Options.PageElements(self).option_703_deductible_1211.click()

    def select_eMD_MEDEFENSE_Plus_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_703_limit_2842.click()
        PCI_Coverage_Options.PageElements(self).option_703_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_2MM(self):
        PCI_Coverage_Options.PageElements(self).option_675_limit_2766.click()
        PCI_Coverage_Options.PageElements(self).option_675_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_3MM(self):
        PCI_Coverage_Options.PageElements(self).option_675_limit_2820.click()
        PCI_Coverage_Options.PageElements(self).option_675_deductible_1211.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_500K(self):
        PCI_Coverage_Options.PageElements(self).option_704_limit_2841.click()
        PCI_Coverage_Options.PageElements(self).option_704_deductible_1211.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_704_limit_2843.click()
        PCI_Coverage_Options.PageElements(self).option_704_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_2MM(self):
        PCI_Coverage_Options.PageElements(self).option_676_limit_2767.click()
        PCI_Coverage_Options.PageElements(self).option_676_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_3MM(self):
        PCI_Coverage_Options.PageElements(self).option_676_limit_2821.click()
        PCI_Coverage_Options.PageElements(self).option_676_deductible_1211.click()

    def select_eMD_and_MEDEFENSE_Separate_Limits_500K(self):
        PCI_Coverage_Options.PageElements(self).option_706_limit_2844.click()
        PCI_Coverage_Options.PageElements(self).option_706_deductible_1211.click()

    def select_eMD_and_MEDEFENSE_Separate_Limits_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_706_limit_2845.click()
        PCI_Coverage_Options.PageElements(self).option_706_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_2MM(self):
        PCI_Coverage_Options.PageElements(self).option_677_limit_2768.click()
        PCI_Coverage_Options.PageElements(self).option_677_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_3MM(self):
        PCI_Coverage_Options.PageElements(self).option_677_limit_2822.click()
        PCI_Coverage_Options.PageElements(self).option_677_deductible_1211.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_500K(self):
        PCI_Coverage_Options.PageElements(self).option_707_limit_2846.click()
        PCI_Coverage_Options.PageElements(self).option_707_deductible_1211.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_1MM(self):
        PCI_Coverage_Options.PageElements(self).option_707_limit_2847.click()
        PCI_Coverage_Options.PageElements(self).option_707_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_2MM(self):
        PCI_Coverage_Options.PageElements(self).option_678_limit_2769.click()
        PCI_Coverage_Options.PageElements(self).option_678_deductible_1211.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_3MM(self):
        PCI_Coverage_Options.PageElements(self).option_678_limit_2823.click()
        PCI_Coverage_Options.PageElements(self).option_678_deductible_1211.click()

    #### END No PCI Options Section


    def select_all_deselect_all(self):
        select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")
        select_deselect_all.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()