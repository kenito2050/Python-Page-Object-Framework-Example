from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

class Date_Time_Generator:

    def return_date_today(self):
        date_today = time.strftime("%m/%d/%Y")
        return date_today

    def return_current_year(self):
        now = datetime.now()
        year_current = now.year
        return year_current

    def return_last_year(self):
        # This Year
        now = datetime.now()
        # Last Year
        last_year_unformatted = datetime.now() - relativedelta(years=1)
        last_year_formatted = last_year_unformatted.strftime('%Y')
        return last_year_formatted

    def return_expiration_day(self):

        # This Year
        now = datetime.now()

        # Last Year
        last_year = datetime.now() - relativedelta(years=1)

        # Find Current Date and Add 4 days
        current_date_plus_4_days = datetime.now() + relativedelta(days=4)

        expir_day = current_date_plus_4_days.strftime('%d').lstrip('0')

        return expir_day

    def return_expiration_month(self):

        # This Year
        now = datetime.now()

        # Last Year
        last_year = datetime.now() - relativedelta(years=1)

        # Find Current Date and Add 4 days
        current_date_plus_4_days = datetime.now() + relativedelta(days=4)

        expir_month = current_date_plus_4_days.strftime('%B')

        return expir_month


    def return_expiration_year(self):

        # This Year
        now = datetime.now()

        # Last Year
        last_year = datetime.now() - relativedelta(years=1)

        # Find Current Date and Add 4 days
        current_date_plus_4_days = datetime.now() + relativedelta(days=4)

        expir_year = current_date_plus_4_days.strftime('%Y')

        return expir_year