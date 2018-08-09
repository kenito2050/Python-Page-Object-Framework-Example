from selenium.webdriver.common.by import By

class PCI_Coverage_Options_Renewal():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit

        # Limits

        # $250,000 (Full Sublimits) ($250K PCI)
        self.option_971_limit_3708 = self.driver.find_element(By.ID, "option-971-limit-3708")

        # Label
        self.label_option_971_limit_3708 = self.driver.find_element(By.XPATH, "//label[@for='option-971-limit-3708']")

        # $500,000 (Full Sublimits) ($500K PCI)
        self.option_971_limit_3709 = self.driver.find_element(By.ID, "option-971-limit-3709")

        # Label
        self.label_option_971_limit_3709 = self.driver.find_element(By.XPATH, "//label[@for='option-971-limit-3709']")

        # $1,000,000 (Full Sublimits) ($1MM PCI)
        self.option_971_limit_3710 = self.driver.find_element(By.ID, "option-971-limit-3710")

        # Label
        self.label_option_971_limit_3710 = self.driver.find_element(By.XPATH, "//label[@for='option-971-limit-3710']")

        # $2,000,000 (Full Sublimits) ($1MM PCI)
        self.option_971_limit_3711 = self.driver.find_element(By.ID, "option-971-limit-3711")

        # Label
        self.label_option_971_limit_3711 = self.driver.find_element(By.XPATH, "//label[@for='option-971-limit-3711']")

        # Deductibles
        # $500
        self.option_971_deductible_1432 = self.driver.find_element(By.ID, "option-971-deductible-1432")

        # Label
        self.label_option_971_deductible_1432 = self.driver.find_element(By.XPATH, "//label[@for='option-971-deductible-1432']")

        # $1,000
        self.option_971_deductible_1427 = self.driver.find_element(By.ID, "option-971-deductible-1427")

        # Label
        self.label_option_971_deductible_1427 = self.driver.find_element(By.XPATH, "//label[@for='option-971-deductible-1427']")

        # $2,500
        self.option_971_deductible_1428 = self.driver.find_element(By.ID, "option-971-deductible-1428")

        # Label
        self.label_option_971_deductible_1428 = self.driver.find_element(By.XPATH, "//label[@for='option-971-deductible-1428']")

        # $5,000
        self.option_971_deductible_1429 = self.driver.find_element(By.ID, "option-971-deductible-1429")

        # Label
        self.label_option_971_deductible_1429 = self.driver.find_element(By.XPATH, "//label[@for='option-971-deductible-1429']")

        # $10,000
        self.option_971_deductible_1430 = self.driver.find_element(By.ID, "option-971-deductible-1430")

        # Label
        self.label_option_971_deductible_1430 = self.driver.find_element(By.XPATH, "//label[@for='option-971-deductible-1430']")

        # $25,000
        self.option_971_deductible_1431 = self.driver.find_element(By.ID, "option-971-deductible-1431")

        # Label
        self.label_option_971_deductible_1431 = self.driver.find_element(By.XPATH, "//label[@for='option-971-deductible-1431']")

        # NetGuard™ Plus with BrandGuard™ and PCI Assessment Sublimit Per Identity

        # Limits

        # $250,000 (Full Sublimits) ($250K PCI)
        self.option_1012_limit_3815 = self.driver.find_element(By.ID, "option-1012-limit-3815")

        # Label
        self.label_option_1012_limit_3815 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-limit-3815']")

        # $500,000 (Full Sublimits) ($500K PCI)
        self.option_1012_limit_3816 = self.driver.find_element(By.ID, "option-1012-limit-3815")

        # Label
        self.label_option_1012_limit_3816 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-limit-3816']")

        # $1,000,000 (Full Sublimits) ($1MM PCI)
        self.option_1012_limit_3817 = self.driver.find_element(By.ID, "option-1012-limit-3817")

        # Label
        self.label_option_1012_limit_3817 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-limit-3817']")

        # $2,000,000 (Full Sublimits) ($1MM PCI)
        self.option_1012_limit_3818 = self.driver.find_element(By.ID, "option-1012-limit-3818")

        # Label
        self.label_option_1012_limit_3818 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-limit-3818']")

        # Deductibles
        # $500
        self.option_1012_deductible_1503 = self.driver.find_element(By.ID, "option-1012-deductible-1503")

        # Label
        self.label_option_1012_deductible_1503 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-deductible-1503']")

        # $1,000
        self.option_1012_deductible_1498 = self.driver.find_element(By.ID, "option-1012-deductible-1498")

        # Label
        self.label_option_1012_deductible_1498 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-deductible-1498']")

        # $2,500
        self.option_1012_deductible_1499 = self.driver.find_element(By.ID, "option-1012-deductible-1499")

        # Label
        self.label_option_1012_deductible_1499 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-deductible-1499']")

        # $5,000
        self.option_1012_deductible_1500 = self.driver.find_element(By.ID, "option-1012-deductible-1500")

        # Label
        self.label_option_1012_deductible_1500 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-deductible-1500']")

        # $10,000
        self.option_1012_deductible_1501 = self.driver.find_element(By.ID, "option-1012-deductible-1501")

        # Label
        self.label_option_1012_deductible_1501 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-deductible-1501']")

        # $25,000
        self.option_1012_deductible_1502 = self.driver.find_element(By.ID, "option-1012-deductible-1502")

        # Label
        self.label_option_1012_deductible_1502 = self.driver.find_element(By.XPATH, "//label[@for='option-1012-deductible-1502']")

        return self

    ## Return Text for Limits

    def return_NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3708.text)
        return NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3709.text)
        return NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3710.text)
        return NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3711.text)
        return NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3815.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3816.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3817.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3818.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text

    ## Return Text for Deductibles

    def return_NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1432.text)
        return NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1427.text)
        return NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1428.text)
        return NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1429.text)
        return NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1430.text)
        return NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1431.text)
        return NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1503.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1498.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1499.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1500.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1501.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text

    def return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text(self):
        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1502.text)
        return NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text

    ## Assert Statements

    def assert_limits_and_labels_display(self):

        NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3708.text)
        assert NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text == "$250,000 (Full Sublimits) ($250K PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3709.text)
        assert NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text == "$500,000 (Full Sublimits) ($500K PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3710.text)
        assert NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text == "$1,000,000 (Full Sublimits) ($1MM PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3711.text)
        assert NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text == "$2,000,000 (Full Sublimits) ($2MM PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3815.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text == "$250,000 (Full Sublimits) ($250K PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3816.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text == "$500,000 (Full Sublimits) ($500K PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_limit_3817.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text == "$1,000,000 (Full Sublimits) ($1MM PCI)"
        print (NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1503.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text == "$2,000,000 (Full Sublimits) ($2MM PCI)"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text)

        return \
            (
                NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text
             )

    def assert_deductibles_and_labels_display(self):

        NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1432.text)
        assert NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text == "$500"
        print(NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1427.text)
        assert NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text == "$1,000"
        print(NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1428.text)
        assert NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text == "$2,500"
        print(NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1429.text)
        assert NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text == "$5,000"
        print(NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1430.text)
        assert NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text == "$10,000"
        print(NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1431.text)
        assert NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text == "$25,000"
        print(NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1503.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text == "$500"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1498.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text == "$1,000"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1499.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text == "$2,500"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1500.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text == "$5,000"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1501.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text == "$10,000"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text)

        NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_1012_deductible_1502.text)
        assert NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text == "$25,000"
        print(NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text)

        return \
            (
                NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text,
                NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text
            )

    def test_ken(self, limit):
        print (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3708.text)
        assert limit == (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3708.text)

    def select_NetGuard_Plus_with_BrandGuard_and_PCI_250K_limit_2_pt_5K_Deduct(self):

        limit_label = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_limit_3708.text)
        deductible_label = (PCI_Coverage_Options_Renewal.PageElements(self).label_option_971_deductible_1428.text)
        # print (limit_label, deductible_label)
        PCI_Coverage_Options_Renewal.PageElements(self).option_971_limit_3708.click()
        PCI_Coverage_Options_Renewal.PageElements(self).option_971_deductible_1428.click()


