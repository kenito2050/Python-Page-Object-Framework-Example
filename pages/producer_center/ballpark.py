from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BallPark():

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

    def start_ballpark_enter_faker_company_name_valid_zip(self, company_name_string, postal_code):
        name_of_Insured_field = self.driver.find_element(By.ID, "name")
        name_of_Insured_field.clear()
        name_of_Insured_field.send_keys(company_name_string)

        zip_code = self.driver.find_element(By.ID, "zip")
        zip_code.send_keys(postal_code)