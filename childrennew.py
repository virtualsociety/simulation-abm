'''
Function to add nr children

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from nrchildrenprobability import calculateNrChildrenProbability
from nrchildren import generateNrChildren

def generateNewChildren(currentdate, citizen, df, df_nrchildren, objs):
    currentday = str(currentdate)
    currentday = currentday[:10]
    currentyear = currentday[:4]
    birthingday = str(citizen.birthingdate)
    if currentday == birthingday and citizen.alive == 1 and citizen.maritalstatus == 'Married':
        nrchildrenprobability = calculateNrChildrenProbability(df_nrchildren, currentyear)
        citizen.nrchildren = generateNrChildren(nrchildrenprobability, citizen.maritalstatus, citizen.age, citizen.children)
        
        citizen.event = 'Life event: Children born'
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
        
        for citizen1 in objs:
            if citizen1.couplenr == citizen.couplenr:
                citizen1.nrchildren = citizen.nrchildren
                citizen1.event = 'Life event: Children born'
                new_event = {'Mutation date': mutationdate, 'ID': citizen1.ID, 'Gender': citizen1.gender,
                             'Age': citizen1.age, 'Birthdate': citizen1.birthdate, 
                             'Life expectancy': citizen1.lifeexpectancyprobability, 'Marital status': citizen1.maritalstatus,
                             'Couple nr': citizen1.couplenr, 'Marriage duration': citizen1.marriageduration, 
                             'Marriage end date': citizen1.marriageenddate, 'Marriage intention': citizen1.marriageintention, 
                             'Marriage age': citizen1.marriageage, 'Wedding date': citizen1.marriagedate, 
                             'Children': citizen1.children, 'Employment status': citizen1.employmentstatus, 'Income': citizen1.income, 
                             'Capital': citizen1.capital, 'NrChildren': citizen1.nrchildren, 'Birth age': citizen1.birthage, 
                             'Birthing date': citizen1.birthingdate, 'Alive': citizen1.alive, 'Event': citizen1.event}
        
    return df, citizen, objs
