'''
Function to generate deceased

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

import random

def generateDeceased (currentdate, citizen, df):
    if random.uniform(0, 1) < (citizen.lifeexpectancyprobability / 365) and citizen.alive == 1:
        citizen.alive = 0
        
        citizen.event = 'Life event: Deceased'
        mutationdate = str(currentdate)
        mutationdate = mutationdate[:10]
        
        new_event = {'Mutation date': mutationdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Couple nr': citizen.couplenr, 'Marriage duration': citizen.marriageduration, 
                     'Marriage end date': citizen.marriageenddate, 'Marriage intention': citizen.marriageintention, 
                     'Marriage age': citizen.marriageage, 'Wedding date': citizen.marriagedate, 
                     'Children': citizen.children, 'Employment status': citizen.employmentstatus, 'Income': citizen.income, 
                     'Capital': citizen.capital, 'NrChildren': citizen.nrchildren, 'Birth age': citizen.birthage, 
                     'Birthing date': citizen.birthingdate, 'Alive': citizen.alive, 'Event': citizen.event}
        
        df = df.append(new_event, ignore_index=True)
    
    return df, citizen
        