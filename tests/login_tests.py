from xml.etree import ElementTree as ET
from selenium import webdriver
from pages.service_center.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):

        # Access XML to retrieve login credentials
        tree = ET.parse('resources.xml')
        root = tree.getroot()

        username = (root[0][0].text)
        password = (root[0][1].text)

        # Initialize Driver; Launch URL
        baseURL = "http://svcrel.wn.nasinsurance.com/"
        driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

        # Maximize Window; Launch URL
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Call Login methods from Pages.home.login_page.py
        lp = LoginPage(driver)
        lp.login(username, password)

        # Wait
        driver.implicitly_wait(10)

        # Close Browser
        driver.quit()