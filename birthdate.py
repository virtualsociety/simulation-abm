'''
Functions to determine the birthday of citizens
By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import random
from datetime import datetime, timedelta

def generateBirthdate(baseyear, age):
    birth_year = (baseyear) - int(age)
    min_year = birth_year
    max_year = birth_year
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
    
        
        
    