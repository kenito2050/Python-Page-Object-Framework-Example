class ZipCodes(dict):

    def return_zip_codes(state):

        # Data Dictionary of Zip Codes
        zip_codes={
            'Alabama': '36101',  #Montgomery
            'Alaska': '99801',   #Juneau
            'Arizona': '85001',  #Phoenix
            'Arkansas': '72201', #Little Rock
            'California': '94203',#Sacramento
            'Colorado': '80123',#Denver
            'Connecticut': '06101',#Hartford
            'Delaware': '19901',#Dover
            'Florida': '32301',#Tallahassee
            'Georgia': '30301',#Atlanta
            'Hawaii': '96813',#Honolulu
            'Idaho': '83701',#Boise
            'Illinois': '62701',#Springfield
            'Indiana': '46201',#Indianapolis
            'Iowa': '50301',#Des Moines
            'Kansas': '66601',#Topeka
            'Kentucky': '40601',#Frankfort
            'Louisiana': '70801',#Baton Rouge
            'Maine': '03901',#Augusta
            'Maryland': '21401',#Annapolis
            'Massachusetts': '02445',#Boston
            'Michigan': '48901',#Lansing
            'Minnesota': '55101',#St. Paul
            'Mississippi': '39201',#Jackson
            'Missouri': '65101',#Jefferson City
            'Montana': '59601',#Helena
            'Nebraska': '68501',#Lincoln
            'Nevada': '89701',#Carson City
            'New Hampshire': '03301',#Concord
            'New Jersey': '08601',#Trenton
            'New Mexico': '87501',#Santa Fe
            'New York': '12201',#Albany
            'North Carolina': '27601',#Raleigh
            'North Dakota': '58501',#Bismarck
            'Ohio': '43085',#Columbus
            'Oklahoma': '73101',#Oklahoma City
            'Oregon': '97301',#Salem
            'Pennsylvania': '17101',#Harrisburg
            'Rhode Island': '02901',#Providence
            'South Carolina': '29201',#Columbia
            'South Dakota': '57501',#Pierre
            'Tennessee': '37115',#Nashville
            'Texas': '73301',#Austin
            'Utah': '84101',#Salt Lake City
            'Vermont': '05601',#Montpelier
            'Virginia': '23218',#Richmond
            'Washington': '98501',#Olympia
            'West Virginia': '25301',#Charleston
            'Wisconsin': '53705',#Madison
            'Wyoming': '82001',#Cheyenne
            }
        return zip_codes[state]