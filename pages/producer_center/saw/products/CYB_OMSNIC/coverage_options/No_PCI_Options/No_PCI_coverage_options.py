from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # e-MD™ Cyber Liability without PCI DSS Liability

        # Limits

        # 1MM
        self.option_1170_limit_4476 = self.driver.find_element(By.ID, "option-1170-limit-4476")

        # Label
        self.label_option_1170_limit_4476 = self.driver.find_element(By.XPATH, "//label[@for='option-1170-limit-4476']")

        # Deductibles
        # $0
        self.option_1170_deductible_1800 = self.driver.find_element(By.ID, "option-1170-deductible-1800")

        # Label
        self.label_option_1170_deductible_1800 = self.driver.find_element(By.XPATH, "//label[@for='option-1170-deductible-1800']")

        return self

    ## Return Text for Limits

    def return_eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_label_text(self):
        eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_text = (No_PCI_Coverage_Options.PageElements(self).label_option_1170_limit_4476.text)
        return eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_text

    ## Return Text for Deductibles

    def return_eMD_Cyber_Liability_without_PCI_DSS_0_deductible_label_text(self):
        eMD_Cyber_Liability_without_PCI_DSS_0_deductible_label_text = (No_PCI_Coverage_Options.PageElements(self).label_option_1170_deductible_1800.text)
        return eMD_Cyber_Liability_without_PCI_DSS_0_deductible_label_text

    def select_eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_0_Deduct(self):
        No_PCI_Coverage_Options.PageElements(self).option_1170_limit_4476.click()
        No_PCI_Coverage_Options.PageElements(self).option_1170_deductible_1800.click()