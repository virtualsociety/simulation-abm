'''
Function to generate new marriages

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def generateNewMarriage(currentdate, maritalstatus, weddingdate, citizen, df):
    currentday = str(currentdate)
    marriageday = str(weddingdate)
    currentday = currentday[:10]
    marriageday = marriageday[:10]
    #print(currentday)
    #print(marriageday)
    if currentday == marriageday and maritalstatus == 'Single' and citizen.alive == 1:
        citizen.maritalstatus = 'Married'
        citizen.event = 'Changed marital status (married)'
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
    return df, citizen