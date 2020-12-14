'''
Function to generate the wedding data

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import random
from datetime import datetime, timedelta

def generateWeddingDate(baseyear, marriageage, age):
    if marriageage != None:
        wedding_year = (baseyear) + (marriageage - age)
        min_year = wedding_year
        max_year = wedding_year
        if (marriageage - age) >= 0:
            try:
                start = datetime(min_year, 1, 1, 00, 00, 00)
                years = max_year - min_year + 1
                end = start + timedelta(days= 365 * years)
                random_date = start + (end - start) * random.random()
                random_date = str(random_date)
                random_date = random_date[:10]
                return random_date
            except:
                return None