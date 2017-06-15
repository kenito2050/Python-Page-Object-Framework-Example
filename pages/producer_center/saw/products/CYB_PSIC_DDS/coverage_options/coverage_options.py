from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PCI_PageElements(self):

        # Regulatory Proceedings Only Enhanced

        # Limits
        # 250K / 250K
        self.option_174_limit_491 = self.driver.find_element(By.ID, "option-174-limit-491")

        # 500K / 500K
        self.option_174_limit_490 = self.driver.find_element(By.ID, "option-174-limit-490")

        # 1MM / 1MM
        self.option_174_limit_489 = self.driver.find_element(By.ID, "option-174-limit-489")

        # Deductibles
        # $1,000
        self.option_174_deductible_134 = self.driver.find_element(By.ID, "option-174-deductible-134")

        # Network Security & Privacy Only Enhanced

        # Limits
        # 250K / 250K
        self.option_176_limit_1000 = self.driver.find_element(By.ID, "option-176-limit-1000")

        # 500K / 500K
        self.option_176_limit_998 = self.driver.find_element(By.ID, "option-176-limit-998")

        # 1MM / 1MM
        self.option_176_limit_996 = self.driver.find_element(By.ID, "option-176-limit-996")

        # Deductibles
        # $0
        self.option_176_deductible_411 = self.driver.find_element(By.ID, "option-176-deductible-411")


        # Regulatory Proceedings and Network Security & Privacy Combined Enhanced

        # Limits
        # 250K / 250K
        self.option_175_limit_1001 = self.driver.find_element(By.ID, "option-175-limit-1001")

        # 500K / 500K
        self.option_175_limit_999 = self.driver.find_element(By.ID, "option-175-limit-999")

        # 1MM / 1MM
        self.option_175_limit_997 = self.driver.find_element(By.ID, "option-175-limit-997")

        # Deductibles
        # $0 / $1,000
        self.option_175_deductible_412 = self.driver.find_element(By.ID, "option-175-deductible-412")

        return self

    # saw_CC.select_Regulatory_Proceedings_Only_Enhanced()
    # saw_CC.select_Network_Security_Privacy_Only_Enhanced()
    # saw_CC.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced()

    def select_Regulatory_Proceedings_Only_Enhanced_250K_limit(self):

        Coverage_Options.PCI_PageElements(self).option_174_limit_491.click()
        Coverage_Options.PCI_PageElements(self).option_174_deductible_134.click()

    def select_Regulatory_Proceedings_Only_Enhanced_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_174_limit_490.click()
        Coverage_Options.PCI_PageElements(self).option_174_deductible_134.click()

    def select_Regulatory_Proceedings_Only_Enhanced_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_174_limit_489.click()
        Coverage_Options.PCI_PageElements(self).option_174_deductible_134.click()

    def select_Network_Security_Privacy_Only_Enhanced_250K_limit(self):

        Coverage_Options.PCI_PageElements(self).option_176_limit_1000.click()
        Coverage_Options.PCI_PageElements(self).option_176_deductible_411.click()

    def select_Network_Security_Privacy_Only_Enhanced_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_176_limit_998.click()
        Coverage_Options.PCI_PageElements(self).option_176_deductible_411.click()

    def select_Network_Security_Privacy_Only_Enhanced_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_176_limit_996.click()
        Coverage_Options.PCI_PageElements(self).option_176_deductible_411.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_250K(self):
        Coverage_Options.PCI_PageElements(self).option_175_limit_1001.click()
        Coverage_Options.PCI_PageElements(self).option_175_deductible_412.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_500K(self):
        Coverage_Options.PCI_PageElements(self).option_175_limit_999.click()
        Coverage_Options.PCI_PageElements(self).option_175_deductible_412.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced_1MM(self):
        Coverage_Options.PCI_PageElements(self).option_175_limit_997.click()
        Coverage_Options.PCI_PageElements(self).option_175_deductible_412.click()


    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()