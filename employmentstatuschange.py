'''
Function to generate the life event of
entering into adulthood

By Dr. Raymond Hoogendoorn
Copyright 2020
'''
from numpy.random import choice

def changeEmploymentStatus(currentdate, age, birthdate, citizen, df, employmentstatusprobability):
    elements = ['Permanent contract', 'Flexible contract', 'Entrepreneur without personnel',
                'Entrepreneur with personel', 'Family business', 'Unknown', 'Unemployed']
    currentday = str(currentdate)
    birthday = str(birthdate)
    currentday = currentday[5:10]
    birthday = birthday[5:10]
    if currentday == birthday and age == 15:
        citizen.employmentstatus = choice(elements, p = employmentstatusprobability)
        citizen.event = 'Changed employment status'
        new_event = {'Mutation date': currentdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income,
                     'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
        
    if currentday == birthday and age == 67:
        citizen.employmentstatus = 'Retired'
        citizen.event = 'Changed employment status'
        new_event = {'Mutation date': currentdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income,
                     'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
    
    return df, citizen
        
        