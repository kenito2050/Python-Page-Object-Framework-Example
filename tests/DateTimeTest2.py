from datetime import datetime
from datetime import timedelta
from urllib.parse import urlparse, parse_qs

# Declare Date / Time Objects

# Sets Today's Date in format dd/mm/YYYY
# checkin_date = datetime.now().strftime("%d-%m-%Y")
# print (checkin_date)
#
# # Using Today's Date, Adds 7 Days
# checkout_date = datetime.now() + timedelta(days=7)
# print(checkout_date)
#
# # Format's checkout date in format dd/mm/YYYY
# checkout_date_new_format = checkout_date.strftime("%d-%m-%Y")
# print (checkout_date_new_format)
#
# current_date = datetime.now().strftime("%m-%d-%Y")
# print (current_date)

# test_url = 'https://proddev.wn.nasinsurance.com/index.php?c=saw.application.primary&app_id=12169'
# parsed_string = urlparse(test_url)
# query_string = parsed_string.query
# last_five_digits = query_string[-5:]
#
# print (test_url)
# print (parsed_string)
# print (query_string)
# print(last_five_digits)

# state_value = "Alabama"
# # return state_value
# print(state_value)

# This code retrieves the app_id value from a URL string
# This code WORKS
test_url = 'https://proddev.wn.nasinsurance.com/index.php?c=saw.application.primary&app_id=12169'
#current_url = self.driver.current_url()
parts = urlparse(test_url)
print (parts)
query_dict = parse_qs(parts.query)
print(query_dict)
print(query_dict['app_id'][0])
