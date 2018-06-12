from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BallPark_PAF():

    def __init__(self, driver):
        self.driver = driver

    def switch_windows(self):
        # Switch Windows
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)

        # switch windows
        self.driver.switch_to.window(self.driver.window_handles[1])

        # wait to make sure the new window is loaded
        WebDriverWait(self.driver, 10).until(lambda d: d.title != "")

        self.driver.maximize_window()

    def select_contract_class(self, contract_class):
        select_contract_class = self.driver.find_element(By.ID, "coverage_category__contract_class_name")
        select_contract_class.send_keys(contract_class)

    def start_ballpark_enter_faker_company_name_valid_zip(self, company_name_string, postal_code):
        name_of_Insured_field = self.driver.find_element(By.ID, "name")
        name_of_Insured_field.clear()
        name_of_Insured_field.send_keys(company_name_string)

        zip_code = self.driver.find_element(By.ID, "zip")
        zip_code.send_keys(postal_code)

    def click_ballpark_button(self):
        ballpark_button = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        ballpark_button.click()

        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

    def select_CYB_AAO(self):

        # CYB_AAO - product - list - item - 44
        cb_CYB_AAO = self.driver.find_element(By.ID, "product-list-item-44")

        cb_CYB_AAO.click()


    def select_CYB_CAP(self):

        # CYB_CAP - product - list - item - 33
        cb_CYB_CAP = self.driver.find_element(By.ID, "product-list-item-33")

        cb_CYB_CAP.click()

    def select_CYB_MDA(self):
            # Ballpark Product Identifiers

            # TODO: Move these identifiers into a separate class

            # CYB_MDA - product - list - item - 9
            cb_CYB_MDA = self.driver.find_element(By.ID, "product-list-item-9")

            cb_CYB_MDA.click()

    def select_CYB_MMIC(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # CYB_MMIC - product - list - item - 21
        cb_CYB_MMIC = self.driver.find_element(By.ID, "product-list-item-21")

        cb_CYB_MMIC.click()


    def select_CYB_MICA(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 74
        cb_CYB_MICA = self.driver.find_element(By.ID, "product-list-item-70")

        cb_CYB_MICA.click()

    def select_CYB_PSIC_DDS(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 67
        cb_CYB_PSIC_DDS = self.driver.find_element(By.ID, "product-list-item-67")

        cb_CYB_PSIC_DDS.click()

    def select_CYB_PSIC_MD(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 66
        cb_CYB_PSIC_MD = self.driver.find_element(By.ID, "product-list-item-66")

        cb_CYB_PSIC_MD.click()

    def select_EO_MISC(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # EO_MISC - product - list - item - 62
        cb_EO_MISC = self.driver.find_element(By.ID, "product-list-item-62")

        cb_EO_MISC.click()

    def select_LSA(self):
            # Ballpark Product Identifiers

            # TODO: Move these identifiers into a separate class

            # LSA Cyber Liability / Medefense™ Plus - product - list - item - 111
            cb_LSA = self.driver.find_element(By.ID, "product-list-item-111")

            cb_LSA.click()

    def select_LTC(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 74
        cb_LTC = self.driver.find_element(By.ID, "product-list-item-32")

        cb_LTC.click()

    def select_NGP(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 74
        cb_NGP = self.driver.find_element(By.ID, "product-list-item-74")

        cb_NGP.click()

    def select_NGP_CAMICO(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 74
        cb_NGP_CAMICO = self.driver.find_element(By.ID, "product-list-item-109")

        cb_NGP_CAMICO.click()

    def select_NGP_OBLIC(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP_old Cyber Liability - product - list - item - 74
        cb_NGP_OBLIC = self.driver.find_element(By.ID, "product-list-item-86")

        cb_NGP_OBLIC.click()

    def select_NGP_USPRO(self):

        # Ballpark Product Identifiers
        # US Pro Cyber Liability  - product-list-item-105
        cb_NGP_USPRO = self.driver.find_element(By.ID, "product-list-item-105")

        cb_NGP_USPRO.click()

        #Other Products

        # PrivaSafe Cyber Liability  - product-list-item-82
        cb_NGP_USI = self.driver.find_element(By.ID, "product-list-item-82")

        # Swett IIABCal Cyber Liability - product-list-item-83
        cb_NGP_SWETT = self.driver.find_element(By.ID, "product-list-item-83")

    def wait_until_effective_date_field_displays(self):

        userElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'effective-date')))


    def enter_effective_date(self, ad_hoc_effectiveDate):

        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.presence_of_element_located((By.ID, 'effective-date')))

        effective_date = self.driver.find_element(By.ID, "effective-date")
        effective_date.click()
        effective_date.clear()
        effective_date.send_keys(ad_hoc_effectiveDate)

        # Click Zip Code Field (Popup calendar should disappear)

        zip_code = self.driver.find_element(By.ID, "zip")
        zip_code.click()

    def enter_current_date(self, date_today):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.ID, 'effective-date')))

        effective_date = self.driver.find_element(By.ID, "effective-date")
        effective_date.click()
        effective_date.clear()
        effective_date.send_keys(date_today)

        # Click Zip Code Field (Popup calendar should disappear)

        zip_code = self.driver.find_element(By.ID, "zip")
        zip_code.click()

    def enter_revenue(self, revenue):
        revenue_field = self.driver.find_element(By.ID, "annual_revenue_current_year")
        revenue_field.send_keys(revenue)

    # Use this for EO_MISC
    def enter_revenue_EO_MISC(self, revenue):
        annual_revenue_next_year_field = self.driver.find_element(By.ID, "annual_revenue_next_year")
        annual_revenue_next_year_field.send_keys(revenue)

    def enter_bed_count(self, bed_count):
        bed_count_field = self.driver.find_element(By.ID, 'bed_count')
        bed_count_field.send_keys(bed_count)

    def click_doctor_count_field(self):
        doctor_count_field = self.driver.find_element(By.ID, "physician_count")
        doctor_count_field.click()

    def enter_doctor_count(self, staff_count):
        physician_count = self.driver.find_element(By.ID, "physician_count")
        physician_count.send_keys(staff_count)

