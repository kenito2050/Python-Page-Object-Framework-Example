import csv
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

from pages.retailer_access.Landing_Page.Account_Creation import Account_Creation

from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes


class CreateAccount():

    def create_account_quote(self):

        Product = "Agent_Registration"

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        global test_summary
        global test_scenario
        global registration_code
        global email_address
        global company_name_excel
        global title
        global address_1
        global address_2
        global city
        global state
        global postal_code
        global phone
        global preferred_wholesaler

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
                test_scenario = str(round(sh.cell_value(i, 1)))
                registration_code = sh.cell_value(i, 2)
                email_address = sh.cell_value(i, 3)
                company_name_excel = sh.cell_value(i, 4)
                title = sh.cell_value(i, 5)
                address_1 = sh.cell_value(i, 6)
                address_2 = sh.cell_value(i, 7)
                city = sh.cell_value(i, 8)
                state = sh.cell_value(i, 9)
                postal_code = str((sh.cell_value(i, 10)))
                phone = sh.cell_value(i, 11)
                preferred_wholesaler = sh.cell_value(i, 12)

            # Else, the cell is empty
            # End the Loop
            else:
                break

            ## Determine Test Environment to run scripts

            ## Read in value from test_environment.xml
            tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
            test_environment = tree.getroot()
            environment = (test_environment[2][0].text)

            ## Select Appropriate URL based on the Environment Value from above
            base_URL = Environments.return_environments(environment)

            # Data Generator Section

            # Create Name
            first_name = name.first_name()
            first_name_initial = first_name[:1]
            last_name = name.last_name()
            company_name = company.company_name()
            # company_name_string = company_name
            company_name_faker = "QA Test" + " " + "-" + " " + first_name_initial + " " + last_name

            # old company name
            # company_name_faker = "QA Test" + " " + "-" + " " + "Dr." + " " + first_name + " " + last_name + " " + "dba" + " " + company_name


            # Create Email Address
            # Take First Character of First Name + . + Last Name String + Mailinator.com
            # Example: John User
            # Becomes: J.User@mailinator.com
            email_address = first_name_initial + "." + last_name + "@" + "mailinator.com"


            # Create Username
            # Take First Character of First Name + . + Last Name String
            # Example: John User
            # Becomes: J.User
            username = first_name + "." + last_name

            # Create Signature
            # Concatenate First Name + Last Name
            signature = first_name + " " + last_name

            # Address Generation
            # This Section Creates values for the Address Fields
            # Only Valid Values are generated based off of the State Value
            address_value = address.street_address()
            # city = StateCapitals.return_state_capital(state)
            # postal_code = ZipCodes.return_zip_codes(state)

            # Format the Postal Code
            # If Postal Code ends in '.0', remove that substring
            # Store the value in a new variable formatted_postal_code
            postal_code_string_length = len(postal_code)
            if postal_code_string_length > 5:
                formatted_postal_code = postal_code[:-2]

            # Date Variables
            date_today = time.strftime("%m/%d/%Y")
            ad_hoc_effectiveDate = "09/06/2017"

            # Convert effective_date value to format MM/DD/YYYY
            # d = xlrd.xldate_as_tuple(int(effective_date), 0)
            # # convert date tuple in mm-dd-yyyy format
            # d = datetime.datetime(*(d[0:3]))
            # effective_date_formatted = d.strftime("%m/%d/%Y")

            # Initialize Driver; Launch URL
            # baseURL = "https://svcdemo1.wn.nasinsurance.com/"
            driver = webdriver.Chrome(os.path.join(config_file_directory, 'chromedriver.exe'))

            # Maximize Window; Launch URL
            driver.maximize_window()
            # driver.get(baseURL)

            driver.get(base_URL)

            driver.implicitly_wait(3)

            # Retailer Access Site
            ac = Account_Creation(driver)

            # Test Scenarios
            # 1 - Retailer, USI / HUB, No Custom Registration Code
            # 2 - Retailer, Not USI / HUB, No Custom Registration Code
            # 3 - Wholesaler
            # 4 - Custom Registration Code "GREENBACKS"

            if test_scenario == "1":
                ac.click_custom_registration_code_no()
                ac.select_retail_agency_type()
                ac.fill_in_first_last_name_email_address_city_zip_phone(first_name, last_name, email_address, address_value, city, formatted_postal_code, phone)
                ac.input_title(title)
                ac.select_state(state)
                ac.input_company_name_FAKER(company_name_faker)
                ac.select_preferred_wholesaler(preferred_wholesaler)

            elif test_scenario == "2":
                ac.click_custom_registration_code_no()
                ac.select_retail_agency_type()
                ac.fill_in_first_last_name_email_address_city_zip_phone(first_name, last_name, email_address, address_value, city, formatted_postal_code, phone)
                ac.input_title(title)
                ac.select_state(state)
                ac.input_company_name_EXCEL(company_name_excel)

            elif test_scenario == "3":
                ac.click_custom_registration_code_no()
                ac.select_wholesale_agency_type()
                ac.fill_in_first_last_name_email_address_city_zip_phone(first_name, last_name, email_address, address_value, city, formatted_postal_code, phone)
                ac.input_title(title)
                ac.select_state(state)
                ac.input_company_name_FAKER(company_name_faker)

            elif test_scenario == "4":
                ac.click_custom_registration_code_yes()
                ac.input_registration_code(registration_code)
                ac.fill_in_first_last_name_email_address_city_zip_phone(first_name, last_name, email_address, address_value, city, formatted_postal_code, phone)
                ac.input_title(title)
                ac.select_state(state)
                ac.input_company_name_FAKER(company_name_faker)

                ac.click_send_button()

            # Wait
            time.sleep(3)

            # Script Works Up to This point

            # Wait
            driver.implicitly_wait(3)

            # Write Values to CSV

            # Declare the values that will be outputted to csv
            if test_scenario == "1" or test_scenario == "3" or test_scenario == "4":
                scenario_1_3_4_values = [test_summary, company_name_faker, city, city, formatted_postal_code, preferred_wholesaler, registration_code]

                # Declare Directory of csv file
                download_dir = os.path.join(test_results_directory, 'Retail_Access_Results.csv')

                # This Section Writes the output to the csv file
                with open(download_dir, "a") as f:
                    writer = csv.writer(f, lineterminator='\n')  # lineterminator='\n'
                    writer.writerow(scenario_1_3_4_values)

            elif test_scenario == "2":
                scenario_2_values = [test_summary, company_name_excel, city, city, formatted_postal_code, preferred_wholesaler, registration_code]

                # Declare Directory of csv file
                download_dir = os.path.join(test_results_directory, 'Retail_Access_Results.csv')

                # This Section Writes the output to the csv file
                with open(download_dir, "a") as f:
                    writer = csv.writer(f, lineterminator='\n')  # lineterminator='\n'
                    writer.writerow(scenario_2_values)

            # # Declare the values that will be outputted to csv
            # values = [test_summary, test_scenario_number, state,company_name_string, username, password, email_address]
            #
            # # Declare Directory of csv file
            # download_dir = os.path.join(test_results_directory, 'Customer_Center_Results.csv') # where you want the file to be downloaded to
            #
            # with open(download_dir, "w") as f:
            #
            #     writer = csv.writer(f)
            #     # writer.writerow({'Test Summary' : test_summary, 'Test Scenario' : test_scenario_number, 'State' : state, 'Insured' : company_name_string, 'Username' : username, 'password' : password, 'Email Address' :email_address })
            #     writer.writerow(values)

            # Close Browser
            driver.quit()

            i += 1

ca = CreateAccount()
ca.create_account_quote()