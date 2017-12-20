from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Applicant is a

        # Individual
        self.individual = self.driver.find_element(By.ID, "mmtm-applicant-individual")


        # Corporation
        self.corporation = self.driver.find_element(By.ID, "mmtm-applicant-corporation")

        # Partnership
        self.partnership = self.driver.find_element(By.ID, "mmtm-applicant-partnership")

        # Other
        self.other = self.driver.find_element(By.ID, "mmtm-applicant-other")

        # Online Vendor(platform on which you sell products or services):
        self.online_vendor_platform = self.driver.find_element(By.ID, "mmtm-platform")

        # Merchant Identification Number(for which coverage is desired):
        self.merchant_id = self.driver.find_element(By.ID, "mmtm-merchant")

        # Applicant's estimated Cost of Goods Sold as a percentage of Gross Sales:

        # <=15%
        self.cogs_15_percent = self.driver.find_element(By.ID, "mmtm_goods_less_than_15")

        # >15% - 25%
        self.cogs_15_25_percent = self.driver.find_element(By.ID, "mmtm_goods_between_15_to_25")

        # >25% - 35%
        self.cogs_25_35_percent = self.driver.find_element(By.ID, "mmtm_goods_between_25_to_35")

        # >35% - 45%
        self.cogs_35_45_percent = self.driver.find_element(By.ID, "mmtm_goods_between_25_to_35")

        # >45%
        self.cogs_45_percent = self.driver.find_element(By.ID, "mmtm_goods_greater_than_45")

        # Years in Business:

        # <2 years
        self.years_in_business_2_years = self.driver.find_element(By.ID, "mmtm_business_less_than_2")

        # 2 - 5 years
        self.years_in_business_2_5_years = self.driver.find_element(By.ID, "mmtm_business_between_2_to_5")

        # >5 years
        self.years_in_business_5_years = self.driver.find_element(By.ID, "mmtm_business_greater_than_5")

        # Positive Feedback Rating (average) for past 365 days(%):
        self.positive_feedback_rating = self.driver.find_element(By.ID, "mmtm_feedback")

        # Do you purchase all your inventory directly from authorized manufacturers, wholesalers, or distributors?
        self.inventory_purchase_yes = self.driver.find_element(By.ID, "mmtm_inventory_purchase-yes")

        self.inventory_purchase_no = self.driver.find_element(By.ID, "mmtm_inventory_purchase-no")

        # Do you fulfill all your inventory using Fulfillment by Amazon(FBA)
        self.amazon_fulfill_yes = self.driver.find_element(By.ID, "mmtm_amazon_fulfill-yes")

        self.amazon_fulfill_no = self.driver.find_element(By.ID, "mmtm_amazon_fulfill-no")

        # Have you received any inquiries or requests for additional details from the online Vendor regarding your seller account in the past 180 days
        self.seller_account_inquiry_yes = self.driver.find_element(By.ID, "mmtm_seller_account_inquiry-yes")

        self.seller_account_inquiry_no = self.driver.find_element(By.ID, "mmtm_seller_account_inquiry-no")

        # Has your seller account been suspended by the Online Vendor in the past 365 days
        self.seller_account_suspension_yes = self.driver.find_element(By.ID, "mmtm_seller_account_suspension-yes")

        self.seller_account_suspension_no = self.driver.find_element(By.ID, "mmtm_seller_account_suspension-no")

        # Have you ever had an online seller account on any platform terminated on a permanent basis
        self.seller_account_online_yes = self.driver.find_element(By.ID, "mmtm_seller_account_online-yes")

        self.seller_account_online_no = self.driver.find_element(By.ID, "mmtm_seller_account_online-no")

        # Are you aware of any circumstance, incident or issue relating to your online selling activities, conduct or performance that is likely to result in a suspension or ban
        self.online_seller_issues_yes = self.driver.find_element(By.ID, "mmtm_online_seller_issues-yes")

        self.online_seller_issues_no = self.driver.find_element(By.ID, "mmtm_online_seller_issues-no")

        return self

    def create_quote_individual(self, online_vendor, merchant_id, positive_feedback_rating_percent):

        PAF.Page_Elements(self).individual.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    def create_quote_corporation(self, online_vendor, merchant_id, positive_feedback_rating_percent):

        PAF.Page_Elements(self).corporation.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    def create_quote_partnership(self, online_vendor, merchant_id, positive_feedback_rating_percent):

        PAF.Page_Elements(self).partnership.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    def create_quote_other(self, online_vendor, merchant_id, positive_feedback_rating_percent):

        PAF.Page_Elements(self).other.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    def create_quote_revenue_between_500K_1MM(self, online_vendor, merchant_id, positive_feedback_rating_percent):
        PAF.Page_Elements(self).individual.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    def create_quote_revenue_between_1MM_2pt5MM(self, online_vendor, merchant_id, positive_feedback_rating_percent):
        PAF.Page_Elements(self).individual.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    def create_quote_revenue_over_2pt5MM(self, online_vendor, merchant_id, positive_feedback_rating_percent):
        PAF.Page_Elements(self).individual.click()
        PAF.Page_Elements(self).online_vendor_platform.send_keys(online_vendor)
        PAF.Page_Elements(self).merchant_id.send_keys(merchant_id)
        PAF.Page_Elements(self).cogs_15_percent.click()
        PAF.Page_Elements(self).years_in_business_2_years.click()
        PAF.Page_Elements(self).positive_feedback_rating.send_keys(positive_feedback_rating_percent)
        PAF.Page_Elements(self).inventory_purchase_yes.click()
        PAF.Page_Elements(self).amazon_fulfill_yes.click()
        PAF.Page_Elements(self).seller_account_inquiry_no.click()
        PAF.Page_Elements(self).seller_account_suspension_no.click()
        PAF.Page_Elements(self).seller_account_online_no.click()
        PAF.Page_Elements(self).online_seller_issues_no.click()

    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[3]/div[3]/a/span[2]/span/span")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()