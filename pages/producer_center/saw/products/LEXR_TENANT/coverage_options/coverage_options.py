from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Limits
        # $250K/$250K
        self.option_518_limit_887 = self.driver.find_element(By.ID, "option-518-limit-887")

        # $500K/$500K
        self.option_518_limit_580 = self.driver.find_element(By.ID, "option-518-limit-580")

        # $1MM/1MM
        self.option_518_limit_579 = self.driver.find_element(By.ID, "option-518-limit-579")

        # Deductibles

        # $5,000
        self.option_518_deductible_177 = self.driver.find_element(By.ID, "option-518-deductible-177")



        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self


    def select_Tenant_Discrimination_Legal_Expense_Loss_Reimbursement_Insurance_250K_limit_5K_Deduct(self):
        Coverage_Options.PageElements(self).option_518_limit_887.click()
        Coverage_Options.PageElements(self).option_518_deductible_177.click()

    def select_Tenant_Discrimination_Legal_Expense_Loss_Reimbursement_Insurance_500K_limit_5K_Deduct(self):
        Coverage_Options.PageElements(self).option_518_limit_580.click()
        Coverage_Options.PageElements(self).option_518_deductible_177.click()

    def select_Tenant_Discrimination_Legal_Expense_Loss_Reimbursement_Insurance_1MM_limit_5K_Deduct(self):
        Coverage_Options.PageElements(self).option_518_limit_579.click()
        Coverage_Options.PageElements(self).option_518_deductible_177.click()


    def select_all_deselect_all(self):
        Coverage_Options.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        Coverage_Options.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        Coverage_Options.PageElements(self).return_to_admin_interface.click()