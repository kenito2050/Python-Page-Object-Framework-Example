from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):


        # CyberRisk™ with Cyber Crime Only

        # Limits
        # 1MM/1MM
        self.option_746_limit_2912 = self.driver.find_element(By.ID, "option-746-limit-2912")

        # Deductibles
        # $50,000
        self.option_746_deductible_1227 = self.driver.find_element(By.ID, "option-746-deductible-1227")

        # CyberRisk™ Only with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_747_limit_2915 = self.driver.find_element(By.ID, "option-747-limit-2915")

        # Deductibles
        # $50,000
        self.option_747_deductible_1227 = self.driver.find_element(By.ID, "option-747-deductible-1227")

        # Medefense™ Plus Only

        # Limits
        # 1MM/2MM
        self.option_748_limit_2922 = self.driver.find_element(By.ID, "option-748-limit-2922")

        # Deductibles
        # $25,000
        self.option_748_deductible_1228 = self.driver.find_element(By.ID, "option-748-deductible-1228")

        # Medefense™ Plus with Peer Review Proceeding Sublimit

        # Limits
        # 1MM/5MM
        self.option_749_limit_2927 = self.driver.find_element(By.ID, "option-749-limit-2927")

        # Deductibles
        # $25,000
        self.option_749_deductible_1229 = self.driver.find_element(By.ID, "option-749-deductible-1229")

        # Medefense™ Plus and CyberRisk™ with Cyber Crime Combined Shared Limits

        # Limits
        # 1MM/1MM
        self.option_750_limit_2928 = self.driver.find_element(By.ID, "option-750-limit-2928")

        # Deductibles
        # $25K/$50K
        self.option_750_deductible_1230 = self.driver.find_element(By.ID, "option-750-deductible-1230")

        # Medefense™ Plus and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_751_limit_2931 = self.driver.find_element(By.ID, "option-751-limit-2931")

        # Deductibles
        # $25K/$50K
        self.option_751_deductible_1230 = self.driver.find_element(By.ID, "option-751-deductible-1230")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_752_limit_2937 = self.driver.find_element(By.ID, "option-752-limit-2937")

        # Deductibles
        # $25K/$50K
        self.option_752_deductible_1230 = self.driver.find_element(By.ID, "option-752-deductible-1230")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_753_limit_2945 = self.driver.find_element(By.ID, "option-753-limit-2945")

        # Deductibles
        # $25K/$50K
        self.option_753_deductible_1230 = self.driver.find_element(By.ID, "option-753-deductible-1230")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_754_limit_2948 = self.driver.find_element(By.ID, "option-754-limit-2948")

        # Deductibles
        # $25K/$50K
        self.option_754_deductible_1231 = self.driver.find_element(By.ID, "option-754-deductible-1231")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_755_limit_2951 = self.driver.find_element(By.ID, "option-755-limit-2951")

        # Deductibles
        # $25K/$50K
        self.option_755_deductible_1231 = self.driver.find_element(By.ID, "option-755-deductible-1231")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Separate Limits with Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_756_limit_2958 = self.driver.find_element(By.ID, "option-756-limit-2958")

        # Deductibles
        # $25K/$50K
        self.option_756_deductible_1231 = self.driver.find_element(By.ID, "option-756-deductible-1231")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_757_limit_2965 = self.driver.find_element(By.ID, "option-757-limit-2965")

        # Deductibles
        # $25K/$50K
        self.option_757_deductible_1231 = self.driver.find_element(By.ID, "option-757-deductible-1231")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        return self

    # select_CyberRisk_Only_with_Cyber_Crime_Only()
    # select_CyberRisk_Only_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()
    # select_Medefense_Plus_Only()
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit()
    # select_Medefense_Plus_and_CyberRisk_with_Cyber_Crime_Combined_Shared_Limits()
    # select_Medefense_Plus_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()
    # select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Cyber_Crime()
    # select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime()
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()

    def select_CyberRisk_Only_with_Cyber_Crime_Only(self):
        PCI_Coverage_Options.PageElements(self).option_746_limit_2912.click()
        PCI_Coverage_Options.PageElements(self).option_746_deductible_1227.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_CyberRisk_Only_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_747_limit_2915.click()
        PCI_Coverage_Options.PageElements(self).option_747_deductible_1227.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_Only(self):
        PCI_Coverage_Options.PageElements(self).option_748_limit_2922.click()
        PCI_Coverage_Options.PageElements(self).option_748_deductible_1228.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit(self):
        PCI_Coverage_Options.PageElements(self).option_749_limit_2927.click()
        PCI_Coverage_Options.PageElements(self).option_749_deductible_1229.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_with_Cyber_Crime_Combined_Shared_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_750_limit_2928.click()
        PCI_Coverage_Options.PageElements(self).option_750_deductible_1230.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_751_limit_2931.click()
        PCI_Coverage_Options.PageElements(self).option_751_deductible_1230.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_752_limit_2937.click()
        PCI_Coverage_Options.PageElements(self).option_752_deductible_1230.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_753_limit_2945.click()
        PCI_Coverage_Options.PageElements(self).option_753_deductible_1230.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_755_limit_2951.click()
        PCI_Coverage_Options.PageElements(self).option_755_deductible_1231.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_756_limit_2958.click()
        PCI_Coverage_Options.PageElements(self).option_756_deductible_1231.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_757_limit_2965.click()
        PCI_Coverage_Options.PageElements(self).option_757_deductible_1231.click()
        PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()