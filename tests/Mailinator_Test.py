import unittest
from faker import company
from faker import name
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Mailinator_Test(unittest.TestCase):

    def create_email_address_check_mailinator(self):

        # Create "Fake" Variables
        first_name = name.first_name()
        last_name = name.last_name()
        company_name = company.company_name()

        email_address_string = "QA-Test" + "-" + first_name + "." + last_name + "@mailinator.com"

        # ### TODO
        # ### Code to launch the application and input the created email address string
        # ### Send a notification email

        # Initialize Driver; Launch URL
        baseURL = "https://www.mailinator.com"
        driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

        # Maximize Window; Launch URL
        driver.maximize_window()
        driver.get(baseURL)

        element_present = EC.element_to_be_clickable((By.LINK_TEXT, 'EMAIL'))
        WebDriverWait(driver, timeout=10).until(element_present)

        # Click Email link
        email_link = driver.find_element(By.LINK_TEXT, "EMAIL")
        email_link.click()

        # Input email address string into Inbox Text Field
        public_inbox_field = driver.find_element_by_id("publicinboxfield")
        public_inbox_field.clear()
        public_inbox_field.send_keys(email_address_string)

        # Click Go (Email should display)
        go_button = driver.find_element_by_xpath("(//button[@type='button'])[2]")
        go_button.click()

        # Put a Break Point on Next line to verify that email was received
        driver.implicitly_wait(3)

mt = Mailinator_Test()
mt.create_email_address_check_mailinator()