from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BallPark_Indication():

    def __init__(self, driver):
        self.driver = driver

    def click_Download_Send_Indication(self):
        download_send_indication_button = self.driver.find_element(By.XPATH, "//form[@id='ballpark-indication-form']/div[6]/a[3]/span[2]/span/span")
        download_send_indication_button.click()

    def click_Request_Quote(self):
        request_quote_button = self.driver.find_element(By.XPATH, "//form[@id='ballpark-indication-form']/div[6]/a[2]/span[2]/span/span")
        request_quote_button.click()

    def click_exit(self):
        exit_button = self.driver.find_element(By.NAME, "Exit")
        exit_button.click()