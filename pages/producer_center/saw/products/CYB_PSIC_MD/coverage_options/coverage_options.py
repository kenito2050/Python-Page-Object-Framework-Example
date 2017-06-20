from selenium.webdriver.common.by import By

class Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PCI_PageElements(self):

        # Regulatory Proceedings Only

        # Limits
        # 250K / 250K
        self.option_171_limit_482 = self.driver.find_element(By.ID, "option-171-limit-482")

        # 500K / 500K
        self.option_171_limit_481 = self.driver.find_element(By.ID, "option-171-limit-481")

        # 1MM / 1MM
        self.option_171_limit_480 = self.driver.find_element(By.ID, "option-171-limit-480")

        # Deductibles
        # $1,000
        self.option_171_deductible_131 = self.driver.find_element(By.ID, "option-171-deductible-131")

        # Network Security & Privacy Only

        # Limits
        # 250K / 250K
        self.option_173_limit_1003 = self.driver.find_element(By.ID, "option-173-limit-1003")

        # 500K / 500K
        self.option_173_limit_1005 = self.driver.find_element(By.ID, "option-173-limit-1005")

        # 1MM / 1MM
        self.option_173_limit_1007 = self.driver.find_element(By.ID, "option-173-limit-1007")

        # Deductibles
        # $0
        self.option_173_deductible_414 = self.driver.find_element(By.ID, "option-173-deductible-414")


        # Regulatory Proceedings and Network Security & Privacy Combined

        # Limits
        # 250K / 250K
        self.option_172_limit_1002 = self.driver.find_element(By.ID, "option-172-limit-1002")

        # 500K / 500K
        self.option_172_limit_1004 = self.driver.find_element(By.ID, "option-172-limit-1004")

        # 1MM / 1MM
        self.option_172_limit_1006 = self.driver.find_element(By.ID, "option-172-limit-1006")

        # Deductibles
        # $0 / $0
        self.option_172_deductible_413 = self.driver.find_element(By.ID, "option-172-deductible-413")

        return self

    # saw_CC.select_Regulatory_Proceedings_Only_Enhanced()
    # saw_CC.select_Network_Security_Privacy_Only_Enhanced()
    # saw_CC.select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_Enhanced()

    def select_Regulatory_Proceedings_Only_250K_limit(self):

        Coverage_Options.PCI_PageElements(self).option_171_limit_482.click()
        Coverage_Options.PCI_PageElements(self).option_171_deductible_131.click()

    def select_Regulatory_Proceedings_Only_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_171_limit_481.click()
        Coverage_Options.PCI_PageElements(self).option_171_deductible_131.click()

    def select_Regulatory_Proceedings_Only_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_171_limit_480.click()
        Coverage_Options.PCI_PageElements(self).option_171_deductible_131.click()

    def select_Network_Security_Privacy_Only_250K_limit(self):

        Coverage_Options.PCI_PageElements(self).option_173_limit_1003.click()
        Coverage_Options.PCI_PageElements(self).option_173_deductible_414.click()

    def select_Network_Security_Privacy_Only_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_173_limit_1005.click()
        Coverage_Options.PCI_PageElements(self).option_173_deductible_414.click()

    def select_Network_Security_Privacy_Only_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_173_limit_1007.click()
        Coverage_Options.PCI_PageElements(self).option_173_deductible_414.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_250K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_172_limit_1002.click()
        Coverage_Options.PCI_PageElements(self).option_172_deductible_413.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_500K_limit(self):
        Coverage_Options.PCI_PageElements(self).option_172_limit_1004.click()
        Coverage_Options.PCI_PageElements(self).option_172_deductible_413.click()

    def select_Regulatory_Proceedings_and_Network_Security_Privacy_Combined_1MM_limit(self):
        Coverage_Options.PCI_PageElements(self).option_172_limit_1006.click()
        Coverage_Options.PCI_PageElements(self).option_172_deductible_413.click()

    def select_all_deselect_all(self):
        select_deselect_all = self.driver.find_element(By.ID, "select-deselect-all")
        select_deselect_all.click()

    def proceed_to_quote(self):
        proceed_to_quote = self.driver.find_element(By.XPATH, "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")
        proceed_to_quote.click()

    def click_return_to_Admin_Interface(self):
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()