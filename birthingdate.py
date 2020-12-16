'''
Function to generate the birthing date

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import random
from datetime import datetime, timedelta

def generateBirthingDate(baseyear, age, birthingage):
    if birthingage != None:
        birthing_year = (baseyear) + int(birthingage - age)
        if birthing_year < baseyear:
            birthing_year = baseyear
        min_year = birthing_year
        max_year = birthing_year
        try:
            start = datetime(min_year, 1, 1, 00, 00, 00)
            years = max_year - min_year + 1
            end = start + timedelta(days=365 * years)
            random_date = start + (end - start) * random.random()
            random_date = str(random_date)
            random_date = random_date[:10]
            return random_date
        except:
            return 'NA'
    else:
        return 'NA'