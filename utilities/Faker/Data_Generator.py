from faker import address
from faker import company
from faker import name

class Data_Generator():

    def create_full_company_name(company_name):

        first_name = name.first_name()
        last_name = name.last_name()
        company_name_string = company.company_name()
        full_company_name = "QA Test" + " " + "-" + " " + first_name + " " + last_name + " " + "DBA" + " " + company_name_string

        return full_company_name

    def create_street_address(address_string):

        address_value = address.street_address()
        return address_value