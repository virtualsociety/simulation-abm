'''
Function to create new marriages

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from marriagedurationprobability import calculateMarriageDurationProbability
from marriageduration import generateMarriageDuration
from marriageenddate import generateMarriageEndDate

def generateNewMarriages(currentdate, citizen, df, df_marriageduration):
    currentday = str(currentdate)
    currentday = currentday[:10]
    currentyear = currentday[:4]
    weddingday = str(citizen.marriagedate)
    if currentday == weddingday and citizen.alive == 1:
        citizen.maritalstatus = 'Married'
        
        citizen.event = 'Life event: Married'
        mutationdate = str(currentdate)
        mutationdate = mutationdate[:10]
        
        marriagedurationprobability = calculateMarriageDurationProbability(df_marriageduration, currentyear)
        citizen.marriageduration = generateMarriageDuration(marriagedurationprobability, citizen.maritalstatus)
        
        citizen.marriageenddate = generateMarriageEndDate(currentyear, citizen.maritalstatus, citizen.marriageduration)
        
        new_event = {'Mutation date': mutationdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Couple nr': citizen.couplenr, 'Marriage duration': citizen.marriageduration, 
                     'Marriage end date': citizen.marriageenddate, 'Marriage intention': citizen.marriageintention, 
                     'Marriage age': citizen.marriageage, 'Wedding date': citizen.marriagedate, 
                     'Children': citizen.children, 'Employment status': citizen.employmentstatus, 'Income': citizen.income, 
                     'Capital': citizen.capital, 'NrChildren': citizen.nrchildren, 'Birth age': citizen.birthage, 
                     'Alive': citizen.alive, 'Event': citizen.event}
        
        df = df.append(new_event, ignore_index=True)
        
    return df, citizen

    
    