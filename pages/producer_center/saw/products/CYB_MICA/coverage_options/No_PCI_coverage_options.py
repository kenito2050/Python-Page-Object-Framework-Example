from selenium.webdriver.common.by import By

class No_PCI_Coverage_Options():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # MEDEFENSE™ Plus Only

        # Limits
        # 1MM/1MM
        self.option_658_limit_2753 = self.driver.find_element(By.ID, "option-658-limit-2753")

        # Deductibles
        # $1,500
        self.option_658_deductible_1186 = self.driver.find_element(By.ID, "option-658-deductible-1186")

        # Cyber Liability Only - No PCI

        # Limits
        # 1MM/1MM
        self.option_667_limit_2760 = self.driver.find_element(By.ID, "option-667-limit-2760")

        # Deductibles
        # $0
        self.option_667_deductible_1189 = self.driver.find_element(By.ID, "option-667-deductible-1189")

        # $2M Cyber Liability Only - No PCI
        # Limits
        # 2MM/2MM
        self.option_942_limit_3676 = self.driver.find_element(By.ID, "option-942-limit-3676")

        # Deductibles
        # $0
        self.option_942_deductible_1189 = self.driver.find_element(By.ID, "option-942-deductible-1189")

        # $3M Cyber Liability Only - No PCI
        # Limits
        # 3MM/3MM
        self.option_943_limit_3677 = self.driver.find_element(By.ID, "option-943-limit-3677")

        # Deductibles
        # $0
        self.option_943_deductible_1189 = self.driver.find_element(By.ID, "option-943-deductible-1189")

        # Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_669_limit_2761 = self.driver.find_element(By.ID, "option-669-limit-2761")

        # Deductibles
        # $0
        self.option_669_deductible_1189 = self.driver.find_element(By.ID, "option-669-deductible-1189")

        # $2M Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 2MM/2MM
        self.option_946_limit_3678 = self.driver.find_element(By.ID, "option-946-limit-3678")

        # Deductibles
        # $0
        self.option_946_deductible_1189 = self.driver.find_element(By.ID, "option-946-deductible-1189")

        # $3M Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_947_limit_3679 = self.driver.find_element(By.ID, "option-947-limit-3679")

        # Deductibles
        # $0
        self.option_947_deductible_1189 = self.driver.find_element(By.ID, "option-947-deductible-1189")

        # Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_668_limit_2760 = self.driver.find_element(By.ID, "option-668-limit-2760")

        # Deductibles
        # $0
        self.option_668_deductible_1189 = self.driver.find_element(By.ID, "option-668-deductible-1189")

        # $2M Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 2MM/2MM
        self.option_944_limit_3676 = self.driver.find_element(By.ID, "option-944-limit-3676")

        # Deductibles
        # $0
        self.option_944_deductible_1189 = self.driver.find_element(By.ID, "option-944-deductible-1189")

        # $3M Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_945_limit_3677 = self.driver.find_element(By.ID, "option-945-limit-3677")

        # Deductibles
        # $0
        self.option_945_deductible_1189 = self.driver.find_element(By.ID, "option-945-deductible-1189")

        # Cyber Liability with Claims Expenses Outside the Limits and Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_670_limit_2761 = self.driver.find_element(By.ID, "option-670-limit-2761")

        # Deductibles
        # $0
        self.option_670_deductible_1189 = self.driver.find_element(By.ID, "option-670-deductible-1189")

        # $2M Cyber Liability with Claims Expenses Outside the Limits and Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 2MM/2MM
        self.option_948_limit_3678 = self.driver.find_element(By.ID, "option-948-limit-3678")

        # Deductibles
        # $0
        self.option_948_deductible_1189 = self.driver.find_element(By.ID, "option-948-deductible-1189")

        # $3M Cyber Liability with Claims Expenses Outside the Limits and Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_949_limit_3979 = self.driver.find_element(By.ID, "option-949-limit-3679")

        # Deductibles
        # $0
        self.option_494_deductible_1189 = self.driver.find_element(By.ID, "option-949-deductible-1189")

        # MEDEFENSE™ Plus and Cyber Liability Combined - No PCI

        # Limits
        # 3MM/3MM
        self.option_671_limit_2762 = self.driver.find_element(By.ID, "option-671-limit-2762")

        # Deductibles
        # $1,500/$0
        self.option_671_deductible_1190 = self.driver.find_element(By.ID, "option-671-deductible-1190")

        # $2M MEDEFENSE™ Plus and Cyber Liability Combined - No PCI

        # Limits
        # 2MM/2MM
        self.option_959_limit_3680 = self.driver.find_element(By.ID, "option-959-limit-3680")

        # Deductibles
        # $1,500 / $0
        self.option_959_deductible_1190 = self.driver.find_element(By.ID, "option-959-deductible-1190")

        # $3M MEDEFENSE™ Plus and Cyber Liability Combined - No PCI

        # Limits
        # 3MM/3MM
        self.option_960_limit_3681 = self.driver.find_element(By.ID, "option-960-limit-3681")

        # Deductibles
        # $0
        self.option_960_deductible_1190 = self.driver.find_element(By.ID, "option-960-deductible-1190")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 2MM/2MM
        self.option_673_limit_2763 = self.driver.find_element(By.ID, "option-673-limit-2763")

        # Deductibles
        # $1,500 / $0
        self.option_673_deductible_1190 = self.driver.find_element(By.ID, "option-673-deductible-1190")

        # $2M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_963_limit_3682 = self.driver.find_element(By.ID, "option-963-limit-3682")

        # Deductibles
        # $1,500 / $0
        self.option_963_deductible_1190 = self.driver.find_element(By.ID, "option-963-deductible-1190")

        # $3M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_964_limit_3683 = self.driver.find_element(By.ID, "option-964-limit-3683")

        # Deductibles
        # $1,500 / $0
        self.option_964_deductible_1190 = self.driver.find_element(By.ID, "option-964-deductible-1190")

        # MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_672_limit_2762 = self.driver.find_element(By.ID, "option-672-limit-2762")

        # Deductibles
        # $1,500 / $0
        self.option_672_deductible_1190 = self.driver.find_element(By.ID, "option-672-deductible-1190")

        # $2M MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 2MM/2MM
        self.option_961_limit_3680 = self.driver.find_element(By.ID, "option-961-limit-3680")

        # Deductibles
        # $1,500 / $0
        self.option_961_deductible_1190 = self.driver.find_element(By.ID, "option-961-deductible-1190")

        # $3M MEDEFENSE™ Plus and Cyber Liability with Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_962_limit_3681 = self.driver.find_element(By.ID, "option-962-limit-3681")

        # Deductibles
        # $1,500 / $0
        self.option_962_deductible_1190 = self.driver.find_element(By.ID, "option-962-deductible-1190")

        # MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 1MM/1MM
        self.option_674_limit_2763 = self.driver.find_element(By.ID, "option-674-limit-2763")

        # Deductibles
        # $1,500 / $0
        self.option_674_deductible_1190 = self.driver.find_element(By.ID, "option-674-deductible-1190")

        # $2M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 2MM/2MM
        self.option_965_limit_3682 = self.driver.find_element(By.ID, "option-965-limit-3682")

        # Deductibles
        # $1,500 / $0
        self.option_965_deductible_1190 = self.driver.find_element(By.ID, "option-965-deductible-1190")

        # $3M MEDEFENSE™ Plus and Cyber Liability with Claims Expenses Outside the Limits and Breach Event Costs Outside the Limits - No PCI

        # Limits
        # 3MM/3MM
        self.option_966_limit_3683 = self.driver.find_element(By.ID, "option-966-limit-3683")

        # Deductibles
        # $1,500 / $0
        self.option_966_deductible_1190 = self.driver.find_element(By.ID, "option-966-deductible-1190")

        return self

    def select_Cyber_Liability_Only_No_PCI(self):
        No_PCI_Coverage_Options.PageElements(self).option_667_limit_2760.click()
        No_PCI_Coverage_Options.PageElements(self).option_667_deductible_1189.click()