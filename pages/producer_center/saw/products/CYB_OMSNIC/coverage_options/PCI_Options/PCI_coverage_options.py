from selenium.webdriver.common.by import By

class PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # e-MD™ Cyber Liability

        # Limits

        # $1MM/$1MM
        self.option_1169_limit_4475 = self.driver.find_element(By.ID, "option-1169-limit-4475")

        # Label
        self.label_option_1169_limit_4475 = self.driver.find_element(By.XPATH, "//label[@for='option-1169-limit-4475']")

        # Deductibles
        # $0
        self.option_1169_deductible_1799 = self.driver.find_element(By.ID, "option-1169-deductible-1799")

        # Label
        self.label_option_1169_deductible_1799 = self.driver.find_element(By.XPATH, "//label[@for='option-1169-deductible-1799']")

        return self

    ## Return Text for Limits

    def return_eMD_Cyber_Liability_PCI_Assessment_1MM_limit_label_text(self):
        eMD_Cyber_Liability_PCI_Assessment_1MM_limit_label_text = (PCI_Coverage_Options.PageElements(self).label_option_1169_limit_4475.text)
        return eMD_Cyber_Liability_PCI_Assessment_1MM_limit_label_text

    ## Return Text for Deductibles

    def return_eMD_Cyber_Liability_PCI_Assessment_0_deductible_label_text(self):
        eMD_Cyber_Liability_PCI_Assessment_0_deductible_label_text = (PCI_Coverage_Options.PageElements(self).label_option_1169_deductible_1799.text)
        return eMD_Cyber_Liability_PCI_Assessment_0_deductible_label_text

    def select_eMD_Cyber_Liability_PCI_Assessment_1MM_limit_0_Deduct(self):
        PCI_Coverage_Options.PageElements(self).option_1169_limit_4475.click()
        PCI_Coverage_Options.PageElements(self).option_1169_deductible_1799.click()