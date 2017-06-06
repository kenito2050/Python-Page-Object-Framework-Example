from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from urllib.parse import urlparse, parse_qs

# Intialize Time Variables
# This Year
now = datetime.now()
# Last Year
last_year = datetime.now() - relativedelta(years=1)

current_year = now.year
previous_year = last_year.year

#
current_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
date_plus_4_days = datetime.now() + relativedelta(days=4)

month = date_plus_4_days.strftime('%B')
day = date_plus_4_days.strftime('%d')
year = date_plus_4_days.strftime('%Y')