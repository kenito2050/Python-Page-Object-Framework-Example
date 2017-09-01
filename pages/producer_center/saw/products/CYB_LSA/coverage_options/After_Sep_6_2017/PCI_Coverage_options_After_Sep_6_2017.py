from selenium.webdriver.common.by import By

class PCI_Coverage_Options_After_Sep_6_2017():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):


        # $1M Medefense™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_847_limit_3151 = self.driver.find_element(By.ID, "option-847-limit-3151")

        # Deductibles
        # $0
        self.option_847_deductible_1287 = self.driver.find_element(By.ID, "option-847-deductible-1287")


        # $1M Cyber Liability Only

        # Limits
        # 1MM/1MM
        self.option_849_limit_3152 = self.driver.find_element(By.ID, "option-849-limit-3152")

        # Deductibles
        # $0/$2,500
        self.option_849_deductible_1288 = self.driver.find_element(By.ID, "option-849-deductible-1288")


        # $2M Cyber Liability Only

        # Limits
        # 2MM/2MM
        self.option_844_limit_3156 = self.driver.find_element(By.ID, "option-844-limit-3156")

        # Deductibles
        # $0/$2,500
        self.option_844_deductible_1288 = self.driver.find_element(By.ID, "option-844-deductible-1288")


        # $3M Cyber Liability Only

        # Limits
        # 3MM/3MM
        self.option_842_limit_3158 = self.driver.find_element(By.ID, "option-842-limit-3158")

        # Deductibles
        # $0/$0/$2,500
        self.option_842_deductible_1288 = self.driver.find_element(By.ID, "option-842-deductible-1288")


        # $1M Cyber Liability and Medefense™ Plus

        # Limits
        # 1MM/1MM
        self.option_848_limit_3154 = self.driver.find_element(By.ID, "option-848-limit-3154")

        # Deductibles
        # $0/$2,500
        self.option_848_deductible_1289 = self.driver.find_element(By.ID, "option-848-deductible-1289")

        # $2M Cyber Liability and Medefense™ Plus

        # Limits
        # 2MM/2MM
        self.option_843_limit_3160 = self.driver.find_element(By.ID, "option-843-limit-3160")

        # Deductibles
        # $0/$0/$2,500
        self.option_843_deductible_1289 = self.driver.find_element(By.ID, "option-843-deductible-1289")

        # $3M Cyber Liability and Medefense™ Plus

        # Limits
        # 3MM/3MM
        self.option_841_limit_3162 = self.driver.find_element(By.ID, "option-841-limit-3162")

        # Deductibles
        # $0/$0/$2,500
        self.option_841_deductible_1289 = self.driver.find_element(By.ID, "option-841-deductible-1289")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def select_1M_Medefense_Plus_Only_1MM_1MM_limit_0_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_847_limit_3151.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_847_deductible_1287.click()

    def select_1M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_849_limit_3152.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_849_deductible_1288.click()

    def select_2M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_844_limit_3156.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_844_deductible_1288.click()

    def select_3M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_842_limit_3158.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_842_deductible_1288.click()

    def select_1M_Cyber_Liability_and_Medefense_Plus_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_848_limit_3154.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_848_deductible_1289.click()

    def select_2M_Cyber_Liability_and_Medefense_Plus_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_843_limit_3160.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_843_deductible_1289.click()

    def select_3M_Cyber_Liability_and_Medefense_Plus_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_841_limit_3162.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_841_deductible_1289.click()

    def select_all_deselect_all(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).return_to_admin_interface.click()