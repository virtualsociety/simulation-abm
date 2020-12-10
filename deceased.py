'''
Function to generate deceased citizens

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import random

def generateDeceased(currentdate, alive, lifeexpectancy, citizen, df):
    
    deceasedrandom = random.uniform(0,1)
    lifeexpectancy_day = lifeexpectancy/365
    
    if deceasedrandom <= lifeexpectancy_day and alive == 1:
        citizen.alive = 0
        citizen.event = 'Deceased'
        new_event = {'Mutation date': currentdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income,
                     'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
    
    return df, citizen