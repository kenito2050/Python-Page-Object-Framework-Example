from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

            # Miscellaneous E&O with NetGuard™ Plus

            # Limits

            # $500K / $500K (with $25K NetGuard™ Plus)
            self.option_967_limit_3690_500K = self.driver.find_element(By.ID, "option-967-limit-3690")

            # $500K / $500K (with $100K NetGuard™ Plus)
            self.option_967_limit_3692_500K = self.driver.find_element(By.ID, "option-967-limit-3692")

            # $1MM / $1MM (with $25K NetGuard™ Plus)
            self.option_967_limit_3691_1MM = self.driver.find_element(By.ID, "option-967-limit-3691")

            # $1MM / $1MM (with $100K NetGuard™ Plus)
            self.option_967_limit_3693_1MM = self.driver.find_element(By.ID, "option-967-limit-3693")

            # $1MM / $2MM (with $25K NetGuard™ Plus)
            self.option_967_limit_3695_1MM = self.driver.find_element(By.ID, "option-967-limit-3695")

            # $1MM / $2MM (with $100K NetGuard™ Plus)
            self.option_967_limit_3696_1MM = self.driver.find_element(By.ID, "option-967-limit-3696")

            # Deductibles

            # $1,000
            self.option_967_deductible_1442_1K = self.driver.find_element(By.ID, "option-967-deductible-1442")

            # $2,500
            self.option_967_deductible_1441_2_pt5_K = self.driver.find_element(By.ID, "option-967-deductible-1441")

            # $5,000
            self.option_967_deductible_1443_5K = self.driver.find_element(By.ID, "option-967-deductible-1443")

            # $10,000
            self.option_967_deductible_1444_10K = self.driver.find_element(By.ID, "option-967-deductible-1444")

            # $15,000
            self.option_967_deductible_1445_15K = self.driver.find_element(By.ID, "option-967-deductible-1445")

            # Miscellaneous E&O with NetGuard™ Plus and Additional Claims Expenses

            # Limits

            # $500K / $500K (with $50K NetGuard™ Plus)
            self.option_968_limit_3698_500K = self.driver.find_element(By.ID, "option-968-limit-3698")

            # $500K / $500K (with $50K NetGuard™ Plus)
            self.option_968_limit_3701_500K = self.driver.find_element(By.ID, "option-968-limit-3701")

            # $1MM / $1MM (with $100K NetGuard™ Plus)
            self.option_968_limit_3700_1MM = self.driver.find_element(By.ID, "option-968-limit-3700")

            # $1MM / $2MM (with $25K NetGuard™ Plus)
            self.option_968_limit_3703_1MM = self.driver.find_element(By.ID, "option-968-limit-3703")

            # $1MM / $2MM (with $100K NetGuard™ Plus)
            self.option_968_limit_3704_1MM = self.driver.find_element(By.ID, "option-968-limit-3704")

            # Deductibles

            # $1,000
            self.option_968_deductible_1442_1K = self.driver.find_element(By.ID, "option-968-deductible-1442")

            # $2,500
            self.option_968_deductible_1441_2_pt5_K = self.driver.find_element(By.ID, "option-968-deductible-1441")

            # $5,000
            self.option_968_deductible_1443_5K = self.driver.find_element(By.ID, "option-968-deductible-1443")

            # $10,000
            self.option_968_deductible_1444_10K = self.driver.find_element(By.ID, "option-968-deductible-1444")

            # $15,000
            self.option_968_deductible_1445_15K = self.driver.find_element(By.ID, "option-968-deductible-1445")


            # Select / Deselect All
            # self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

            # Proceed to Quote
            self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                        "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
            # Return to Admin Interface
            self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

            # Additional Coverage Options

            # First Dollar Defense
            self.first_dollar_defense = self.driver.find_element(By.ID, "product-form-952")


            return self

    def select_deselect_all(self):
        # Miscellaneous E&O with NetGuard™ Plus
        Coverage_Options.Page_Elements(self).option_967_limit_3690_500K.click()
        Coverage_Options.Page_Elements(self).option_967_limit_3692_500K.click()
        Coverage_Options.Page_Elements(self).option_967_limit_3691_1MM.click()
        Coverage_Options.Page_Elements(self).option_967_limit_3693_1MM.click()
        Coverage_Options.Page_Elements(self).option_967_limit_3695_1MM.click()
        Coverage_Options.Page_Elements(self).option_967_limit_3696_1MM.click()
        Coverage_Options.Page_Elements(self).option_967_deductible_1442_1K.click()
        Coverage_Options.Page_Elements(self).option_967_deductible_1441_2_pt5_K.click()
        Coverage_Options.Page_Elements(self).option_967_deductible_1443_5K.click()
        Coverage_Options.Page_Elements(self).option_967_deductible_1444_10K.click()
        Coverage_Options.Page_Elements(self).option_967_deductible_1445_15K.click()
        # Miscellaneous E&O with NetGuard™ Plus and Additional Claims Expenses
        Coverage_Options.Page_Elements(self).option_968_limit_3698_500K.click()
        Coverage_Options.Page_Elements(self).option_968_limit_3701_500K.click()
        Coverage_Options.Page_Elements(self).option_968_limit_3700_1MM.click()
        Coverage_Options.Page_Elements(self).option_968_limit_3703_1MM.click()
        Coverage_Options.Page_Elements(self).option_968_limit_3704_1MM.click()
        Coverage_Options.Page_Elements(self).option_968_deductible_1442_1K.click()
        Coverage_Options.Page_Elements(self).option_968_deductible_1441_2_pt5_K.click()
        Coverage_Options.Page_Elements(self).option_968_deductible_1443_5K.click()
        Coverage_Options.Page_Elements(self).option_968_deductible_1444_10K.click()
        Coverage_Options.Page_Elements(self).option_968_deductible_1445_15K.click()
        # First Dollar Defense
        Coverage_Options.Page_Elements(self).first_dollar_defense.click()


        # NOT: This method is not callable
        # Proceed to Quote methoc placed in the Methods that check the Options Check Boxes
    def click_proceed_to_quote(self):
        Coverage_Options.Page_Elements(self).proceed_to_quote.click()
