'''
Functions to determine end date of marriage
By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import random
from datetime import datetime, timedelta

def generateMarriageEndDate(baseyear, maritalstatus, marriageduration):
    if maritalstatus == 'Married':
        end_year = int(baseyear) + int(marriageduration)
        min_year = end_year
        max_year = end_year
        try:
            start = datetime(min_year, 1, 1, 00, 00, 00)
            years = max_year - min_year + 1
            end = start + timedelta(days=365 * years)
            random_date = start + (end - start) * random.random()
            random_date = str(random_date)
            random_date = random_date[:10]
            endmarriagedate = random_date
        except:
                endmarriagedate = 'NA'
        return endmarriagedate
