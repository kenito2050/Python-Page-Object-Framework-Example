from urllib.parse import urlparse, parse_qs
from selenium.webdriver.common.by import By

class ClientContact():

    def __init__(self, driver):
        self.driver = driver

    def parse_url_get_app_id(self):
        #test_url = 'https://proddev.wn.nasinsurance.com/index.php?c=saw.application.primary&app_id=12169'
        current_url = self.driver.current_url
        parts = urlparse(current_url)
        query_dict = parse_qs(parts.query)
        application_id = (query_dict['app_id'][0])
        return application_id
        #print(parts)
        #print(query_dict)
        #print(query_dict['app_id'][0])

    def parse_url_get_app_id_draft(self, application_id):
        # test_url = 'https://proddev.wn.nasinsurance.com/index.php?c=saw.application.primary&app_id=12169'
        current_url = self.driver.current_url
        parsed_url_string = urlparse(current_url)
        query_string = parsed_url_string.query
        application_id = query_string[-5:]
        return application_id

    def click_next(self):
        next_button = self.driver.find_element(By.CSS_SELECTOR, "span.button-mid")
        next_button.click()