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
        print("Married")
        citizen.maritalstatus = 'Married'
        citizen.event = 'Changed marital status (married)'
        new_event = {'Mutation date': currentdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Marriage intention': citizen.marriageintention, 'Marriage age': citizen.marriageage,
                     'Wedding date': citizen.marriagedate,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income,
                     'Alive': citizen.alive, 'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
    
    return df, citizen