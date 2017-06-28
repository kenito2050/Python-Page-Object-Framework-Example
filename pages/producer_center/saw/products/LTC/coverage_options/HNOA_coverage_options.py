from selenium.webdriver.common.by import By

class HNOA_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Long Term Care PL/GL

        ##### NOTE: All States Except Florida will display ONLY 1MM / 3MM Limit

        # Limits
        # $50K/$200K
        #self.option_0_limit_722 = self.driver.find_element(By.ID, "option-0-limit-722")

        # $100K/$300K
        #self.option_0_limit_740 = self.driver.find_element(By.ID, "option-0-limit-740")

        # $250K/$500K
        #self.option_0_limit_227 = self.driver.find_element(By.ID, "option-0-limit-227")

        # $500K/$1MM
        #self.option_0_limit_226 = self.driver.find_element(By.ID, "option-0-limit-226")

        # $1MM/$1MM
        #self.option_0_limit_178 = self.driver.find_element(By.ID, "option-0-limit-178")

        # $1MM/$2MM
        #self.option_0_limit_179 = self.driver.find_element(By.ID, "option-0-limit-179")

        # $1MM/$3MM
        self.option_0_limit_180 = self.driver.find_element(By.ID, "option-0-limit-180")

        # Deductibles
        # $1,000
        self.option_0_deductible_49 = self.driver.find_element(By.ID, "option-0-deductible-49")

        # Hired Auto and Non-Owned Auto Liability ($100K/$300K Limits)
        self.ltc_hnoa_endt_selected = self.driver.find_element(By.ID, "ltc_hnoa_endt_selected")

        return self

        ##### NOTE: Deductible is selected by default

        # select_LTC_Include_HNOA_50K_200K_Limit()
        # select_LTC_Include_HNOA_100K_300K_Limit()
        # select_LTC_Include_HNOA_250K_500K_Limit()
        # select_LTC_Include_HNOA_500K_1MM_Limit()
        # select_LTC_Include_HNOA_1MM_1MM_Limit()
        # select_LTC_Include_HNOA_1MM_2MM_Limit()
        # select_LTC_Include_HNOA_1MM_3MM_Limit()

    ## These options commented out 6-28-17

    # def select_LTC_Include_HNOA_50K_200K_Limit(self):
    #     HNOA_Coverage_Options.PageElements(self).option_0_limit_722.click()
    #     # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
    #     HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()
    #
    # def select_LTC_Include_HNOA_100K_300K_Limit(self):
    #     HNOA_Coverage_Options.PageElements(self).option_0_limit_740.click()
    #     # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
    #     HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()
    #
    # def select_LTC_Include_HNOA_250K_500K_Limit(self):
    #     HNOA_Coverage_Options.PageElements(self).option_0_limit_227.click()
    #     # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
    #     HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()
    #
    # def select_LTC_Include_HNOA_500K_1MM_Limit(self):
    #     HNOA_Coverage_Options.PageElements(self).option_0_limit_226.click()
    #     # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
    #     HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()
    #
    # def select_LTC_Include_HNOA_1MM_1MM_Limit(self):
    #     HNOA_Coverage_Options.PageElements(self).option_0_limit_178.click()
    #     # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
    #     HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()
    #
    # def select_LTC_Include_HNOA_1MM_2MM_Limit(self):
    #     HNOA_Coverage_Options.PageElements(self).option_0_limit_179.click()
    #     # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
    #     HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()

    def select_LTC_Include_HNOA_1MM_3MM_Limit(self):
        # HNOA_Coverage_Options.PageElements(self).option_0_limit_180.click()
        # HNOA_Coverage_Options.PageElements(self).option_0_deductible_49.click()
        HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()

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