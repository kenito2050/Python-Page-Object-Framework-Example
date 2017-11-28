from selenium.webdriver.common.by import By

class California_HNOA_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        # Long Term Care PL/GL

        # Limits
        # $1MM/$3MM
        self.option_902_limit_180 = self.driver.find_element(By.ID, "option-902-limit-180")

        # Deductibles
        # $1,000
        self.option_902_deductible_49 = self.driver.find_element(By.ID, "option-902-deductible-49")

        # Hired Auto and Non-Owned Auto Liability ($100K/$300K Limits)
        self.ltc_hnoa_endt_selected = self.driver.find_element(By.ID, "ltc_hnoa_endt_selected")

        return self

    def select_LTC_Include_HNOA_1MM_3MM_Limit_1K_Deduct(self):
        California_HNOA_Coverage_Options.PageElements(self).option_902_limit_180.click()
        California_HNOA_Coverage_Options.PageElements(self).option_902_deductible_49.click()
        California_HNOA_Coverage_Options.PageElements(self).ltc_hnoa_endt_selected.click()

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