from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options_After_Sep_6_2017():

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

        # $1M Cyber Liability Only - No PCI

        # Limits
        # 1MM/1MM
        self.option_846_limit_3153 = self.driver.find_element(By.ID, "option-846-limit-3153")

        # Deductibles
        # $0/$2,500
        self.option_846_deductible_1290 = self.driver.find_element(By.ID, "option-846-deductible-1290")


        # $2M Cyber Liability Only - No PCI

        # Limits
        # 2MM/2MM
        self.option_840_limit_3157 = self.driver.find_element(By.ID, "option-840-limit-3157")

        # Deductibles
        # $0/$2,500
        self.option_840_deductible_1290 = self.driver.find_element(By.ID, "option-840-deductible-1290")


        # $3M Cyber Liability Only - No PCI

        # Limits
        # 3MM/3MM
        self.option_838_limit_3159 = self.driver.find_element(By.ID, "option-838-limit-3159")

        # Deductibles
        # $0/$0/$2,500
        self.option_838_deductible_1290 = self.driver.find_element(By.ID, "option-838-deductible-1290")


        # $1M Cyber Liability and Medefense™ Plus - No PCI

        # Limits
        # 1MM/1MM
        self.option_845_limit_3155 = self.driver.find_element(By.ID, "option-845-limit-3155")

        # Deductibles
        # $0/$2,500
        self.option_845_deductible_1291 = self.driver.find_element(By.ID, "option-845-deductible-1291")

        # $2M Cyber Liability and Medefense™ Plus - No PCI

        # Limits
        # 2MM/2MM
        self.option_839_limit_3161 = self.driver.find_element(By.ID, "option-839-limit-3161")

        # Deductibles
        # $0/$0/$2,500
        self.option_839_deductible_1291 = self.driver.find_element(By.ID, "option-839-deductible-1291")

        # $3M Cyber Liability and Medefense™ Plus - No PCI

        # Limits
        # 3MM/3MM
        self.option_837_limit_3163 = self.driver.find_element(By.ID, "option-837-limit-3163")

        # Deductibles
        # $0/$0/$2,500
        self.option_837_deductible_1291 = self.driver.find_element(By.ID, "option-837-deductible-1291")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def select_1M_Medefense_Plus_Only_1MM_1MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_847_limit_3151.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_847_deductible_1287.click()

    def select_1M_Cyber_Liability_Only_No_PCI_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_846_limit_3153.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_846_deductible_1290.click()

    def select_2M_Cyber_Liability_Only_No_PCI_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_840_limit_3157.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_840_deductible_1290.click()

    def select_3M_Cyber_Liability_Only_No_PCI_1MM_1MM_limit_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_838_limit_3159.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_838_deductible_1290.click()

    def select_1M_Cyber_Liability_and_Medefense_Plus_No_PCI_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_845_limit_3155.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_845_deductible_1291.click()

    def select_2M_Cyber_Liability_and_Medefense_Plus_No_PCI_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_839_limit_3161.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_839_deductible_1291.click()

    def select_3M_Cyber_Liability_and_Medefense_Plus_No_PCI_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_837_limit_3163.click()
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_837_deductible_1291.click()

    def select_all_deselect_all(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        No_PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).return_to_admin_interface.click()