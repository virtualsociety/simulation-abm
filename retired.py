'''
Function to generate retirees

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def generateRetired(currentdate, citizen, df):

    currentday = str(currentdate)
    retiredday = str(citizen.birthdate)
    currentday = currentday[5:10]
    retiredday = retiredday[5:10]
    
    if currentday == retiredday and citizen.age >= 65 and citizen.employmentstatus != 'Retired' and citizen.alive == 1:
        citizen.employmentstatus = 'Retired'
        citizen.income = citizen.income * 0.70
        
        citizen.event = 'Life event: Retired'
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
                     'Alive': citizen.alive, 'Event': citizen.event}
        
        df = df.append(new_event, ignore_index=True)
    
    return df, citizen


