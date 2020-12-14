'''
Function to change the marital status into divorced

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def changeMaritalStatus(currentdate, maritalstatus, marriageenddate, citizen, df):
    
    currentday = str(currentdate)
    marriageendday = str(marriageenddate)
    currentday = currentday[:10]
    marriageendday = marriageendday[:10]
    
    if currentday == marriageendday and maritalstatus == 'Married' and citizen.alive == 1:
        citizen.maritalstatus = 'Divorced'
        citizen.event = 'Changed marital status (divorced)'
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