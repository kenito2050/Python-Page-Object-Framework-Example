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
import xlwt
from glob import glob
from xlrd import open_workbook
import pandas as pd
from pandas import np

from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.client_contact_page import ClientContact

# Begin Generic SAW Pages
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods

##### CHANGE THESE VALUES WHEN CREATING A NEW PRODUCT
# Begin Product Specific Pages - SAW Pages
from pages.producer_center.saw.products.NGP_CAMICO.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.NGP_CAMICO.PAF.PAF import PAF
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.PCI_50k_coverage_options import \
    PCI_50k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.PCI_100k_coverage_options import \
    PCI_100k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.No_PCI_50k_coverage_options import \
    No_PCI_50k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.No_PCI_100k_coverage_options import \
    No_PCI_100k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.select_option.select_option import Select_Option

# Continue Generic SAW Pages
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.producer_center.saw.summary import Summary
from pages.service_center.agents_page import AgentsPage
from pages.service_center.applications_page import ApplicationsPage
from pages.service_center.application_screens.application_screens import Application_Screens
from pages.service_center.application_screens.details import App_Details
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from pages.service_center.policies_page import PoliciesPage
from pages.service_center.policy_screens.policy_screens import Policy_Screens
from pages.service_center.policy_screens.details import Details
from pages.service_center.agent_screens.agent_details import Agent_Details
from pages.service_center.policy_screens.effective_periods import Effective_Periods
from pages.service_center.subjectivities import Subjectivities
from utilities.Environments.Environments import Environments
from utilities.contract_classes.contract_classes import ContractClasses
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes


Product = "MEDEMD"

## Directory Locations

tests_directory = os.path.abspath(os.pardir)
framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
test_results_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

# print(tests_directory)
# print(framework_directory)
# print(config_file_directory)
# print(test_case_directory)
# print(test_results_directory)

## Open Test Scenario Workbook; Instantiate worksheet object
wb = xlrd.open_workbook(os.path.join(test_case_directory, Product + '.xlsx'))
sh = wb.sheet_by_index(0)

### Convert values in worksheet to a List
# list = []
# for row in range (1, sh.nrows):
#     for col in range (0, sh.ncols):
#         list.append(sh.cell_value(row, col))
# print (len(list))

i=1
# rows = sh.nrows
empty_cell = False
for x in range(1, sh.nrows):

    cell_val= sh.cell(i, 0).value
    if cell_val== '':
        # If Cell Value is empty, set empty_cell to True
        empty_cell = True
    else:
        # If Cell Value is NOT empty, set empty_cell to False
        empty_cell = False

    # Check to see if cell is NOT empty
    # If cell is not empty, read in the values
    if empty_cell == False:

        test_scenario_number = str(round(sh.cell_value(i, 0)))
        test_scenario = sh.cell_value(i, 1)
        regression = sh.cell_value(i, 2)
        smoke = sh.cell_value(i, 3)
        sanity = sh.cell_value(i, 4)
        pci_dss = sh.cell_value(i, 5)
        contract_class = sh.cell_value(i, 6)
        agent = sh.cell_value(i, 7)
        state = sh.cell_value(i, 8)
        revenue = str(round(sh.cell_value(i, 9)))
        staff_count = str(round(sh.cell_value(i, 10)))

        print(test_scenario_number, test_scenario, regression, smoke, sanity, pci_dss, agent, state, revenue,
              staff_count)

        i +=1

    # Else, the cell is empty
    # End the Loop
    else:
        break


print ("This is the end of the loop")

# Iterate through spreadsheet
# i = 1
# while sh.cell(i, 5).value != 0:
#     test_scenario_number = sh.cell_value(i, 0)
#     test_scenario = sh.cell_value(i, 1)
#     agent = sh.cell_value(i, 2)
#     state = sh.cell_value(i, 3)
#     revenue = sh.cell_value(i, 4)
#     staff_count = sh.cell_value(i, 5)
#
#     print (test_scenario_number, test_scenario, agent, state, revenue, staff_count)
#     i += 1
#     print (i)
#
# print ("This is the end of the loop")


# Iterate through spreadsheet
# Get number of rows
# rows = sh.nrows
# i = 1
# while rows > i:
# test_scenario_number = str(round(sh.cell_value(i, 0)))
# test_scenario = sh.cell_value(i, 1)
# regression = sh.cell_value(i, 2)
# smoke = sh.cell_value(i, 3)
# sanity = sh.cell_value(i, 4)
# pci_dss = sh.cell_value(i, 5)
# contract_class = sh.cell_value(i, 6)
# agent = sh.cell_value(i, 7)
# state = sh.cell_value(i, 8)
# revenue = str(round(sh.cell_value(i, 9)))
# staff_count = str(round(sh.cell_value(i, 10)))
#
#     print (round(test_scenario_number), test_scenario, agent, state, round(revenue), round(staff_count))
#     i += 1
#     print (i)
#
# print ("This is the end of the loop")

