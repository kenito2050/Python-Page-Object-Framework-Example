from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Miscellaneous E&O for Healthcare Professionals (Expert Witness)

        # Limits

        # 1MM/1MM
        self.option_68_limit_357 = self.driver.find_element(By.ID, "option-68-limit-357")

        # 1MM/3MM
        self.option_68_limit_358 = self.driver.find_element(By.ID, "option-68-limit-358")

        # Deductibles
        # $2,500
        self.option_68_deductible_92 = self.driver.find_element(By.ID, "option-68-deductible-92")

        # Additional Coverage

        # First Dollar Defense
        self.first_dollar_defense = self.driver.find_element(By.ID, "product-form-952")

        # Additional Claim Expenses Limit (DOL)
        self.additional_claim_expenses_limit_claim_expenses_limit = self.driver.find_element(By.ID, "product-form-953")


        # Select / Deselect All
        # Not Working
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
        Coverage_Options.Page_Elements(self).option_68_limit_357.click()
        Coverage_Options.Page_Elements(self).option_68_limit_358.click()
        Coverage_Options.Page_Elements(self).option_68_deductible_92.click()
        Coverage_Options.Page_Elements(self).first_dollar_defense.click()
        Coverage_Options.Page_Elements(self).additional_claim_expenses_limit_claim_expenses_limit.click()


        # NOT: This method is not callable
        # Proceed to Quote methoc placed in the Methods that check the Options Check Boxes
    def click_proceed_to_quote(self):
        Coverage_Options.Page_Elements(self).proceed_to_quote.click()
