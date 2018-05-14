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

from pages.customer_center.Landing_Page.Login import Login
from pages.customer_center.Landing_Page.Account_Creation import Account_Creation
from pages.customer_center.Insured_Information.Insured_Information import Insured_Information
from pages.customer_center.PAF.PAF import PAF
from pages.customer_center.Signature.Signature import Signature
from pages.customer_center.Signature.Signature_View_Signed_Forms import Signature_View_Signed_Forms

from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes


class CreateAccount():

    def create_account_quote(self):

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
        global password
        global address_1
        global address_2
        global city
        global state
        global postal_code
        global formatted_postal_code
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
                password = sh.cell_value(i, 2)
                address_1 = sh.cell_value(i, 3)
                address_2 = sh.cell_value(i, 4)
                city = sh.cell_value(i, 5)
                state = sh.cell_value(i, 6)
                postal_code = str((sh.cell_value(i, 7)))
                revenue = str(round(sh.cell_value(i, 8)))
                effective_date = sh.cell_value(i, 9)
                online_vendor = str((sh.cell_value(i, 10)))
                merchant_id = str((sh.cell_value(i, 11)))
                positive_feedback_rating = str(round(sh.cell_value(i, 12)))
                _OLD_scenario = str((sh.cell_value(i, 13)))

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
            email_address = first_name + "." + last_name + "@" + "mailinator.com"


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
            d = xlrd.xldate_as_tuple(int(effective_date), 0)
            # convert date tuple in mm-dd-yyyy format
            d = datetime.datetime(*(d[0:3]))
            effective_date_formatted = d.strftime("%m/%d/%Y")

            # Initialize Driver; Launch URL
            # baseURL = "https://svcdemo1.wn.nasinsurance.com/"
            driver = webdriver.Chrome(os.path.join(config_file_directory, 'chromedriver.exe'))

            # Maximize Window; Launch URL
            driver.maximize_window()
            # driver.get(baseURL)

            driver.get(base_URL)

            driver.implicitly_wait(3)

            # Create New Account, Click Submit
            ac = Account_Creation(driver)
            ac.input_name_email_username_password(company_name_string, email_address, username, password )
            ac.click_submit_button()

            # Wait
            time.sleep(10)

            # Fill in Insured Information Screen
            ii = Insured_Information(driver)
            ii.fill_in_insured_information_fields(address_value, address_2, city, state, revenue)

            # Determine if Postal Code is More than 5 Characters
            # If more than 5 characters, Trim the last 2 digits; Remove '.0'
            if postal_code_string_length > 5:
                ii.fill_in_formatted_postal_code(formatted_postal_code)
            elif postal_code_string_length < 6:
                ii.fill_in_postal_code(postal_code)

            ii.click_continue_button()

            # Wait
            time.sleep(5)

            # Fill in PAF

            saw_PAF = PAF(driver)

            if test_scenario_number == "1" or test_scenario_number == "5" or test_scenario_number == "6" or test_scenario_number == "7":
                saw_PAF.create_quote_individual(online_vendor, merchant_id, date_today)
            elif test_scenario_number == "2":
                saw_PAF.create_quote_corporation(online_vendor, merchant_id, date_today)
            elif test_scenario_number == "3":
                saw_PAF.create_quote_partnership(online_vendor, merchant_id, date_today)
            elif test_scenario_number == "4":
                saw_PAF.create_quote_other(online_vendor, merchant_id, date_today)

            # Click Next on PAF Screen
            saw_PAF.click_next_button()

            # Application - Signature Screen
            s = Signature(driver)

            # Select Typed Signature
            s.select_typed()

            # Wait
            time.sleep(3)

            # Input Typed Signature
            s.input_typed_signature(signature)

            # Click Save Signature
            s.click_save_signature_button()

            # Wait
            time.sleep(3)

            # Click Next Button After Inputting Signature
            svsf = Signature_View_Signed_Forms(driver)
            svsf.click_next_button_after_inputting_signature()

            # Script Works Up to This point

            # Wait
            driver.implicitly_wait(3)

            # Write Values to CSV

            # Declare the values that will be outputted to csv
            values = [test_summary, test_scenario_number, state,company_name_string, username, password, email_address]

            # Declare Directory of csv file
            download_dir = os.path.join(test_results_directory, 'Customer_Center_Results.csv')

            # This Section Writes the output to the csv file
            with open(download_dir, "a") as f:
                writer = csv.writer(f, lineterminator='\n')  # lineterminator='\n'
                writer.writerow(values)

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