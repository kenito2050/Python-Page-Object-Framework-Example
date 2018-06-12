import csv
import unittest
import os
from xml.etree import ElementTree as ET

import xlrd
from faker import address
from faker import company
from faker import name
from selenium import webdriver

from pages.producer_center.ballpark.ballpark_Indication import BallPark_Indication
from pages.producer_center.ballpark.ballpark_PAF import BallPark_PAF
from pages.producer_center.ballpark.ballpark_download_send import BallPark_Download_Send
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.service_center.agents_page import AgentsPage
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from utilities.contract_classes.contract_classes_Medical import ContractClasses_Medical
from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes
import time


class CreateQuote():

    def test_login_search_for_agent_create_quote(self):

        Product = "CYB_MDA_BALLPARK"

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(
            os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        ## Determine Test Environment to run scripts

        ## Read in value from test_environment.xml
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment  = tree.getroot()
        environment =(test_environment[0][0].text)

        global test_summary
        global test_scenario
        global effective_date
        global contract_class
        global agent
        global state
        global postal_code
        global broker
        global staff_count
        global _OLD_scenario
        global _OLD_scenario_number

        # Open Test Scenario Workbook; Instantiate worksheet object
        wb = xlrd.open_workbook(os.path.join(test_case_directory, Product + '.xlsx'))
        sh = wb.sheet_by_index(1)

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
                effective_date = sh.cell_value(i, 2)
                contract_class = sh.cell_value(i, 3)
                agent = sh.cell_value(i, 4)
                state = sh.cell_value(i, 5)
                postalcode = (sh.cell_value(i, 6))
                broker = sh.cell_value(i, 7)
                staff_count = str(round(sh.cell_value(i, 8)))
                _OLD_scenario = sh.cell_value(i, 9)
                _OLD_scenario_number = str(round(sh.cell_value(i, 10)))

            # Else, the cell is empty
            # End the Loop
            else:
                break

        ## Select Appropriate URL based on the Environment Value from above
        baseURL  = Environments.return_environments(environment)

        # Create "Fake" Variables
        #state = frandom.us_state()
        # state = "North Carolina"
        #state = Create_Insured_Address.return_alabama(state_value)
        first_name = name.first_name()
        last_name = name.last_name()
        company_name = company.company_name()
        #company_name_string = company_name
        company_name_string = "QA Ballpark Test" + " " + "-" + " " + "Dr." + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        # str_post_code = str(postal_code)
        # n = len(str_post_code)
        # if n < 5:
        #     s = "0"
        #     for i in range(1, 5 - n):
        #         s += "0"
        # appended_postal_code = "0" + postal_code

        # Access XML to retrieve login credentials
        tree = ET.parse(os.path.join(config_file_directory, 'resources.xml'))
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[1][1].text)

        # Access XML to retrieve the agent to search for
        # tree = ET.parse(os.path.join(config_file_directory, 'Agents.xml'))
        # agents = tree.getroot()
        # agent = (agents[5][0].text)

        # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
        # Access XML to retrieve contract_class

        # NOTE: For XML, the array count starts at 0
        # I have inserted a placeholder element at 0 -- Ken
        # Array will be 1 - 74
        # For List of Contract Classes, See Contract_Classes.xml
        # tree = ET.parse(os.path.join(config_file_directory, 'Contract_Classes_Medical.xml'))
        # contract_classes_XML = tree.getroot()
        # contract_class = (contract_classes_XML[0][1].text)
        # Contract Class - 1 - Medical Group
        # Contract Class - 2 - Office of Physician
        # Contract Class - 3 - Office of Dentists

        # NOTE: For contract_classes.py, the array count starts at 1
        # Array will be 1 - 74
        # contract_class_int_value = ContractClasses_Medical.return_contract_class_values(contract_class)

        # To Debug, contract_class, uncomment the next line; set value to an integer from the utilities.contract_classes.py class
        #contract_class_value = "74"

        date_today = time.strftime("%m/%d/%Y")
        ad_hoc_effectiveDate = "07/01/2017"

        # Initialize Driver; Launch URL
        # baseURL = "https://svcrel.wn.nasinsurance.com/"
        driver = webdriver.Chrome(os.path.join(config_file_directory, 'chromedriver.exe'))

        # Maximize Window; Launch URL
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Call Login methods from Pages.home.login_page.py
        lp = LoginPage(driver)
        lp.login(username, password)
        lp.click_login_button()
        nb = NavigationBar(driver)
        nb.click_agents()
        ap = AgentsPage(driver)
        ap.search_for_agent(agent)
        ap.click_submit_new_application_as_agent()
        pp = ProductsAndPrograms(driver)
        pp.click_ballpark()

        bp_PAF = BallPark_PAF(driver)
        bp_PAF.switch_windows()

        # if n < 5:
        #     bp_PAF.start_ballpark_enter_faker_company_name_valid_zip(company_name_string, appended_postal_code)
        # elif n == 5:
        #     bp_PAF.start_ballpark_enter_faker_company_name_valid_zip(company_name_string, postal_code)

        bp_PAF.start_ballpark_enter_faker_company_name_valid_zip(company_name_string, postal_code)
        bp_PAF.select_contract_class(contract_class)
        bp_PAF.click_ballpark_button()

        bp_PAF.select_CYB_MDA()
        time.sleep(3)

        # Enter Ad Hoc Effective Date
        # bp_PAF.enter_effective_date(ad_hoc_effectiveDate)

        # Enter Today's Date as Effective Date
        bp_PAF.enter_current_date(date_today)

        time.sleep(3)
        bp_PAF.click_doctor_count_field()
        bp_PAF.enter_doctor_count(staff_count)
        bp_PAF.click_ballpark_button()

        bp_Indication = BallPark_Indication(driver)
        bp_Indication.click_Download_Send_Indication()

        bp_Download_Send = BallPark_Download_Send(driver)
        bp_Download_Send.input_email()
        bp_Download_Send.click_send_email()

        # Close Ballpark Window
        driver.close()

        # Switch to First Window (Service Center)
        driver.switch_to.window(driver.window_handles[0])

        # Close First Window (Service Center)
        #driver.close()

        # Wait
        driver.implicitly_wait(3)

        # Write Values to CSV

        # Declare the values that will be outputted to csv
        values = [test_summary, company_name_string]

        # Declare Directory of csv file
        download_dir = os.path.join(test_results_directory, 'Regressions', Product + '_Regression_Test_Results.csv')

        # This Section Writes the output to the csv file
        with open(download_dir, "a") as f:
            writer = csv.writer(f, lineterminator='\n')  # lineterminator='\n'
            writer.writerow(values)

        # Declare the values that will be outputted to csv
        values = [test_summary, company_name_string]

        # Declare Directory of csv file
        download_dir = os.path.join(test_results_directory, 'Regressions',
                                    Product + '_Regression_Test_Results.csv')  # where you want the file to be downloaded to

        with open(download_dir, "w") as f:

            writer = csv.writer(f)
            writer.writerow(
                {'Test Summary': test_summary, 'Insured': company_name_string})
            writer.writerow(values)

        # Close Browser
        driver.quit()

cq = CreateQuote()
cq.test_login_search_for_agent_create_quote()