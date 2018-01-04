import datetime
import os
import time
import unittest
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

import xlrd
from faker import address
from faker import company
from faker import name
from selenium import webdriver

from pages.customer_center.Landing_Page.Login import Login
from pages.customer_center.Landing_Page.Account_Creation import Account_Creation
from pages.customer_center.Insured_Information.Insured_Information import Insured_Information

from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes


class CreateAccount():

    def create_account(self):

        Product = "MMTM_Customer_Center"

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        # Determine the Test Run Type
        # Get Test Run Type Text from config file
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment = tree.getroot()
        test_run_type = (test_environment[1][0].text)

        global test_summary
        global test_scenario_number
        global test_scenario
        global password
        global address_1
        global address_2
        global city
        global state
        global postal_code
        global revenue
        global effective_date
        global online_vendor
        global merchant_id
        global positive_feedback_rating
        global _OLD_scenario

        # Open Test Scenario Workbook; Instantiate worksheet object
        # 0 - First Worksheet
        # 1 - Second Worksheet...etc

        wb = xlrd.open_workbook(os.path.join(test_case_directory, Product + '.xlsx'))
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

            # Check to see if cell is NOT empty
            # If cell is not empty, read in the values
            if empty_cell == False:
                test_summary = sh.cell_value(i, 0)
                test_scenario_number = str(round(sh.cell_value(i, 1)))
                test_scenario = sh.cell_value(i, 2)
                password = sh.cell_value(i, 3)
                address_1 = sh.cell_value(i, 4)
                address_2 = sh.cell_value(i, 5)
                city = sh.cell_value(i, 6)
                state = sh.cell_value(i, 7)
                postal_code = str(round(sh.cell_value(i, 8)))
                revenue = str(round(sh.cell_value(i, 9)))
                effective_date = sh.cell_value(i, 10)
                online_vendor = str((sh.cell_value(i, 11)))
                merchant_id = str((sh.cell_value(i, 12)))
                positive_feedback_rating = str(round(sh.cell_value(i, 13)))
                _OLD_scenario = str((sh.cell_value(i, 14)))

            # Else, the cell is empty
            # End the Loop
            else:
                break

            ## Determine Test Environment to run scripts

            ## Read in value from test_environment.xml
            tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
            test_environment = tree.getroot()
            environment = (test_environment[0][0].text)

            ## Select Appropriate URL based on the Environment Value from above
            base_URL = Environments.return_environments(environment)

            # Data Generator Section

            # Create Name
            first_name = name.first_name()
            first_name_initial = first_name[:1]
            last_name = name.last_name()
            company_name = company.company_name()
            # company_name_string = company_name
            company_name_string = "QA Test" + " " + "-" + " " + " " + first_name + " " + last_name + " " + "dba" + " " + company_name


            # Create Email Address
            # Take First Character of First Name + . + Last Name String + Mailinator.com
            # Example: John User
            # Becomes: J.User@mailinator.com
            email_address = first_name_initial + "." + last_name + "@" + "mailinator.com"


            # Create Username
            # Take First Character of First Name + . + Last Name String
            # Example: John User
            # Becomes: J.User
            username = first_name_initial + "." + last_name

            # Address Generation
            # This Section Creates values for the Address Fields
            # Only Valid Values are generated based off of the State Value
            address_value = address.street_address()
            # city = StateCapitals.return_state_capital(state)
            # postal_code = ZipCodes.return_zip_codes(state)

            # Date Variables
            date_today = time.strftime("%m/%d/%Y")
            ad_hoc_effectiveDate = "09/06/2017"

            # Convert effective_date value to format MM/DD/YYYY
            d = xlrd.xldate_as_tuple(int(effective_date), 0)
            # convert date tuple in mm-dd-yyyy format
            d = datetime.datetime(*(d[0:3]))
            effective_date_formatted = d.strftime("%m/%d/%Y")

            # Initialize Driver; Launch URL
            # baseURL = "https://svcdemo1.wn.nasinsurance.com/"
            driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

            # Maximize Window; Launch URL
            driver.maximize_window()
            # driver.get(baseURL)

            driver.get(base_URL)

            driver.implicitly_wait(3)

            # Create New Account, Click Submit
            ac = Account_Creation(driver)
            ac.input_name_email_username_password(company_name_string, email_address, username, password)
            ac.click_submit_button()

            # Fill in Insured Information Screen
            ii = Insured_Information(driver)
            ii.fill_in_insured_information_fields(address_value, address_2, city, state, postal_code, revenue)
            ii.click_continue_button()

            # Script Works Up to This point

            # Wait
            driver.implicitly_wait(3)

            # Close Browser
            driver.quit()

            i += 1

ca = CreateAccount()
ca.create_account()