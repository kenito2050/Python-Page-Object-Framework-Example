from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # CyberRisk™ with Cyber Crime Only

        # Limits
        # 1MM/1MM
        self.option_435_limit_1920 = self.driver.find_element(By.ID, "option-435-limit-1920")

        # Deductibles
        # $50,000
        self.option_435_deductible_772 = self.driver.find_element(By.ID, "option-435-deductible-772")

        # CyberRisk™ Only with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_436_limit_1942 = self.driver.find_element(By.ID, "option-436-limit-1942")

        # Deductibles
        # $25,000
        self.option_436_deductible_772 = self.driver.find_element(By.ID, "option-436-deductible-772")

        # Medefense™ Plus Only

        # Limits
        # 1MM/2MM
        self.option_309_limit_1523 = self.driver.find_element(By.ID, "option-309-limit-1523")

        # Deductibles
        # $25,000
        self.option_309_deductible_54 = self.driver.find_element(By.ID, "option-309-deductible-54")

        # Medefense™ Plus with Peer Review Proceeding Sublimit

        # Limits
        # 1MM/5MM
        self.option_310_limit_1528 = self.driver.find_element(By.ID, "option-310-limit-1528")

        # Deductibles
        # $25,000
        self.option_310_deductible_195 = self.driver.find_element(By.ID, "option-310-deductible-195")

        # Medefense™ Plus and CyberRisk™ with Cyber Crime Combined Shared Limits

        # Limits
        # 1MM/1MM
        self.option_431_limit_1923 = self.driver.find_element(By.ID, "option-431-limit-1923")

        # Deductibles
        # $25K/$50K
        self.option_431_deductible_773 = self.driver.find_element(By.ID, "option-431-deductible-773")

        # Medefense™ Plus and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_437_limit_1945 = self.driver.find_element(By.ID, "option-437-limit-1945")

        # Deductibles
        # $25K/$50K
        self.option_437_deductible_773 = self.driver.find_element(By.ID, "option-437-deductible-773")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_432_limit_1929 = self.driver.find_element(By.ID, "option-432-limit-1929")

        # Deductibles
        # $25K/$50K
        self.option_432_deductible_773 = self.driver.find_element(By.ID, "option-432-deductible-773")

        # Medefense™ Plus and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_438_limit_1952 = self.driver.find_element(By.ID, "option-438-limit-1952")

        # Deductibles
        # $25K/$50K
        self.option_438_deductible_773 = self.driver.find_element(By.ID, "option-438-deductible-773")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_433_limit_1932 = self.driver.find_element(By.ID, "option-433-limit-1932")

        # Deductibles
        # $25K/$50K
        self.option_433_deductible_759 = self.driver.find_element(By.ID, "option-433-deductible-759")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Shared Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/1MM
        self.option_439_limit_1955 = self.driver.find_element(By.ID, "option-439-limit-1955")

        # Deductibles
        # $25K/$50K
        self.option_439_deductible_759 = self.driver.find_element(By.ID, "option-439-deductible-759")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Separate Limits with Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_434_limit_1939 = self.driver.find_element(By.ID, "option-434-limit-1939")

        # Deductibles
        # $25K/$50K
        self.option_434_deductible_759 = self.driver.find_element(By.ID, "option-434-deductible-759")

        # Medefense™ Plus with Peer Review Proceeding Sublimit and CyberRisk™ Combined Separate Limits with Claim Expenses Outside Limits and Cyber Crime

        # Limits
        # 1MM/5MM
        self.option_440_limit_1962 = self.driver.find_element(By.ID, "option-440-limit-1962")

        # Deductibles
        # $25K/$50K
        self.option_440_deductible_759 = self.driver.find_element(By.ID, "option-440-deductible-759")


        return self

    # select_CyberRisk_with_Cyber_Crime_Only()
    # select_CyberRisk_Only_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()
    # select_Medefense_Plus_Only()
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit()
    # select_Medefense_Plus_and_CyberRisk_with_Cyber_Crime_Combined_Shared_Limits()
    # select_Medefense_Plus_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()
    # select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Cyber_Crime()
    # select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime()
    # select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime()


    def select_CyberRisk_with_Cyber_Crime_Only(self):
        PCI_Coverage_Options.PageElements(self).option_435_limit_1920.click()
        PCI_Coverage_Options.PageElements(self).option_435_deductible_772.click()

    def select_CyberRisk_Only_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_436_limit_1942.click()
        PCI_Coverage_Options.PageElements(self).option_436_deductible_772.click()

    def select_Medefense_Plus_Only(self):
        PCI_Coverage_Options.PageElements(self).option_309_limit_1523.click()
        PCI_Coverage_Options.PageElements(self).option_309_deductible_54.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit(self):
        PCI_Coverage_Options.PageElements(self).option_310_limit_1528.click()
        PCI_Coverage_Options.PageElements(self).option_310_deductible_195.click()

    def select_Medefense_Plus_and_CyberRisk_with_Cyber_Crime_Combined_Shared_Limits(self):
        PCI_Coverage_Options.PageElements(self).option_431_limit_1923.click()
        PCI_Coverage_Options.PageElements(self).option_431_deductible_773.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_437_limit_1945.click()
        PCI_Coverage_Options.PageElements(self).option_437_deductible_773.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_432_limit_1929.click()
        PCI_Coverage_Options.PageElements(self).option_432_deductible_773.click()

    def select_Medefense_Plus_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_438_limit_1952.click()
        PCI_Coverage_Options.PageElements(self).option_438_deductible_773.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_439_limit_1955.click()
        PCI_Coverage_Options.PageElements(self).option_439_deductible_759.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Shared_Limits_with_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_434_limit_1939.click()
        PCI_Coverage_Options.PageElements(self).option_434_deductible_759.click()

    def select_Medefense_Plus_with_Peer_Review_Proceeding_Sublimit_and_CyberRisk_Combined_Separate_Limits_with_Claim_Expenses_Outside_Limits_and_Cyber_Crime(self):
        PCI_Coverage_Options.PageElements(self).option_440_limit_1962.click()
        PCI_Coverage_Options.PageElements(self).option_440_deductible_759.click()