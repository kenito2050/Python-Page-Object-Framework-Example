from selenium import webdriver
import unittest
import os
from xml.etree import ElementTree as ET
from utilities.Environments.Environments import Environments

from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar

import datetime
import time
from urllib.parse import urlparse, parse_qs

class Unittest_login_create_quote(unittest.TestCase):

    def setUp(self):

        ## Directory Locations
        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))

        self.driver = webdriver.Chrome(os.path.join(config_file_directory, 'chromedriver.exe'))

    def test_login(self):

        ## Directory Locations
        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        ## Read in value from test_environment.xml
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment = tree.getroot()
        environment = (test_environment[0][0].text)

        ## Select Appropriate URL based on the Environment Value from above
        base_URL = Environments.return_environments(environment)

        # self.driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

        # Maximize Window; Launch URL
        self.driver.maximize_window()

        self.driver.get(base_URL)

        self.driver.implicitly_wait(3)

        # Access XML to retrieve login credentials
        tree = ET.parse(os.path.join(config_file_directory, 'resources.xml'))
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[0][1].text)

        lp = LoginPage(self.driver)
        lp.login(username, password)
        lp.click_login_button()

        nb = NavigationBar(self.driver)
        nb.logout_Exists()

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()