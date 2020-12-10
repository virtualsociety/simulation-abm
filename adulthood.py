'''
Function to generate the life event of
entering into adulthood

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

def generateAdulthood(currentdate, age, birthdate, citizen, df):
    currentday = str(currentdate)
    birthday = str(birthdate)
    currentday = currentday[5:10]
    birthday = birthday[5:10]
    if currentday == birthday and age == 18 and citizen.alive == 1:
        citizen.event = 'Adulthood'
        new_event = {'Mutation date': currentdate, 'ID': citizen.ID, 'Gender': citizen.gender,
                     'Age': citizen.age, 'Birthdate': citizen.birthdate, 
                     'Life expectancy': citizen.lifeexpectancyprobability, 'Marital status': citizen.maritalstatus,
                     'Marriage duration': citizen.marriageduration, 'Marriage end date': citizen.marriageenddate,
                     'Employment status': citizen.employmentstatus, 'Income': citizen.income,
                     'Alive': citizen.alive, 'Event': citizen.event}
        df = df.append(new_event, ignore_index=True)
    return df, citizen
        