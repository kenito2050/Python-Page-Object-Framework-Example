from selenium.webdriver.common.by import By

class Coverage_Options_Revenue_Over_2pt5MM():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # Online Seller Suspension

        # Limits
        # $1MM/1MM
        self.option_904_limit_3534 = self.driver.find_element(By.ID, "option-904-limit-3534")

        # Deductibles

        # None
        self.option_904_deductible_1408 = self.driver.find_element(By.ID, "option-904-deductible-1408")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self


    def select_Online_Seller_Suspension_1MM_limit_0_Deduct(self):
        Coverage_Options_Revenue_Over_2pt5MM.PageElements(self).option_904_limit_3534.click()
        Coverage_Options_Revenue_Over_2pt5MM.PageElements(self).option_904_deductible_1408.click()

    def select_all_deselect_all(self):
        Coverage_Options_Revenue_Over_2pt5MM.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        Coverage_Options_Revenue_Over_2pt5MM.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        Coverage_Options_Revenue_Over_2pt5MM.PageElements(self).return_to_admin_interface.click()