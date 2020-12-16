'''
Function to generate the life event of
entering into adulthood

By Dr. Raymond Hoogendoorn
Copyright 2020
'''
from numpy.random import choice
from random import randint

def changeEmploymentStatus(currentdate, age, birthdate, citizen, df, employmentstatusprobability, incomeprobability):
    elements = ['Permanent contract', 'Flexible contract', 'Entrepreneur without personnel',
                'Entrepreneur with personel', 'Family business', 'Unknown', 'Unemployed']
    
    elements_2 = range(0,8)
    min_range = [0, 10000, 20000, 30000, 40000, 50000, 100000, 200000]
    max_range = [10000, 20000, 30000, 40000, 50000, 100000, 200000, 500000]

    
    currentday = str(currentdate)
    birthday = str(birthdate)
    currentday = currentday[5:10]
    birthday = birthday[5:10]
    
    if currentday == birthday and age == 15 and citizen.alive ==  1:
        citizen.employmentstatus = choice(elements, p = employmentstatusprobability)
        
        incomeclass = choice(elements_2, p = incomeprobability)
        min_income = min_range[incomeclass]
        max_income = max_range[incomeclass]
        income = randint(min_income, max_income)
        
        citizen.income = income
        
        citizen.event = 'Changed employment status and income'
        mutationdate = str(currentdate)
        mutationdate = mutationdate[:10]
        new_event = {'Mutation date': mutationdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Marriage intention': citizen.marriageintention, 'Marriage age': citizen.marriageage,
                     'Wedding date': citizen.marriagedate, 'Children': citizen.children,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income, 'Capital': citizen.capital, 
                     'NrChildren': citizen.nrchildren, 'Birth age': citizen.birthage, 
                     'Birthing date': citizen.birthingdate, 'Alive': citizen.alive, 
                     'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
        
    if currentday == birthday and age == 67 and citizen.alive == 1:
        citizen.employmentstatus = 'Retired'
        citizen.income = citizen.income * 0.70
        citizen.event = 'Changed employment status and income'
        mutationdate = str(currentdate)
        mutationdate = mutationdate[:10]
        new_event = {'Mutation date': mutationdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Marriage intention': citizen.marriageintention, 'Marriage age': citizen.marriageage,
                     'Wedding date': citizen.marriagedate, 'Children': citizen.children,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income,
                     'NrChildren': citizen.nrchildren, 'Birth age': citizen.birthage, 
                     'Birthing date': citizen.birthingdate, 'Alive': citizen.alive, 
                     'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
    
    return df, citizen
        