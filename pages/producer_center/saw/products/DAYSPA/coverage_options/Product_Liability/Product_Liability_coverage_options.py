from selenium.webdriver.common.by import By

class Product_Liability_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # PL & GL Claims Made

        # Limits

        # 1MM/3MM
        self.option_900_limit_3516 = self.driver.find_element(By.ID, "option-900-limit-3516")

        # $1MM/$3MM with Products/Completed Operations Liability
        self.option_900_limit_3517 = self.driver.find_element(By.ID, "option-900-limit-3517")

        # Deductibles
        # $2,500
        self.option_900_deductible_1401 = self.driver.find_element(By.ID, "option-900-deductible-1401")

        # PL Claims Made & GL Occurrence

        # Limits

        # $1MM/$3MM
        self.option_901_limit_3516 = self.driver.find_element(By.ID, "option-901-limit-3516")

        # Deductibles

        # $2,500
        self.option_901_deductible_1401 = self.driver.find_element(By.ID, "option-901-deductible-1401")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self


    def select_PL_GL_Claims_Made_1MM_3MM_limit_2pt5K_Deduct(self):
        Product_Liability_Coverage_Options.PageElements(self).option_900_limit_3516.click()
        Product_Liability_Coverage_Options.PageElements(self).option_900_deductible_1401.click()

    def select_PL_GL_Claims_Made_1MM_3MM_with_Products_Completed_Operations_Liability_limit_2pt5K_Deduct(self):
        Product_Liability_Coverage_Options.PageElements(self).option_900_limit_3517.click()
        Product_Liability_Coverage_Options.PageElements(self).option_900_deductible_1401.click()

    def select_PL_Claims_Made_GL_Occurrence_1MM_3MM_limit_2pt5K_Deduct(self):
        Product_Liability_Coverage_Options.PageElements(self).option_901_limit_3516.click()
        Product_Liability_Coverage_Options.PageElements(self).option_901_deductible_1401.click()

    def select_all_deselect_all(self):
        Product_Liability_Coverage_Options.PageElements(self).select_deselect_all.click()

    def proceed_to_quote(self):
        Product_Liability_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        Product_Liability_Coverage_Options.PageElements(self).return_to_admin_interface.click()