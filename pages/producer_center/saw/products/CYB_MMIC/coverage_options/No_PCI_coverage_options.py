from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

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

        # e-MD™ without PCI DSS Liability
        # Limits
        # 500K/500K
        self.option_695_limit_2829 = self.driver.find_element(By.ID, "option-695-limit-2829")

        # 1MM/1MM
        self.option_695_limit_2828 = self.driver.find_element(By.ID, "option-695-limit-2828")

        # Deductibles
        # $0
        self.option_695_deductible_1214 = self.driver.find_element(By.ID, "option-695-deductible-1214")

        # e-MD™ Higher Limits without PCI DSS Liability
        # Limits
        # 2MM/2MM
        self.option_700_limit_2834 = self.driver.find_element(By.ID, "option-700-limit-2834")

        # 3MM/3MM
        self.option_700_limit_2835 = self.driver.find_element(By.ID, "option-700-limit-2835")

        # Deductibles
        # $0
        self.option_700_deductible_1214 = self.driver.find_element(By.ID, "option-700-deductible-1214")

        # e-MD™ and MEDEFENSE+ without PCI DSS Liability
        # Limits
        # 500K/500K
        self.option_709_limit_2848 = self.driver.find_element(By.ID, "option-709-limit-2848")

        # 1MM/1MM
        self.option_709_limit_2849 = self.driver.find_element(By.ID, "option-709-limit-2849")

        # Deductibles
        # $0
        self.option_709_deductible_1216 = self.driver.find_element(By.ID, "option-709-deductible-1216")

        # e-MD™ Higher Limits and MEDEFENSE+ without PCI DSS Liability
        # Limits
        # 2MM/1MM/2MM
        self.option_713_limit_2854 = self.driver.find_element(By.ID, "option-713-limit-2854")

        # 3MM/1MM/3MM
        self.option_713_limit_2855 = self.driver.find_element(By.ID, "option-713-limit-2855")

        # Deductibles
        # $0
        self.option_713_deductible_1216 = self.driver.find_element(By.ID, "option-713-deductible-1216")


        # e-MD™ and MEDEFENSE+ with $50k Disciplinary without PCI DSS Liability
        # Limits
        # 2MM/50K/1MM/2MM
        self.option_717_limit_2860 = self.driver.find_element(By.ID, "option-717-limit-2860")

        # 3MM/50K/1MM/3MM
        self.option_717_limit_2861 = self.driver.find_element(By.ID, "option-717-limit-2861")

        # Deductibles
        # $0
        self.option_717_deductible_1216 = self.driver.find_element(By.ID, "option-717-deductible-1216")


        # e-MD™ Higher Limits and MEDEFENSE+ with $50k Disciplinary without PCI DSS Liability
        # Limits
        # 2MM/50K/1MM/2MM
        self.option_722_limit_2866 = self.driver.find_element(By.ID, "option-722-limit-2866")

        # 3MM/50K/1MM/3MM
        self.option_722_limit_2867 = self.driver.find_element(By.ID, "option-722-limit-2867")

        # Deductibles
        # $0
        self.option_722_deductible_1216 = self.driver.find_element(By.ID, "option-722-deductible-1216")

        # e-MD™ and MEDEFENSE+ Separate Limits without PCI DSS Liability
        # Limits
        # 500K/1MM
        self.option_721_limit_2872 = self.driver.find_element(By.ID, "option-721-limit-2872")

        # 1MM/2MM
        self.option_721_limit_2873 = self.driver.find_element(By.ID, "option-721-limit-2873")

        # Deductibles
        # $0
        self.option_721_deductible_1216 = self.driver.find_element(By.ID, "option-721-deductible-1216")

        # e-MD™ Higher Limits and MEDEFENSE+ Separate Limits without PCI DSS Liability
        # Limits
        # 2MM/1MM/3MM
        self.option_729_limit_2878 = self.driver.find_element(By.ID, "option-729-limit-2878")

        # 3MM/1MM/4MM
        self.option_729_limit_2879 = self.driver.find_element(By.ID, "option-729-limit-2879")

        # Deductibles
        # $0
        self.option_729_deductible_1216 = self.driver.find_element(By.ID, "option-729-deductible-1216")

        # e-MD™ and MEDEFENSE+ with $50k Disciplinary Separate Limits without PCI DSS Liability
        # Limits
        # 2MM/1MM/3MM
        self.option_733_limit_2884 = self.driver.find_element(By.ID, "option-733-limit-2884")

        # 3MM/1MM/4MM
        self.option_733_limit_2885 = self.driver.find_element(By.ID, "option-733-limit-2885")

        # Deductibles
        # $0
        self.option_733_deductible_1216 = self.driver.find_element(By.ID, "option-733-deductible-1216")

        # e-MD™ Higher Limits and MEDEFENSE+ with $50k Disciplinary Separate Limits without PCI DSS Liability
        # Limits
        # 2MM/50K/1MM/3MM
        self.option_737_limit_2890 = self.driver.find_element(By.ID, "option-737-limit-2890")

        # 3MM/50K/1MM/4MM
        self.option_737_limit_2891 = self.driver.find_element(By.ID, "option-737-limit-2891")

        # Deductibles
        # $0
        self.option_737_deductible_1216 = self.driver.find_element(By.ID, "option-737-deductible-1216")

        return self

    # NON-PCI Options

    # select_MEDEFENSE_Plus_Only_500K()
    # select_MEDEFENSE_Plus_Only_1MM()
    # select_MEDEFENSE_with_50K_Disciplinary_500K()
    # select_MEDEFENSE_with_50K_Disciplinary_1MM()
    # select_eMD_without_PCI_DSS_Liability_500K()
    # select_eMD_without_PCI_DSS_Liability_1MM()
    # select_eMD_Higher_Limits_without_PCI_DSS_Liability_2MM()
    # select_eMD_Higher_Limits_without_PCI_DSS_Liability_3MM()
    # select_eMD_and_MEDEFENSE_without_PCI_DSS_Liability_500K()
    # select_eMD_and_MEDEFENSE_without_PCI_DSS_Liability_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_without_PCI_DSS_Liability_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_without_PCI_DSS_Liability_3MM()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_500K()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_3MM()
    # select_eMD_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_500K()
    # select_eMD_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_3MM()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_500K()
    # select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_1MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_2MM()
    # select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_3MM()

    def select_MEDEFENSE_Plus_Only_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_690_limit_2816.click()
        No_PCI_Coverage_Options.PageElements(self).option_690_deductible_884.click()

    def select_MEDEFENSE_Plus_Only_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_690_limit_2815.click()
        No_PCI_Coverage_Options.PageElements(self).option_690_deductible_884.click()

    def select_MEDEFENSE_with_50K_Disciplinary_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_691_limit_2818.click()
        No_PCI_Coverage_Options.PageElements(self).option_691_deductible_884.click()

    def select_MEDEFENSE_with_50K_Disciplinary_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_691_limit_2817.click()
        No_PCI_Coverage_Options.PageElements(self).option_691_deductible_884.click()

    def select_eMD_without_PCI_DSS_Liability_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_695_limit_2829.click()
        No_PCI_Coverage_Options.PageElements(self).option_695_deductible_1214.click()

    def select_eMD_without_PCI_DSS_Liability_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_695_limit_2828.click()
        No_PCI_Coverage_Options.PageElements(self).option_695_deductible_1214.click()

    def select_eMD_Higher_Limits_without_PCI_DSS_Liability_2MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_700_limit_2834.click()
        No_PCI_Coverage_Options.PageElements(self).option_700_deductible_1214.click()

    def select_eMD_Higher_Limits_without_PCI_DSS_Liability_3MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_700_limit_2835.click()
        No_PCI_Coverage_Options.PageElements(self).option_700_deductible_1214.click()

    def select_eMD_and_MEDEFENSE_without_PCI_DSS_Liability_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_709_limit_2848.click()
        No_PCI_Coverage_Options.PageElements(self).option_709_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_without_PCI_DSS_Liability_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_709_limit_2849.click()
        No_PCI_Coverage_Options.PageElements(self).option_709_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_without_PCI_DSS_Liability_2MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_713_limit_2854.click()
        No_PCI_Coverage_Options.PageElements(self).option_713_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_without_PCI_DSS_Liability_3MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_713_limit_2855.click()
        No_PCI_Coverage_Options.PageElements(self).option_713_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_717_limit_2860.click()
        No_PCI_Coverage_Options.PageElements(self).option_717_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_717_limit_2861.click()
        No_PCI_Coverage_Options.PageElements(self).option_717_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_2MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_722_limit_2866.click()
        No_PCI_Coverage_Options.PageElements(self).option_722_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_without_PCI_DSS_Liability_3MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_722_limit_2867.click()
        No_PCI_Coverage_Options.PageElements(self).option_722_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_721_limit_2872.click()
        No_PCI_Coverage_Options.PageElements(self).option_721_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_721_limit_2873.click()
        No_PCI_Coverage_Options.PageElements(self).option_721_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_2MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_729_limit_2878.click()
        No_PCI_Coverage_Options.PageElements(self).option_729_deductible_1216.click()

    def eMD_Higher_Limits_and_MEDEFENSE_Separate_Limits_without_PCI_DSS_Liability_3MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_729_limit_2879.click()
        No_PCI_Coverage_Options.PageElements(self).option_729_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_500K(self):
        No_PCI_Coverage_Options.PageElements(self).option_733_limit_2884.click()
        No_PCI_Coverage_Options.PageElements(self).option_733_deductible_1216.click()

    def select_eMD_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_1MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_733_limit_2885.click()
        No_PCI_Coverage_Options.PageElements(self).option_733_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_2MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_737_limit_2890.click()
        No_PCI_Coverage_Options.PageElements(self).option_737_deductible_1216.click()

    def select_eMD_Higher_Limits_and_MEDEFENSE_with_50k_Disciplinary_Separate_Limits_without_PCI_DSS_Liability_3MM(self):
        No_PCI_Coverage_Options.PageElements(self).option_737_limit_2891.click()
        No_PCI_Coverage_Options.PageElements(self).option_737_deductible_1216.click()

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