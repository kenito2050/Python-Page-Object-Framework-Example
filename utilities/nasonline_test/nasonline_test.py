import datetime
import unittest
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

from faker import address
from faker import company
from faker import name
from selenium import webdriver
import time

import os
import xlrd

from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes

from utilities.contract_classes.contract_classes_Medical import ContractClasses_Medical

global test_summary
global test_scenario
global effective_date
global test_scenario_number
global regression
global smoke
global sanity
global contract_class
global agent
global state
global revenue
global staff_count
global limit
global deductible
global _OLD_scenario
global _OLD_scenario_number


class NasOnlineTest (unittest.TestCase):

    def runTests(self):
        print('parent :-)')
        exit()

    def initialSetup(self):

        # Directory Locations
        self.tests_directory = os.path.abspath(os.pardir)
        self.framework_directory = os.path.abspath(os.path.join(self.tests_directory, os.pardir))
        self.config_file_directory = os.path.abspath(os.path.join(self.framework_directory, 'config_files'))
        self.test_case_directory = os.path.abspath(os.path.join(self.framework_directory, 'utilities\Excel_Sheets\Products'))
        self.test_results_directory = os.path.abspath( os.path.join(self.framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        # Determine Test Environment to run scripts
        # Read in value from test_environment.xml
        tree = ET.parse(os.path.join(self.config_file_directory, 'test_environment.xml'))
        test_environment = tree.getroot()
        environment = (test_environment[0][0].text)

        # Select Appropriate URL based on the Environment Value from above
        self.base_URL = Environments.return_environments(environment)


    def readTestfile(self, Product):

        # Determine the Test Run Type
        # Get Test Run Type Text from config file
        # tree = ET.parse(os.path.join(self.config_file_directory, 'test_environment.xml'))
        # test_environment = tree.getroot()
        # test_run_type = (test_environment[1][0].text)
        self.test_run_type_value = ''

        # If / Else to convert test_run_type text to a value
        if self.test_run_type == "Regression":
            self.test_run_type_value = '1'
        elif test_run_type == "Smoke":
            self.test_run_type_value = '2'
        elif test_run_type == "Sanity":
            self.test_run_type_value = '3'

        # Open Test Scenario Workbook; Instantiate worksheet object
        wb = xlrd.open_workbook(os.path.join( self.test_case_directory, Product + '.xlsx'))
        sh = wb.sheet_by_index(0)

        ## Begin For Loop to iterate through Test Scenarios
        i = 1
        rows = sh.nrows
        empty_cell = False
        for x in range(1, sh.nrows):

            cell_val = sh.cell(i, 0).value
            if cell_val == '':
                # If Cell Value is empty, set empty_cell to True
                empty_cell = True
            else:
                # If Cell Value is NOT empty, set empty_cell to False
                empty_cell = False

            regression_check = sh.cell_value(i, 3)
            smoke_check = sh.cell_value(i, 4)
            sanity_check = sh.cell_value(i, 5)

            # If / Else Section to check if a test needs to be run
            #### CODE NOT WORKING YET - Ken 8-2-17
            #### Program is running ALL rows & NOT skipping rows
            if self.test_run_type_value == 3 and sanity_check == "0":
                continue
            if self.test_run_type_value == 2 and smoke_check == "0":
                continue
            if self.test_run_type_value == 1 and regression_check == "0":
                continue

            # Check to see if cell is NOT empty
            # If cell is not empty, read in the values
            if empty_cell == False:
                self.test_summary = sh.cell_value(i, 0)
                self.test_scenario = sh.cell_value(i, 1)
                self.effective_date = sh.cell_value(i, 2)
                self.test_scenario_number = str(round(sh.cell_value(i, 3)))
                self.regression = sh.cell_value(i, 4)


                self.smoke = sh.cell_value(i, 5)
                self.sanity = sh.cell_value(i, 6)
                self.contract_class = sh.cell_value(i, 7)
                self.agent = sh.cell_value(i, 8)
                self.state = sh.cell_value(i, 9)
                self.revenue = str(round(sh.cell_value(i, 10)))
                self.staff_count = str(round(sh.cell_value(i, 11)))
                _OLD_scenario = sh.cell_value(i, 12)
                _OLD_scenario_number = str(round(sh.cell_value(i, 13)))

            # Else, the cell is empty
            # End the Loop
            else:
                break

            # Create "Fake" insured and company
            # state = frandom.us_state()
            # state = "California"
            # state = Create_Insured_Address.return_alabama(state_value)

            self.first_name = name.first_name()
            self.last_name = name.last_name()
            company_name = company.company_name()
            self.company_name_string = "QA Test" + " " + "-" + " " + "Dr." + " " + self.first_name + " " + self.last_name + " " + "dba" + " " + company_name
            self.address_value = address.street_address()
            self.city = StateCapitals.return_state_capital(self.state)
            self.postal_code = ZipCodes.return_zip_codes(self.state)

            # Convert effective_date value to format MM/DD/YYYY
            d = xlrd.xldate_as_tuple(int(self.effective_date), 0)
            # convert date tuple in mm-dd-yyyy format
            d = datetime.datetime(*(d[0:3]))
            self.effective_date_formatted = d.strftime("%m/%d/%Y")

            # Access XML to retrieve login credentials
            tree = ET.parse('resources.xml')
            login_credentials = tree.getroot()
            username = (login_credentials[0][0].text)
            password = (login_credentials[0][1].text)

            # NOTE: For contract_classes.py, the array count starts at 1
            # Array will be 1 - 74
            contract_class_int_value = ContractClasses_Medical.return_contract_class_values(self.contract_class)

            # Date Variables
            date_today = time.strftime("%m/%d/%Y")
            ad_hoc_effectiveDate = "09/06/2017"

            # Initialize Driver; Launch URL
            # baseURL = "https://svcdemo1.wn.nasinsurance.com/"
            driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

            # Maximize Window; Launch URL
            driver.maximize_window()
            # driver.get(baseURL)

            driver.get(self.base_URL)

            driver.implicitly_wait(3)

            self.runTests()

            i += 1
