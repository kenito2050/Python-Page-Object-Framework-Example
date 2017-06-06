from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

            # Select / Deselect All
            self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

            # Proceed to Quote
            self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                        "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
            # Return to Admin Interface
            self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

            # Additional Coverage Options

            # First Dollar Defense
            self.first_dollar_defense = self.driver.find_element(By.ID, "product-form-952")

            return self


    def Netguard_Plus_options_limits_deductibles(self):

        # NetGuard™ Plus

        # Limits

        # $500K / $500K (with $25K NetGuard™ Plus)
        self.option_222_limit_1168_500K = self.driver.find_element(By.ID, "option-222-limit-1168")

        # $500K / $500K (with $100K NetGuard™ Plus)
        self.option_222_limit_1174_500K = self.driver.find_element(By.ID, "option-222-limit-1174")

        # $1MM / $1MM (with $25K NetGuard™ Plus)
        self.option_222_limit_1169_1MM = self.driver.find_element(By.ID, "option-222-limit-1169")

        # $1MM / $2MM (with $25K NetGuard™ Plus)
        self.option_222_limit_1178_1MM = self.driver.find_element(By.ID, "option-222-limit-1178")

        # $1MM / $1MM (with $100K NetGuard™ Plus)
        self.option_222_limit_1175_1MM = self.driver.find_element(By.ID, "option-222-limit-1175")

        # $1MM / $2MM (with $100K NetGuard™ Plus)
        self.option_222_limit_1179_1MM = self.driver.find_element(By.ID, "option-222-limit-1179")

        # Deductibles

        # $1,000
        self.option_222_deductible_513_1K = self.driver.find_element(By.ID, "option-222-deductible-513")

        # $2,500
        self.option_222_deductible_512_2_pt5_K = self.driver.find_element(By.ID, "option-222-deductible-512")

        # $5,000
        self.option_222_deductible_514_5K = self.driver.find_element(By.ID, "option-222-deductible-514")

        # $10,000
        self.option_222_deductible_515_10K = self.driver.find_element(By.ID, "option-222-deductible-515")

        # $15,000
        self.option_222_deductible_516_15K = self.driver.find_element(By.ID, "option-222-deductible-516")

        return self


    def Netguard_Plus_Additional_Claims_Expenses_options_limits_deductibles (self):

        # NetGuard™ Plus and Additional Claims Expenses

        # Limits

        # $500K / $500K (with $25K NetGuard™ Plus)
        self.option_476_limit_2120_500K = self.driver.find_element(By.ID, "option-476-limit-2120")

        # $500K / $500K (with $100K NetGuard™ Plus)
        self.option_476_limit_2123_500K = self.driver.find_element(By.ID, "option-476-limit-2123")

        # $1MM / $1MM (with $25K NetGuard™ Plus)
        self.option_476_limit_2125_1MM = self.driver.find_element(By.ID, "option-476-limit-2125")

        # $1MM / $2MM (with $25K NetGuard™ Plus)
        self.option_476_limit_2130_1MM = self.driver.find_element(By.ID, "option-476-limit-2130")

        # $1MM / $1MM (with $100K NetGuard™ Plus)
        self.option_476_limit_2124_1MM = self.driver.find_element(By.ID, "option-476-limit-2124")

        # $1MM / $2MM (with $100K NetGuard™ Plus)
        self.option_476_limit_2131_1MM = self.driver.find_element(By.ID, "option-476-limit-2131")

        # Deductibles

        # $1,000
        self.option_476_deductible_513_1K = self.driver.find_element(By.ID, "option-476-deductible-513")

        # $2,500
        self.option_476_deductible_512_2_pt5_K = self.driver.find_element(By.ID, "option-476-deductible-512")

        # $5,000
        self.option_476_deductible_514_5K = self.driver.find_element(By.ID, "option-476-deductible-514")

        # $10,000
        self.option_476_deductible_515_10K = self.driver.find_element(By.ID, "option-476-deductible-515")

        # $15,000
        self.option_476_deductible_516_15K = self.driver.find_element(By.ID, "option-476-deductible-516")

        return self

    def select_Netguard_Plus_option_limits_deductibles(self):

        # Select Limit and Deductible
        # Proceed to Next Page
        Coverage_Options.Page_Elements(self).select_deselect_all.click()
        #Coverage_Options.Netguard_Plus_options_limits_deductibles(self).option_222_limit_1169_1MM.click()
        #Coverage_Options.Netguard_Plus_options_limits_deductibles(self).option_222_deductible_512_2_pt5_K.click()
        Coverage_Options.Page_Elements(self).first_dollar_defense.click()
        Coverage_Options.Page_Elements(self).proceed_to_quote.click()

    def select_Netguard_Plus_Additional_Claims_Expenses_option_limits_deductibles(self):

        # Select Limit and Deductible
        # Proceed to Next Page
        #Coverage_Options.Page_Elements(self).select_deselect_all.click()
        Coverage_Options.Netguard_Plus_Additional_Claims_Expenses_options_limits_deductibles(self).option_476_limit_2125_1MM.click()
        Coverage_Options.Netguard_Plus_Additional_Claims_Expenses_options_limits_deductibles(self).option_476_deductible_512_2_pt5_K.click()
        #Coverage_Options.Page_Elements(self).first_dollar_defense.click()
        Coverage_Options.Page_Elements(self).proceed_to_quote.click()
