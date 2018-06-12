from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Property Manager’s E&O with NetGuard™ Plus and Tenant Discrimination
        # Limits

        # $1MM/1MM
        self.option_989_limit_3772 = self.driver.find_element(By.ID, "option-989-limit-3772")

        # Deductibles

        # $2,500
        self.option_989_deductible_1490 = self.driver.find_element(By.ID, "option-989-deductible-1490")


        # First Dollar Defense
        self.first_dollar_defense = self.driver.find_element(By.ID, "product-form-952")

        # Additional Claim Expenses Limit (DOL)
        self.additional_claim_expenses_limit = self.driver.find_element(By.ID, "product-form-953")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH, "//*[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")


        return self

    def select_deselect_all(self):
        # Property Manager’s E&O with NetGuard™ Plus and Tenant Discrimination
        # Coverage_Options.PageElements(self).option_989_limit_3772.click()
        # Coverage_Options.PageElements(self).option_989_deductible_1490.click()
        # First Dollar Defense
        Coverage_Options.PageElements(self).first_dollar_defense.click()
        Coverage_Options.PageElements(self).additional_claim_expenses_limit.click()

    # def select_all_deselect_all(self):
    #     Coverage_Options.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        Coverage_Options.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        Coverage_Options.PageElements(self).return_to_admin_interface.click()