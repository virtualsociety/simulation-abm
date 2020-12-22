'''
Function to create new marriages

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from marriagedurationprobability import calculateMarriageDurationProbability
from marriageduration import generateMarriageDuration
from marriageenddate import generateMarriageEndDate

def generateNewMarriages(currentdate, citizen, df, df_marriageduration, objs):
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
        
        maxcouplenr = 0
        
        for citizen1 in objs:
            if citizen1.couplenr > maxcouplenr:
                maxcouplenr = citizen1.couplenr
        
        citizen.couplenr = maxcouplenr + 1
        
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
        
        for citizen1 in objs:
            if citizen.gender == 'Male' and citizen1.gender == 'Female' and citizen1.age > 17 and citizen1.maritalstatus == 'Single':
                citizen1.maritalstatus = 'Married'
                citizen1.couplenr = citizen.couplenr
                citizen1.marriageduration = citizen.marriageduration
                citizen1.marriageenddate = citizen.marriageenddate
                citizen1.event = 'Life event: Married'
                new_event = {'Mutation date': mutationdate, 'ID': citizen1.ID, 'Gender': citizen1.gender,
                     'Age': citizen1.age, 'Birthdate': citizen1.birthdate, 
                     'Life expectancy': citizen1.lifeexpectancyprobability, 'Marital status': citizen1.maritalstatus,
                     'Couple nr': citizen1.couplenr, 'Marriage duration': citizen1.marriageduration, 
                     'Marriage end date': citizen1.marriageenddate, 'Marriage intention': citizen1.marriageintention, 
                     'Marriage age': citizen1.marriageage, 'Wedding date': citizen1.marriagedate, 
                     'Children': citizen1.children, 'Employment status': citizen1.employmentstatus, 'Income': citizen1.income, 
                     'Capital': citizen1.capital, 'NrChildren': citizen1.nrchildren, 'Birth age': citizen1.birthage, 
                     'Alive': citizen1.alive, 'Event': citizen1.event}
                df = df.append(new_event, ignore_index=True)
                break
            
            elif citizen.gender == 'Female' and citizen1.gender == 'Male' and citizen1.age > 17 and citizen1.maritalstatus == 'Single':
                citizen1.maritalstatus = 'Married'
                citizen1.couplenr = citizen.couplenr
                citizen1.marriageduration = citizen.marriageduration
                citizen1.marriageenddate = citizen.marriageenddate
                citizen.event1 = 'Life event: Married'
                new_event = {'Mutation date': mutationdate, 'ID': citizen1.ID, 'Gender': citizen1.gender,
                     'Age': citizen1.age, 'Birthdate': citizen1.birthdate, 
                     'Life expectancy': citizen1.lifeexpectancyprobability, 'Marital status': citizen1.maritalstatus,
                     'Couple nr': citizen1.couplenr, 'Marriage duration': citizen1.marriageduration, 
                     'Marriage end date': citizen1.marriageenddate, 'Marriage intention': citizen1.marriageintention, 
                     'Marriage age': citizen1.marriageage, 'Wedding date': citizen1.marriagedate, 
                     'Children': citizen1.children, 'Employment status': citizen1.employmentstatus, 'Income': citizen1.income, 
                     'Capital': citizen1.capital, 'NrChildren': citizen1.nrchildren, 'Birth age': citizen1.birthage, 
                     'Alive': citizen1.alive, 'Event': citizen1.event}
                df = df.append(new_event, ignore_index=True)
                break
        
    return df, citizen

    
    