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