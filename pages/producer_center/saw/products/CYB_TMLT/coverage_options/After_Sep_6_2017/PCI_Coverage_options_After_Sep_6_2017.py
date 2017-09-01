from selenium.webdriver.common.by import By

class PCI_Coverage_Options_After_Sep_6_2017():

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


        # $1M Cyber Liability Only

        # Limits
        # 1MM/1MM
        self.option_818_limit_3138 = self.driver.find_element(By.ID, "option-818-limit-3138")

        # Deductibles
        # $0/$2,500
        self.option_818_deductible_1279 = self.driver.find_element(By.ID, "option-818-deductible-1279")


        # $2M Cyber Liability Only

        # Limits
        # 2MM/2MM
        self.option_824_limit_3142 = self.driver.find_element(By.ID, "option-824-limit-3142")

        # Deductibles
        # $0/$2,500
        self.option_824_deductible_1279 = self.driver.find_element(By.ID, "option-824-deductible-1279")


        # $3M Cyber Liability Only

        # Limits
        # 3MM/3MM
        self.option_827_limit_3144 = self.driver.find_element(By.ID, "option-827-limit-3144")

        # Deductibles
        # $0/$0/$2,500
        self.option_827_deductible_1279 = self.driver.find_element(By.ID, "option-827-deductible-1279")


        # $1M Cyber Liability and Medefense™ Plus

        # Limits
        # 1MM/1MM
        self.option_819_limit_3139 = self.driver.find_element(By.ID, "option-819-limit-3139")

        # Deductibles
        # $0/$2,500
        self.option_819_deductible_1280 = self.driver.find_element(By.ID, "option-819-deductible-1280")

        # $2M Cyber Liability and Medefense™ Plus

        # Limits
        # 2MM/2MM
        self.option_825_limit_3143 = self.driver.find_element(By.ID, "option-825-limit-3143")

        # Deductibles
        # $0/$0/$2,500
        self.option_825_deductible_1280 = self.driver.find_element(By.ID, "option-825-deductible-1280")

        # $3M Cyber Liability and Medefense™ Plus

        # Limits
        # 3MM/3MM
        self.option_828_limit_3145 = self.driver.find_element(By.ID, "option-828-limit-3145")

        # Deductibles
        # $0/$0/$2,500
        self.option_828_deductible_1280 = self.driver.find_element(By.ID, "option-828-deductible-1280")


        # Select Deselect All
        self.select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        # Return to Admin Interface
        self.return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def select_1M_Medefense_Plus_Only_1MM_1MM_limit_0_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_820_limit_3137.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_820_deductible_1278.click()

    def select_1M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_818_limit_3138.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_818_deductible_1279.click()

    def select_2M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_824_limit_3142.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_824_deductible_1279.click()

    def select_3M_Cyber_Liability_Only_1MM_1MM_limit_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_827_limit_3144.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_827_deductible_1279.click()

    def select_1M_Cyber_Liability_and_Medefense_Plus_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_819_limit_3139.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_819_deductible_1280.click()

    def select_2M_Cyber_Liability_and_Medefense_Plus_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_825_limit_3143.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_825_deductible_1280.click()

    def select_3M_Cyber_Liability_and_Medefense_Plus_1MM_1MM_limit_0_0_2pt5K_Deduct(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_828_limit_3145.click()
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).option_828_deductible_1280.click()

    def select_all_deselect_all(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).select_deselect_all.click()

    def click_proceed_to_quote(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        PCI_Coverage_Options_After_Sep_6_2017.PageElements(self).return_to_admin_interface.click()