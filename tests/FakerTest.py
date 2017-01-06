from faker import address
from faker import company
from faker import frandom
from datetime import date
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes

class FakerTest():

    def faker_test(self):

        # Create "Fake" Variables
        first_name = "Test"
        last_name = "Customer"
        state = frandom.us_state()
        company_name = company.company_name()
        company_name_string = company_name + " " + "-" + " " + state + " " + "Test"
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        # Instantiate Year and Month Variables
        expiration_year = date.today().year + 1
        expiration_month_integer = date.today().month
        expiration_month_name = date(1900, expiration_month_integer, 1).strftime('%B')

        print(first_name + " " + last_name + " " + "from" + " " + city + "," + " " + state)
        print(company_name)
        print(company_name_string)
        print(address_value)
        print(city)
        print(state)
        print(postal_code)
        print(expiration_year)
        print(expiration_month_name)

ft = FakerTest()
ft.faker_test()