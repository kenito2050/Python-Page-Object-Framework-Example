from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):


        # $1M Medefense™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_820_limit_3137 = self.driver.find_element(By.ID, "option-820-limit-3137")

        # Deductibles
        # $0
        self.option_820_deductible_1278 = self.driver.find_element(By.ID, "option-820-deductible-1278")


        # $1M Cyber Liability Only - No PCI

        # Limits
        # 1MM/1MM
        self.option_821_limit_3140 = self.driver.find_element(By.ID, "option-821-limit-3140")

        # Deductibles
        # $0/$2,500
        self.option_821_deductible_1281 = self.driver.find_element(By.ID, "option-821-deductible-1281")


        # $2M Cyber Liability Only - No PCI

        # Limits
        # 2MM/2MM
        self.option_830_limit_3146 = self.driver.find_element(By.ID, "option-830-limit-3146")

        # Deductibles
        # $0/$2,500
        self.option_830_deductible_1281 = self.driver.find_element(By.ID, "option-830-deductible-1281")


        # $3M Cyber Liability Only - No PCI

        # Limits
        # 3MM/3MM
        self.option_832_limit_3148 = self.driver.find_element(By.ID, "option-832-limit-3148")

        # Deductibles
        # $0/$0/$2,500
        self.option_832_deductible_1281 = self.driver.find_element(By.ID, "option-832-deductible-1281")


        # $1M Cyber Liability and Medefense™ Plus - No PCI

        # Limits
        # 1MM/1MM
        self.option_822_limit_3141 = self.driver.find_element(By.ID, "option-822-limit-3141")

        # Deductibles
        # $0/$2,500
        self.option_822_deductible_1282 = self.driver.find_element(By.ID, "option-822-deductible-1282")

        # $2M Cyber Liability and Medefense™ Plus - No PCI

        # Limits
        # 2MM/2MM
        self.option_831_limit_3147 = self.driver.find_element(By.ID, "option-831-limit-3147")

        # Deductibles
        # $0/$0/$2,500
        self.option_831_deductible_1282 = self.driver.find_element(By.ID, "option-831-deductible-1282")

        # $3M Cyber Liability and Medefense™ Plus - No PCI

        # Limits
        # 3MM/3MM
        self.option_833_limit_3149 = self.driver.find_element(By.ID, "option-833-limit-3149")

        # Deductibles
        # $0/$0/$2,500
        self.option_833_deductible_1282 = self.driver.find_element(By.ID, "option-833-deductible-1282")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def select_1M_Medefense_Plus_Only_1MM_1MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_820_limit_3137.click()
        No_PCI_Coverage_Options.PageElements(self).option_820_deductible_1278.click()

    def select_1M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_821_limit_3140.click()
        No_PCI_Coverage_Options.PageElements(self).option_821_deductible_1281.click()

    def select_2M_Cyber_Liability_Only_No_PCI_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_830_limit_3146.click()
        No_PCI_Coverage_Options.PageElements(self).option_830_deductible_1281.click()

    def select_3M_Cyber_Liability_Only_No_PCI_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_832_limit_3148.click()
        No_PCI_Coverage_Options.PageElements(self).option_832_deductible_1281.click()

    def select_1M_Cyber_Liability_and_Medefense_Plus_No_PCI_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_822_limit_3141.click()
        No_PCI_Coverage_Options.PageElements(self).option_822_deductible_1282.click()

    def select_2M_Cyber_Liability_and_Medefense_Plus_No_PCI_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_831_limit_3147.click()
        No_PCI_Coverage_Options.PageElements(self).option_831_deductible_1282.click()

    def select_3M_Cyber_Liability_and_Medefense_Plus_No_PCI_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_833_limit_3149.click()
        No_PCI_Coverage_Options.PageElements(self).option_833_deductible_1282.click()

    def select_all_deselect_all(self):
        No_PCI_Coverage_Options.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        No_PCI_Coverage_Options.PageElements(self).return_to_admin_interface.click()