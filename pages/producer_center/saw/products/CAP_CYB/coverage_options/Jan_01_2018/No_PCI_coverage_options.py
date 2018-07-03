from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):


        # CyberRisk™ with Cyber Crime Only - No PCI

        # Limits
        # 1MM/1MM
        self.option_758_limit_2969 = self.driver.find_element(By.ID, "option-758-limit-2969")

        # Deductibles
        # $50,000
        self.option_758_deductible_1232 = self.driver.find_element(By.ID, "option-758-deductible-1232")

        # CyberRisk™ Only with Claim Expenses Outside Limits and Cyber Crime - No PCI

        # Limits
        # 1MM/1MM
        self.option_759_limit_2972 = self.driver.find_element(By.ID, "option-759-limit-2972")

        # Deductibles
        # $50,000
        self.option_759_deductible_1232 = self.driver.find_element(By.ID, "option-759-deductible-1232")

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

        # Medefense™ Plus and CyberRisk™ with Cyber Crime Combined Shared Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_760_limit_2975 = self.driver.find_element(By.ID, "option-760-limit-2975")

        # Deductibles
        # $25K/$50K
        self.option_760_deductible_1233 = self.driver.find_element(By.ID, "option-760-deductible-1233")

        # Medefense™ Plus and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime - No PCI

        # Limits
        # 1MM/1MM
        self.option_761_limit_2978 = self.driver.find_element(By.ID, "option-761-limit-2978")

        # Deductibles
        # $25K/$50K
        self.option_761_deductible_1233 = self.driver.find_element(By.ID, "option-761-deductible-1233")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Cyber Crime - No PCI

        # Limits
        # 1MM/5MM
        self.option_762_limit_2984 = self.driver.find_element(By.ID, "option-762-limit-2984")

        # Deductibles
        # $25K/$50K
        self.option_762_deductible_1233 = self.driver.find_element(By.ID, "option-762-deductible-1233")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime - No PCI

        # Limits
        # 1MM/5MM
        self.option_763_limit_2992 = self.driver.find_element(By.ID, "option-763-limit-2992")

        # Deductibles
        # $25K/$50K
        self.option_763_deductible_1233 = self.driver.find_element(By.ID, "option-763-deductible-1233")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Cyber Crime - No PCI

        # Limits
        # 1MM/1MM
        self.option_764_limit_2995 = self.driver.find_element(By.ID, "option-764-limit-2995")

        # Deductibles
        # $25K/$50K
        self.option_764_deductible_1234 = self.driver.find_element(By.ID, "option-764-deductible-1234")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime - No PCI

        # Limits
        # 1MM/1MM
        self.option_765_limit_2998 = self.driver.find_element(By.ID, "option-765-limit-2998")

        # Deductibles
        # $25K/$50K
        self.option_765_deductible_1234 = self.driver.find_element(By.ID, "option-765-deductible-1234")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Separate Limits with Cyber Crime - No PCI

        # Limits
        # 1MM/5MM
        self.option_766_limit_3005 = self.driver.find_element(By.ID, "option-766-limit-3005")

        # Deductibles
        # $25K/$50K
        self.option_766_deductible_1234 = self.driver.find_element(By.ID, "option-766-deductible-1234")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime - No PCI

        # Limits
        # 1MM/5MM
        self.option_767_limit_3012 = self.driver.find_element(By.ID, "option-767-limit-3012")

        # Deductibles
        # $25K/$50K
        self.option_767_deductible_1234 = self.driver.find_element(By.ID, "option-767-deductible-1234")

        # Proceed to Quote
        self.proceed_to_quote = self.driver.find_element(By.XPATH,
                                                    "//div[@id='saw-application-coverage-builder']/form/div[5]/a/span[2]/span/span")

        return self

        # select_CyberRisk_Only_with_Cyber_Crime_Only_No_PCI()
        # select_CyberRisk_Only_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI()
        # select_Medefense_Plus_Only()
        # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit()
        # select_Medefense_Plus_and_CyberRisk_with_Cyber_Crime_Combined_Shared_Limits_No_PCI
        # select_Medefense_Plus_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI
        # select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Cyber_Crime_No_PCI
        # select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI
        # select_Medefense_Plus_with_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime_No_PCI
        # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI
        # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime_No_PCI
        # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI


    def select_CyberRisk_Only_with_Cyber_Crime_Only_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_758_limit_2969.click()
        No_PCI_Coverage_Options.PageElements(self).option_758_deductible_1232.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_CyberRisk_Only_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_759_limit_2972.click()
        No_PCI_Coverage_Options.PageElements(self).option_759_deductible_1232.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_Only(self):
        No_PCI_Coverage_Options.PageElements(self).option_748_limit_2922.click()
        No_PCI_Coverage_Options.PageElements(self).option_748_deductible_1228.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit(self):
        No_PCI_Coverage_Options.PageElements(self).option_749_limit_2927.click()
        No_PCI_Coverage_Options.PageElements(self).option_749_deductible_1229.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_with_Cyber_Crime_Combined_Shared_Limits_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_760_limit_2975.click()
        No_PCI_Coverage_Options.PageElements(self).option_760_deductible_1233.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_761_limit_2978.click()
        No_PCI_Coverage_Options.PageElements(self).option_761_deductible_1233.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Cyber_Crime_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_762_limit_2984.click()
        No_PCI_Coverage_Options.PageElements(self).option_762_deductible_1233.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_763_limit_2992.click()
        No_PCI_Coverage_Options.PageElements(self).option_763_deductible_1233.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_764_limit_2995.click()
        No_PCI_Coverage_Options.PageElements(self).option_764_deductible_1234.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_765_limit_2998.click()
        No_PCI_Coverage_Options.PageElements(self).option_765_deductible_1234.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_766_limit_3005.click()
        No_PCI_Coverage_Options.PageElements(self).option_766_deductible_1234.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime_No_PCI(
            self):
        No_PCI_Coverage_Options.PageElements(self).option_767_limit_3012.click()
        No_PCI_Coverage_Options.PageElements(self).option_767_deductible_1234.click()
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()

    def proceed_to_quote(self):
        No_PCI_Coverage_Options.PageElements(self).proceed_to_quote.click()