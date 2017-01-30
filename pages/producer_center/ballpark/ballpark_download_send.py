from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BallPark_Download_Send():

    def __init__(self, driver):
        self.driver = driver

    def input_email(self):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.click()
        email_field.clear()
        email_field.send_keys("qatest@nasinsurance.com")

    def click_send_email(self):
        send_button = self.driver.find_element(By.ID, "send-email-text")
        send_button.click()